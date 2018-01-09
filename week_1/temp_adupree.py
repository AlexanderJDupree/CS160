#File: temp_adupree.py
#Description:Computes the wind-chill temperature
#Author:Alex DuPree, Alex Hoang
#Date: 10/06/2017
#Compiler: 3.4.1

#Poll user for outside temperature in degrees Fahrenheit,
#Poll user for wind speed
#Conditions, wind speed != < 2, -58 <= temp <= 41

print("This program computes the new wind-chill temperature")
print("by gathering the wind speed and current temperature from the user.")
print("\nThe formula cannot be used for wind speeds below 2MPH or")
print("temperatures below -58 degrees Fahrenheit or above 41 degrees.")

temp = float(input("\nCurrent outisde temperature in degrees Fahrenheit? "))
#Conditional check for variables outside of domain
if temp <= -58 or temp >= 41:
    print("\nError, temp must be above -58 degrees or below 41 degrees")
    quit()

wind_speed = float(input("\nCurrent wind speed in MPH? "))
#Conditional check for variables outside of domain
if wind_speed <= 2:
    print("\nError, wind speeds must be above 2 MPH")
    quit()
#computes wind chill with below formula
wind_chill = 35.74 + 0.6215*temp - 35.75*(wind_speed**0.16) + 0.4275 * temp * (wind_speed**0.16)
#prints the wind chill back to user.
print("\nThe current wind chill temp feels like", wind_chill, "degrees Fahrenheit")
