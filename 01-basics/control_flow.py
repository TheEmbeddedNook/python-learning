#########################
## simple if
#########################
print("Simple if example")
battery_voltage = 12.4

print(f"Battery Voltage: {battery_voltage} V")

if battery_voltage > 11.5:
    print("Battery Healthy")

print("System Check Complete")

#########################
##  if --else
#########################
print("if-else example")

battery_voltage = 10.8

if battery_voltage > 11.5:
    print("Battery Healthy")
else:
    print("Battery Low")

#########################
## if elif --else
#########################
print("if-elif-else example")
temperature = 92

if temperature >= 100:
    print("Critical Temperature")
elif temperature >= 80:
    print("High Temperature")
elif temperature >= 50:
    print("Normal Temperature")
else:
    print("Cold")