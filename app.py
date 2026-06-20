import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tools.weather import get_weather
from tools.crops import suggest_crops
from tools.market import get_market_prices
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(
    page_title="Tamil Farmer Assistant",
    page_icon="🌾",
    layout="centered"
)

# Title
st.title("🌾 Tamil Farmer Assistant")
st.subheader("விவசாய உதவியாளர் - யாழ்ப்பாணம்")
st.divider()

# Weather section
st.subheader("🌤️ இன்றைய வானிலை")
weather = get_weather("Jaffna")
col1, col2, col3 = st.columns(3)
col1.metric("வெப்பநிலை", f"{weather['temperature']}°C")
col2.metric("ஈரப்பதம்", f"{weather['humidity']}%")
col3.metric("நிலை", weather['description'])

st.divider()

# Crop section
st.subheader("🌱 பரிந்துரைக்கப்பட்ட பயிர்கள்")
crops = suggest_crops(weather["temperature"], weather["humidity"])
for crop in crops:
    st.success(f"✅ {crop}")

st.divider()

# Market price section
st.subheader("💰 இன்றைய சந்தை விலை")
prices = get_market_prices()
for crop, info in prices.items():
    st.info(f"🌾 {crop}: ரூ.{info['price']}/{info['unit']} {info['trend']}")

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
if question := st.chat_input("உங்கள் கேள்வியை இங்க type பண்ணுங்க..."):
    with st.chat_message("user"):
        st.write(question)
    st.session_state.messages.append({"role": "user", "content": question})

    system_prompt = f"""நீ ஒரு அனுபவமுள்ள Tamil farmer assistant.
இப்போதைய Jaffna weather: {weather}
பரிந்துரைக்கப்பட்ட பயிர்கள்: {crops}
இன்றைய சந்தை விலை: {prices}
எப்போதும் Tamil-ல மட்டும் பேசு. Short-ஆ clear-ஆ answer கொடு."""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(st.session_state.chat_history)
    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "user", "content": question})
    st.session_state.chat_history.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})