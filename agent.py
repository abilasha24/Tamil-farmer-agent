from groq import Groq
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tools.weather import get_weather
from tools.crops import suggest_crops
from tools.market import get_market_prices

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_farmer_agent(question, chat_history=[]):
    weather = get_weather("Jaffna")
    crops = suggest_crops(weather["temperature"], weather["humidity"])
    prices = get_market_prices()

    system_prompt = f"""நீ ஒரு அனுபவமுள்ள Tamil farmer assistant.
உன் பெயர் "விவசாய உதவியாளர்".
இப்போதைய Jaffna weather: {weather}
பரிந்துரைக்கப்பட்ட பயிர்கள்: {crops}
இன்றைய சந்தை விலை: {prices}

விதிகள்:
- எப்போதும் Tamil-ல மட்டும் பேசு
- Farmer-கிட்ட மரியாதையாக பேசு
- Short-ஆ, clear-ஆ answer கொடு
- உதவியான practical tips கொடு"""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content
    chat_history.append({"role": "user", "content": question})
    chat_history.append({"role": "assistant", "content": answer})

    return answer, chat_history

def main():
    print("=" * 50)
    print("🌾 Tamil Farmer Assistant 🌾")
    print("விவசாய உதவியாளர்")
    print("=" * 50)
    print("வெளியேற 'bye' type பண்ணுங்க")
    print("=" * 50)

    chat_history = []

    while True:
        question = input("\nநீங்கள்: ")
        if question.lower() == "bye":
            print("நன்றி! வணக்கம்! 🙏")
            break

        answer, chat_history = ask_farmer_agent(question, chat_history)
        print(f"\n🤖 உதவியாளர்: {answer}")

if __name__ == "__main__":
    main()