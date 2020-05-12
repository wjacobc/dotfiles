import requests
from datetime import datetime
import time

# First get the text from wttr.in using the -T option, which removes color
try:
    weather_string = requests.get("http://wttr.in/?T").text
except requests.exceptions.ConnectionError:
    time.sleep(10)
    weather_string = requests.get("http://wttr.in/?T").text

# If wttr.in is down, just do nothing rather than throw an error
if "Sorry" in weather_string:
    quit()

# We only need the third and fourth lines, which have the current condition and temperature
weather_string_list = weather_string.split("\n")[2:4]
# Finally we remove everything up to the condition and the temperature, and remove the
# trailing whitespace so that we just have the condition text and the two temperatures
weather_string_list[:] = [string[15:].strip() for string in weather_string_list]

condition, temperature = tuple(weather_string_list)

# Since we are given two temperatures, we convert them to ints, take the average, and
# convert the average back into a formatted string
if (len(temperature) < 6):
    temperature = temperature[:2] + "°"
elif "+" in temperature:
    temperature = str(int((int(temperature[:2]) + int(temperature[5:7])) / 2)) + "°"
else:
    temperature = str(int((int(temperature[:2]) + int(temperature[4:6])) / 2)) + "°"

# Since wttr.in gives us some complex conditions, we can simplify them down
if "thunder" in condition.lower() and "patch" not in condition.lower():
    condition = "Thunderstorms"
elif "rain" in condition.lower():
    condition = "Rain"

valid_conditions_day = {"Sunny": "", "Clear": "", "Partly cloudy": "", "Fog": "", "Overcast": "", "Rain": "", "Thunderstorms": ""}

valid_conditions_night = {"Sunny": "", "Clear": "", "Partly cloudy": "", "Fog": "", "Overcast": "", "Rain": "", "Thunderstorms": ""}

time = datetime.now().time()
vaguely_sunset = datetime.strptime("20:30","%H:%M").time()
vaguely_sunrise = datetime.strptime("07:30", "%H:%M").time()

night = False
# If the current time is after sunset or before sunrise, we enable a second set
# of condition glyphs that are correct for nighttime
if (time > vaguely_sunset or time < vaguely_sunrise):
    night = True

if condition in valid_conditions_day and not night:
    condition = valid_conditions_day[condition]
elif condition in valid_conditions_night and night:
    condition = valid_conditions_night[condition]

print(condition + " " + temperature)

