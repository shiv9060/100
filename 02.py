#Writeaprogramthatwillconvertcelsiusvaluetofahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit. ")
