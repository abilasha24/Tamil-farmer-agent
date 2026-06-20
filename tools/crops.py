def suggest_crops(temperature, humidity):
    crops = []
    
    if temperature >= 25 and temperature <= 35:
        if humidity >= 70:
            crops.append("நெல் (Rice) - ஈரப்பதம் அதிகம், நல்லா விளையும்")
            crops.append("வாழை (Banana) - இந்த வெப்பநிலையில் நல்லா வளரும்")
        if humidity < 70:
            crops.append("மிளகாய் (Chilli) - குறைந்த ஈரப்பதத்தில் நல்லா விளையும்")
            crops.append("வெங்காயம் (Onion) - இந்த weather-ல perfect")
    
    if temperature >= 20 and temperature <= 30:
        crops.append("தக்காளி (Tomato) - இந்த temperature-ல best")
        crops.append("கத்தரிக்காய் (Brinjal) - நல்லா விளையும்")
    
    if temperature > 35:
        crops.append("கம்பு (Pearl Millet) - வெப்பமான சூழலில் தாங்கும்")
        crops.append("சோளம் (Sorghum) - வறட்சியை தாங்கும்")
    
    if not crops:
        crops.append("இந்த வானிலையில் பயிரிட கஷ்டம் - நிபுணரை கேளுங்கள்")
    
    return crops

if __name__ == "__main__":
    # Test - Jaffna weather
    result = suggest_crops(28, 86)
    print("பரிந்துரைக்கப்பட்ட பயிர்கள்:")
    for crop in result:
        print(f"✅ {crop}")