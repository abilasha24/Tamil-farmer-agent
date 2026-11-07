
import streamlit as st
import sys
import os

# Project folder path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Page config - must be the first Streamlit command
st.set_page_config(
    page_title="Tamil Farmer Assistant",
    page_icon="🌾",
    layout="centered"
)

# Imports
import importlib
import tools.weather as weather_module

# Reload the weather module
weather_module = importlib.reload(weather_module)

get_weather = weather_module.get_weather
get_forecast = getattr(weather_module, "get_forecast", None)
from tools.crops import suggest_crops
from tools.market import get_market_prices
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Title
st.title("🌾 Tamil Farmer Assistant")
st.subheader("விவசாய உதவியாளர் - யாழ்ப்பாணம்")
st.divider()


# Weather section
st.subheader("🌤️ தற்போதைய வானிலை")

weather = get_weather("Jaffna")

crops = []
prices = {}
forecast_data = {"forecast": []}

if "error" in weather:

    st.warning(weather["error"])

else:

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "வெப்பநிலை",
        f"{weather['temperature']}°C"
    )

    col2.metric(
        "ஈரப்பதம்",
        f"{weather['humidity']}%"
    )

    col3.metric(
        "நிலை",
        weather["description"]
    )

st.divider()


# Weather Forecast section
st.subheader("🌧️ அடுத்த 4 நாட்கள் வானிலை முன்னறிவிப்பு")

if get_forecast is None:

    st.info("வானிலை முன்னறிவிப்பு வசதி தற்போது கிடைக்கவில்லை.")

else:

    forecast_data = get_forecast("Jaffna")

    if "error" in forecast_data:

        st.warning(forecast_data["error"])

    else:

        forecast_days = forecast_data.get("forecast", [])

        if forecast_days:

            columns = st.columns(len(forecast_days))

            for col, day in zip(columns, forecast_days):

                with col:

                    st.markdown(f"**{day['date']}**")

                    st.metric(
                        "குறைந்த வெப்பநிலை",
                        f"{day['min_temp']}°C"
                    )

                    st.metric(
                        "அதிக வெப்பநிலை",
                        f"{day['max_temp']}°C"
                    )

                    st.metric(
                        "மழை வாய்ப்பு",
                        f"{day['rain_probability']}%"
                    )

                    st.caption(day["description"])

        else:

            st.info("வானிலை முன்னறிவிப்பு கிடைக்கவில்லை.")

st.divider()


# Crop section
st.subheader("🌱 பரிந்துரைக்கப்பட்ட பயிர்கள்")

if "error" not in weather:

    crops = suggest_crops(
        weather["temperature"],
        weather["humidity"]
    )

    for crop in crops:
        st.success(f"✅ {crop}")

else:

    st.info("வானிலைத் தகவல் கிடைத்த பிறகு பயிர் பரிந்துரை வழங்கப்படும்.")

st.divider()


# Market price section
st.subheader("💰 சந்தை விலை விவரங்கள்")

st.caption(
    "குறிப்பு: இவை கைமுறையாகப் பராமரிக்கப்படும் விலைகள். Live market data அல்ல."
)

prices = get_market_prices()

for crop, info in prices.items():

    st.info(
        f"🌾 {crop}: ரூ.{info['price']}/{info['unit']} {info['trend']}"
    )

st.divider()


# Chat section
st.subheader("💬 கேள்வி கேளுங்கள்")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "messages" not in st.session_state:
    st.session_state.messages = []


