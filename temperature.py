import requests

LOCATION_KEY = "2102499"
API_KEY = '794dd492f0181a66f673f0973093d5f4'
lat = 40.60407
lon = -74.13266


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def get_temperature(date):
    # url = f"https://api.openweathermap.org/data/3.0/onecall?lat=40.60407&lon=-74.13266&appid=794dd492f0181a66f673f0973093d5f4"
    # url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&appid={API_KEY}"
    # response = requests.get(url)
    # data = response.json()
    #
    # if response.status_code == 200 and data:
    #     high_temp = kelvin_to_fahrenheit(data["temperature"]["max"])
    #     low_temp = kelvin_to_fahrenheit(data["temperature"]["min"])
    #     return high_temp.__round__(2), low_temp.__round__(2)
    return 0, 1


if __name__ == "__main__":
    print(get_temperature("2025-03-10"))
