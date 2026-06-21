from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tools.weather import get_weather
from tools.crops import suggest_crops
from tools.market import get_market_prices

load_dotenv()

# Tool 1 — Weather
def weather_tool(city: str = "Jaffna") -> dict:
    """Get current weather for a city"""
    return get_weather(city)

# Tool 2 — Crop Suggestion
def crop_tool(temperature: float, humidity: float) -> list:
    """Suggest crops based on weather conditions"""
    return suggest_crops(temperature, humidity)

# Tool 3 — Market Price
def market_tool() -> dict:
    """Get current market prices for crops"""
    return get_market_prices()

# ADK Agent create பண்ணு
farmer_agent = Agent(
    name="tamil_farmer_assistant",
    model="gemini-1.5-flash-latest",
    description="Tamil Farmer Assistant for Jaffna agriculture",
    instruction="""நீ ஒரு அனுபவமுள்ள Tamil farmer assistant.
    எப்போதும் Tamil-ல பேசு.
    Weather, crop suggestion, market price tools use பண்ணி farmers-க்கு உதவு.
    Short-ஆ, clear-ஆ, practical-ஆ answer கொடு.""",
    tools=[weather_tool, crop_tool, market_tool],
)

async def run_agent(question: str):
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="tamil_farmer",
        user_id="farmer_1"
    )
    
    runner = Runner(
        agent=farmer_agent,
        app_name="tamil_farmer",
        session_service=session_service
    )
    
    content = types.Content(
        role="user",
        parts=[types.Part(text=question)]
    )
    
    async for event in runner.run_async(
        user_id="farmer_1",
        session_id=session.id,
        new_message=content
    ):
        if event.is_final_response():
            print(f"\n🤖 விவசாய உதவியாளர்: {event.response.text}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_agent("இன்னைக்கு என்ன பயிர் போடலாம்?"))