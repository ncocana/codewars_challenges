from src.convert_to_celsius import convert_to_celsius

def weather_info (temp):
    c = convert_to_celsius(temp)
    if c < 0:
        return str(c) + " is freezing temperature"
    else:
        return str(c) + " is above freezing temperature"