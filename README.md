# 🌾 Tamil Farmer Assistant

An AI-powered, Tamil-language agricultural assistant built for farmers in Jaffna, Sri Lanka. It combines weather information, rule-based crop recommendations, market price snapshots, and an LLM-powered conversational interface to provide practical agricultural guidance in Tamil.

Originally developed as a capstone project for the **Kaggle × Google 5-Day AI Agents Intensive Course**.

## 🚀 Live Demo

[Open Tamil Farmer Assistant](https://tamil-farmer-agent-j3cyzcehjeedshdjfmt3mw.streamlit.app/)

Hosted on Streamlit Community Cloud.

## ✨ Features

- 🌤️ **Weather Information:** Retrieves weather data for Jaffna using the OpenWeatherMap API.
- 🌱 **Crop Recommendations:** Suggests suitable crops based on temperature and humidity using rule-based logic.
- 💰 **Market Price Snapshot:** Displays price information for common crops, including rice, tomato, onion, chilli, banana, and brinjal.
- 💬 **Tamil Conversational Assistant:** Provides agricultural guidance through an LLM-powered chat interface.
- 🧩 **Multi-Agent Implementations:** Includes a direct Groq-based conversational agent and a Google ADK multi-tool agent.

## 🛠️ Tech Stack

- **Language:** Python
- **UI Framework:** Streamlit
- **LLM API:** Groq API
- **LLM Model:** OpenAI GPT-OSS 120B
- **Agent Framework:** Google Agent Development Kit (ADK)
- **Weather API:** OpenWeatherMap
- **Environment Configuration:** python-dotenv

## 🏗️ Project Structure

```text
Tamil-farmer-agent/
├── app.py
├── agent.py
├── adk_agent.py
├── requirements.txt
└── tools/
    ├── weather.py
    ├── crops.py
    └── market.py
```

- `app.py` – Streamlit application and user interface.
- `agent.py` – Groq-based conversational agent.
- `adk_agent.py` – Google ADK agent implementation.
- `tools/weather.py` – Weather data integration.
- `tools/crops.py` – Rule-based crop recommendation logic.
- `tools/market.py` – Market price information.

## 🏃 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/abilasha24/Tamil-farmer-agent.git
cd Tamil-farmer-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_openweathermap_api_key
```

Never upload real API keys or secrets to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

## 🎯 Project Purpose

Farmers in Jaffna, Sri Lanka need accessible agricultural information in their native Tamil language. This project aims to make weather information, crop recommendations, and agricultural guidance easier to access through a conversational AI assistant.

## 📌 Project Highlights

- Combines external API integration, rule-based logic, and an LLM.
- Provides a Tamil-language conversational interface.
- Includes two agent implementations for exploring different AI agent architectures.
- Deployed using Streamlit Community Cloud.

## 👩‍💻 Author

**Abilasha Selvanayakam**

- GitHub: [abilasha24](https://github.com/abilasha24)
- LinkedIn: [Abilasha Selvanayakam](https://www.linkedin.com/in/abilashaselvanayakam2k06/)
- Portfolio: [My Portfolio](https://my-portfolio-webapp-ashy.vercel.app/)