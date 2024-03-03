def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (Celsius, Fahrenheit, or Kelvin): ").lower()

    if unit == 'celsius':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
    elif unit == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
    elif unit == 'kelvin':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
    else:
        print("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")
        return

    print(f"\nConverted Temperatures:")
    if unit == 'celsius':
        print(f"Fahrenheit: {fahrenheit:.2f} °F")
        print(f"Kelvin: {kelvin:.2f} K")
    elif unit == 'fahrenheit':
        print(f"Celsius: {celsius:.2f} °C")
        print(f"Kelvin: {kelvin:.2f} K")
    elif unit == 'kelvin':
        print(f"Celsius: {celsius:.2f} °C")
        print(f"Fahrenheit: {fahrenheit:.2f} °F")

if __name__ == "__main__":
    main()