# Show chat history
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# Chat input
if question := st.chat_input(
    "உங்கள் கேள்வியை இங்கே type பண்ணுங்க..."
):

    with st.chat_message("user"):
        st.write(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })


    # System prompt
    system_prompt = f"""
நீ யாழ்ப்பாண விவசாயிகளுக்கு உதவும் அனுபவமுள்ள
தமிழ் விவசாய உதவியாளர்.

தற்போதைய வானிலைத் தகவல்:
{weather}

அடுத்த 4 நாட்கள் வானிலை முன்னறிவிப்பு:
{forecast_data}

பரிந்துரைக்கப்பட்ட பயிர்கள்:
{crops}

சந்தை விலைத் தகவல்:
{prices}

முக்கியமான விதிமுறைகள்:

1. எப்போதும் எளிய, தெளிவான தமிழில் பதிலளி.
2. விவசாயிகளுக்குப் புரியும் வகையில் விளக்கு.
3. தற்போதைய வானிலையை வைத்து எதிர்கால மழையை
   உறுதியாகக் கூறாதே.
4. வெப்பநிலை மற்றும் ஈரப்பதம் மட்டும் வைத்து
   பயிர் நிச்சயமாக வளரும் என்று கூறாதே.
5. மண் வகை, பருவம், நீர் வசதி ஆகியவற்றையும்
   கருத்தில் கொள்.
6. சந்தை விலைகள் static/manual தகவல்கள்.
   அவற்றை live prices என்று கூறாதே.
7. விலை குறைவாக இருப்பதால் அதிக லாபம் என்று
   முடிவு செய்யாதே.
8. தகவல் இல்லையென்றால் கற்பனை செய்யாதே.
   தேவையான விவரங்களைக் கேள்.
9. நோய் அல்லது பூச்சித் தாக்குதல் பற்றிக் கேட்டால்
   அறிகுறிகளை முதலில் கேள்.
10. சுருக்கமாகவும் தெளிவாகவும் பதிலளி.

11. பயனர் Tamil words-ஐ English letters-ல்
    எழுதினாலும் அதன் அர்த்தத்தைப் புரிந்துகொள்.

12. "malai", "mazhai", "mazha" போன்ற சொற்கள்
    வானிலை தொடர்பான கேள்வியில் வந்தால்
    அவற்றை மழை (rain) என்று புரிந்துகொள்.

13. "hail" அல்லது "aalangatti mazhai" என்றால்
    மட்டுமே ஆலங்கட்டி மழை என்று புரிந்துகொள்.

14. "Jaffna la malai varumoo" என்றால்
    "யாழ்ப்பாணத்தில் மழை வருமா?" என்று
    புரிந்துகொண்டு பதிலளி.

15. அடுத்த 4 நாட்கள் forecast தகவல் இருந்தால்
    அதைப் பயன்படுத்தி மழை வாய்ப்பை விளக்கு.
    மழை வாய்ப்பு 100% என்றாலும் அது உறுதியான
    மழை அளவு அல்ல; forecast probability என்று
    தெளிவுபடுத்து.

16. குறிப்பிட்ட நாளைப் பற்றிக் கேட்டால் அந்த
    நாளின் forecast தகவலை மட்டும் பயன்படுத்தி
    பதிலளி. Forecast கிடைக்காவிட்டால்
    ஊகித்துப் பதிலளிக்காதே.
17. பதில்களை எளிய தமிழில் சுருக்கமாகக் கொடு.
    பொதுவாக 5 முதல் 8 முக்கியமான வரிகள் போதும்.

18. உறுதிப்படுத்தப்படாத விவசாயத் தகவல்களை
    உண்மை என்று கூறாதே.

19. மண் வகை, பயிரின் வளர்ச்சி நிலை போன்ற
    விவரங்கள் தெரியாவிட்டால் குறிப்பிட்ட
    மருந்து அல்லது உரத்தைப் பரிந்துரைக்காதே.

20. வானிலை forecast என்பது கணிப்பு மட்டுமே.
    100% என்று இருந்தாலும் உண்மையான மழையை
    உறுதியாகக் கூறாதே.

21. பயனர் குறிப்பிட்ட பயிரைப் பற்றிக் கேட்காவிட்டால்
    எல்லாப் பயிர்களுக்கும் ஒரே ஆலோசனை கொடுக்காதே.
"""


    # Prepare messages
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(st.session_state.chat_history)

    messages.append({
        "role": "user",
        "content": question
    })


    # Groq API call
    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages
        )

        answer = response.choices[0].message.content

        # Save chat history
        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })

        # Display AI response
        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:

        st.error(f"AI பதிலளிப்பதில் பிழை ஏற்பட்டது: {e}")
