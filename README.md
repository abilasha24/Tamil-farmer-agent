# 🌾 Tamil Farmer Assistant — AI Agent for Agriculture

A Tamil-language multi-tool AI assistant built for farmers in Jaffna, Sri Lanka. It combines live weather data, rule-based crop recommendations, and market price information with an LLM-powered conversational interface — so farmers can get practical advice entirely in Tamil.

Originally built as the capstone project for the **Kaggle × Google 5-Day AI Agents Intensive (Vibe Coding) Course**.

## 🚀 Live Demo

🔗 **App:** https://tamil-farmer-agent-j3cyzcehjeedshdjfmt3mw.streamlit.app/

> Hosted on Streamlit Community Cloud, with UptimeRobot pinging every 5 minutes to prevent the free-tier app from sleeping.

## ✨ Features

- 🌤️ **Live weather** for Jaffna via the OpenWeatherMap API (temperature, humidity, conditions)
- 🌱 **Crop suggestions** generated from current temperature and humidity conditions
- 💰 **Market price snapshot** for common crops (rice, tomato, onion, chilli, banana, brinjal)
- 💬 **Tamil-only conversational chat**, powered by Groq's LLaMA 3.3 model, that stays grounded in the live weather/crop/price context for every answer
- 🧩 Two agent implementations included: a direct Groq chat-completion agent (`agent.py`) and a Google ADK multi-tool agent (`adk_agent.py`) that orchestrates the same three tools

## 🛠️ Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **LLM:** Groq API — LLaMA 3.3 (70B)
- **Agent Framework:** Google Agent Development Kit (ADK) with Gemini 1.5 Flash
- **External API:** OpenWeatherMap
- **Config:** python-dotenv for environment variables

## 🏗️ Project Structure

```text
Tamil-farmer-agent
├── app.py            # Streamlit UI — weather, crops, market price, chat
├── agent.py           # Groq-based conversational agent (CLI + chat logic)
├── adk_agent.py        # Google ADK multi-tool agent implementation
├── requirements.txt
└── tools/
    ├── weather.py       # OpenWeatherMap integration
    ├── crops.py         # Rule-based crop recommendation logic
    └── market.py        # Market price data
```

## 🏃 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/abilasha24/Tamil-farmer-agent.git
cd Tamil-farmer-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_openweathermap_api_key
```

> Never commit real API keys to GitHub.

### 4. Run the app

```bash
streamlit run app.py
```

## 📌 Project Highlights

- Multi-tool AI agent architecture combining external APIs, rule-based logic, and an LLM
- Fully Tamil-language system prompt and conversational responses
- Two parallel agent implementations (direct API vs. Google ADK) for comparison
- Deployed and monitored for uptime on a free-tier cloud host

## 👩‍💻 Author

**Abilasha Selvanayakam**

- GitHub: https://github.com/abilasha24
- LinkedIn: https://www.linkedin.com/in/abilashaselvanayakam2k06/
- Portfolio: https://my-portfolio-webapp-ashy.vercel.app/
