from agents import function_tool


@function_tool
def add(a:int,b:int) -> str:

    """This is add function
    arg:
         a:int
         b:int
         result:str
    """
    print("add tool fire ------>")
    return a + b



@function_tool
def get_weather(city:str) -> str:

    """This is get_weather function"""

    print("get_weather tool fire ------>")
    weather = {
        "karachi": " Sunny, 32°C",
        "lahore": " Partly Cloudy, 30°C",
        "islamabad": " Thunderstorms, 28°C"
    }
    return weather.get(city.lower(), f"Weather for {city} not found.")
    

