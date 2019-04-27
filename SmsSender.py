import time
import pyowm
from twilio.rest import Client


def send_sms(location):
    localtime = time.strftime('%I:%M:%S%p,%d-%B-%y')
    temperature = get_weather(location)
    twilio_account_key = "ACf15cca26781eb59a937ddc7c88568856"
    twilio_authentication_token = "43e29cf2823848c7b5d5dc60a0e9ee4b"
    client = Client(twilio_account_key, twilio_authentication_token)
    client.messages.create(to="+923043404677", from_="+15866661648",
                           body="Temperature at "+ location+" on ( "+localtime+" ) is "+ str(temperature)+"'C")




def get_weather(location):
    apiKey = 'a1db274fcb4e9a13a14e52e569c6fd1a'
    openWeatherClient = pyowm.OWM(apiKey)
    observation = openWeatherClient.weather_at_place(location)
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    return temperature
