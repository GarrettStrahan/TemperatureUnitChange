def CelisusTofahrenheit(celsius):
    fahrenheit = 0
    celsius = float(celsius)
    fahrenheit = float(fahrenheit)
  #  celsius = input("What is the Celisus temp?")   #Remove the comment if you want to ask instead of pull it from Arguments
    print("The current celisus temperature is")
    print(celsius)
    print("Converting")
    fahrenheit =  (float(celsius) * 1.8)
    fahrenheit = fahrenheit + 32
    print("Converted to fahrenheit")
    print(fahrenheit)
#    return(fahrenheit)
def FahrenheitToCelsius(fahrenheit):
    print("The fahrenheit is currently at ")
    print(fahrenheit)
    print("Converting")
    celsius = fahrenheit - 32
    celsius = celsius * 5
    celsius = celsius / 9
    print("The value is now ")
    print(celsius)
