import random

temp=random.randint(1,200)
humidity=random.randint(1,200)

print("temperature:",temp)
if temp > 15 and temp < 25:

    print("temperature is normal")
elif temp < 20:
    print("temperature is low")
else:
    print("temperature is  high")

print("Humidity:",humidity)
if humidity> 30 and humidity < 60:
    print("humidity is normal")
elif humidity < 35:
    print("humidity is low")
else:
    print("humidity is  high")
    
