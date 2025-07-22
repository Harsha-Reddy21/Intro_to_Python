
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Sample Temperature Conversions:")
    c = 25
    f = 77
    k = 298.15

    print(f"{c}°C to Fahrenheit: {celsius_to_fahrenheit(c):.2f}°F")
    print(f"{f}°F to Celsius: {fahrenheit_to_celsius(f):.2f}°C")
    print(f"{c}°C to Kelvin: {celsius_to_kelvin(c):.2f}K")
    print(f"{k}K to Celsius: {kelvin_to_celsius(k):.2f}°C")
    print(f"{f}°F to Kelvin: {fahrenheit_to_kelvin(f):.2f}K")
    print(f"{k}K to Fahrenheit: {kelvin_to_fahrenheit(k):.2f}°F")


if __name__ == "__main__":
    main()
