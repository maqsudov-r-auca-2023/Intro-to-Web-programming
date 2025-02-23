import requests

api_key = "your_api_key_here"
city = input("Enter the city name: ")  # Take input from the user
api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(api_url)
data = response.json()

if "error" in data:
    print("Invalid city name. Please try again.")
else:
    print(f"Weather in {city}: {data['current']['temp_c']}°C")
