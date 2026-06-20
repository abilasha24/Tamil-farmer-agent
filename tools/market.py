def get_market_prices():
    # Real API இல்லாததால் இப்போ static data use பண்றோம்
    prices = {
        "நெல் (Rice)": {"price": 45, "unit": "கிலோ", "trend": "↑ அதிகரிக்குது"},
        "தக்காளி (Tomato)": {"price": 30, "unit": "கிலோ", "trend": "↓ குறைகுது"},
        "வெங்காயம் (Onion)": {"price": 55, "unit": "கிலோ", "trend": "→ நிலையானது"},
        "மிளகாய் (Chilli)": {"price": 120, "unit": "கிலோ", "trend": "↑ அதிகரிக்குது"},
        "வாழை (Banana)": {"price": 25, "unit": "கிலோ", "trend": "→ நிலையானது"},
        "கத்தரிக்காய் (Brinjal)": {"price": 20, "unit": "கிலோ", "trend": "↓ குறைகுது"},
    }
    return prices

if __name__ == "__main__":
    prices = get_market_prices()
    print("இன்றைய யாழ்ப்பாண சந்தை விலை:")
    print("-" * 40)
    for crop, info in prices.items():
        print(f"🌾 {crop}: ரூ.{info['price']}/{info['unit']} {info['trend']}")