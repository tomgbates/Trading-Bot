import psutil

battery = psutil.sensors_battery()

# Returns percentage battery life remaining
print("Battery percentage: ", battery.percent)

# Returns True or False. If laptop is plugged in == True, if laptop is not plugged in == False
print("Power plugged in: ", battery.power_plugged)