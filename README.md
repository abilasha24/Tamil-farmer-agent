# 🌾 Tamil Farmer Assistant

An AI-powered agricultural assistant designed to help farmers in Jaffna, Sri Lanka, with weather updates, weather forecasts, crop suggestions, market price information, and Tamil-language agricultural support.

## 🚀 Features

- **Current Weather:** Displays current weather conditions in Jaffna.
- **4-Day Weather Forecast:** Shows upcoming weather forecasts, temperature ranges, and rain probabilities.
- **Crop Suggestions:** Provides crop suggestions based on temperature and humidity.
- **Market Prices:** Displays manually maintained agricultural market prices and trends.
- **Tamil AI Chatbot:** Answers agricultural questions in simple Tamil.
- **Forecast-Based Answers:** Uses weather forecast information to answer questions about upcoming rain and farming activities.

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- LLaMA / supported Groq model
- OpenWeatherMap API
- Requests
- python-dotenv
- Git and GitHub

## 📁 Project Structure

```text
tamil-farmer-agent/
│
├── app.py
├── tools/
│   ├── weather.py
│   ├── crops.py
│   └── market.py
│
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/abilasha24/Tamil-farmer-agent.git
```

### 2. Open the project folder

```bash
cd Tamil-farmer-agent
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install streamlit requests python-dotenv groq
```

## 🔑 Environment Variables

Create a `.env` file in the project root directory.

Add your own API keys:

```env
WEATHER_API_KEY=your_openweathermap_api_key
GROQ_API_KEY=your_groq_api_key
```

Replace the example values with your actual API keys.

**Important:** Never upload your `.env` file or expose your API keys on GitHub.

## ▶️ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🌦️ Weather and Market Data Notes

- Weather information is retrieved using the weather API.
- Forecast information is based on available forecast data and may change.
- Market prices are manually maintained and are not live market prices.
- Crop suggestions are general recommendations, not guaranteed agricultural outcomes.

## 🎯 Project Goal

The goal of this project is to make useful weather and agricultural information more accessible to farmers in Jaffna through a simple Tamil-language AI assistant.

## 👩‍💻 Developer

**Abilasha Selvanayakam**

- GitHub: https://github.com/abilasha24

---

*Built with Python, Streamlit, and AI to support Tamil-speaking farmers.*
