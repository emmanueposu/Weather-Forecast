import json
from socket import *

suggestions = {
    "95": {
        "clear sky": {
            "clothing": "Light breathable clothing",
            "activity": "Go swimming or have a picnic in the shade",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "thunderstorm": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Avoid the outdoors",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "poor air quality": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Limit outdoor exposure",
            "accessories": "Respirator"
        },
        "snow": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Sunglasses or goggles"
        }
    },
    "85": {
        "clear sky": {
            "clothing": "Light breathable clothing",
            "activity": "Go swimming or have a picnic in the shade",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "thunderstorm": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Avoid the outdoors",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "poor air quality": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Limit outdoor exposure",
            "accessories": "Respirator"
        },
        "snow": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Sunglasses or goggles"
        }
    },
    "70": {
        "clear sky": {
            "clothing": "Light breathable clothing",
            "activity": "Go swimming or have a picnic in the shade",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "thunderstorm": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Avoid the outdoors",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "poor air quality": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Limit outdoor exposure",
            "accessories": "Respirator"
        },
        "snow": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Sunglasses or goggles"
        }
    },
    "50": {
        "clear sky": {
            "clothing": "Warm breathable clothing",
            "activity": "Go for a walk or have a picnic in the shade",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Warm breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sweater"
        },
        "thunderstorm": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Avoid the outdoors",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "poor air quality": {
            "clothing": "Warm breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Limit outdoor exposure",
            "accessories": "Respirator"
        },
        "snow": {
            "clothing": "Warm water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Sunglasses or goggles"
        }
    },
    "30": {
        "clear sky": {
            "clothing": "Warm breathable clothing",
            "activity": "Go for a walk",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Warm clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Beanie"
        },
        "thunderstorm": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Avoid the outdoors",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Umbrella"
        },
        "poor air quality": {
            "clothing": "Warm breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Limit outdoor exposure",
            "accessories": "Respirator"
        },
        "snow": {
            "clothing": "Warm Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Sunglasses or goggles"
        }
    },
    "10": {
        "clear sky": {
            "clothing": "Light breathable clothing",
            "activity": "Go swimming or have a picnic in the shade",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "thunderstorm": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Avoid the outdoors",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "poor air quality": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Limit outdoor exposure",
            "accessories": "Respirator"
        },
        "snow": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Sunglasses or goggles"
        }
    },
    "0": {
        "clear sky": {
            "clothing": "Warm heavy breathable clothing",
            "activity": "Go swimming or have a picnic in the shade",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "thunderstorm": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Avoid the outdoors",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be aware of changing weather conditions",
            "accessories": "Sunblock or hat"
        },
        "poor air quality": {
            "clothing": "Light breathable clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Limit outdoor exposure",
            "accessories": "Respirator"
        },
        "snow": {
            "clothing": "Water resistant clothing",
            "activity": "Read a book or watch a movie",
            "precautions": "Be cautious of slippery surfaces",
            "accessories": "Sunglasses or goggles"
        }
    }
}

weatherServiceSocket = socket(AF_INET, SOCK_STREAM)

weatherServiceAddress = ('localhost', 3000)

weatherServiceSocket.bind(weatherServiceAddress)

weatherServiceSocket.listen(1)

print('Weather Service listening on {}:{}'.format(*weatherServiceAddress))

while True:
    clientSocket, clientAddress = weatherServiceSocket.accept()

    dataStr = clientSocket.recv(1024).decode()
    print('Received from client:', dataStr)

    dataObj = json.loads(dataStr)

    weather = dataObj["description"]
    temp = int(dataObj["temperature"])
    unit = dataObj["unit"]

    if unit.lower() == "c":
        temp = (temp * 9 / 5) + 32

    if weather in {"smoke", "haze", "sand/dust whirls", "sand", "dust", "volcanic ash", "squalls", "tornado"}:
        weather = "poor air quality"

    elif weather in {"overcast clouds", "few clouds", "scattered clouds", "broken clouds"}:
        weather = "clouds"

    elif weather == "fog":
        weather = "mist"

    elif weather in {"thunderstorm with light rain", "thunderstorm with rain", "thunderstorm with heavy rain",
                     "light thunderstorm", "thunderstorm", "heavy thunderstorm", "ragged thunderstorm",
                     "thunderstorm with light drizzle", "thunderstorm with drizzle", "thunderstorm with heavy drizzle"}:
        weather = "thunderstorm"

    elif weather in {"light intensity drizzle", "drizzle", "heavy intensity drizzle", "light intensity drizzle rain",
                     "drizzle rain", "heavy intensity drizzle rain", "shower rain and drizzle",
                     "heavy shower rain and drizzle", "shower drizzle"}:
        weather = "rain"

    elif weather in {"light rain", "moderate rain", "heavy intensity rain", "very heavy rain", "extreme rain",
                     "freezing rain", "light intensity shower rain", "shower rain", "heavy intensity shower rain",
                     "ragged shower rain"}:
        weather = "rain"

    elif weather in {"light snow", "snow", "heavy snow", "sleet", "light shower sleet", "shower sleet",
                     "light rain and snow", "rain and snow", "light shower snow", "shower snow", "heavy shower snow"}:
        weather = "snow"

    if temp >= 95:
        response = suggestions["95"][weather]

    elif 95 > temp >= 85:
        response = suggestions["85"][weather]

    elif 85 > temp >= 70:
        response = suggestions["70"][weather]

    elif 70 > temp >= 50:
        response = suggestions["50"][weather]

    elif 50 > temp >= 30:
        response = suggestions["30"][weather]

    elif 30 > temp >= 10:
        response = suggestions["10"][weather]

    else:
        response = suggestions["0"][weather]

    responseStr = json.dumps(response)
    print('Sent to client:', responseStr)
    clientSocket.send(responseStr.encode())

    clientSocket.close()
