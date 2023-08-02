import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Error fetching weather data.")
        return []

def get_temperature(data, date):
    for entry in data:
        if date in entry["dt_txt"]:
            return entry["main"]["temp"]
    return None

def get_wind_speed(data, date):
    for entry in data:
        if date in entry["dt_txt"]:
            return entry["wind"]["speed"]
    return None

def get_pressure(data, date):
    for entry in data:
        if date in entry["dt_txt"]:
            return entry["main"]["pressure"]
    return None

def main():
    weather_data = get_weather_data()
    #print(weather_data)
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (yyyy-mm-dd hh:mm:ss): ")
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} K")
            else:
                print("Data not available for the selected date.")

        elif choice == "2":
            date = input("Enter the date (yyyy-mm-dd hh:mm:ss): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available for the selected date.")

        elif choice == "3":
            date = input("Enter the date (yyyy-mm-dd hh:mm:ss): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the selected date.")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
