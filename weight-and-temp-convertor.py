def tempConvertor():
    unit = input("The temperature in which unit (C/F/K) = ").upper()
    temp = float(input("Enter the temperature = "))

    choose = input('''In which unit you want to see the temperature
                    1. Celsius
                    2. Fahrenheit
                    3. Kelvin
                    4. ALL
                    ''')
    if unit == 'C':
        Cel = temp
        Fah = round((9 * temp) / 5 + 32, 1)
        Kelvin = round(temp + 273.15, 1)
    elif unit == 'F':
        Cel = round((temp - 32) * 5 / 9, 1)
        Fah = temp
        Kelvin = round((temp - 32) * 5 / 9 + 273.15, 1)
    elif unit == 'K':
        Cel = round(temp - 273.15, 1)
        Fah = round((temp - 273.15) * 9 / 5 + 32, 1)
        Kelvin = temp
    else:
        print("Invalid unit")
        exit()

    if int(choose) == 1:
        print(f"The temperature {temp} in Celsius is {Cel}")
    elif int(choose) == 2:
        print(f"The temperature {temp} in Fahrenheit is {Fah}")
    elif int(choose) == 3:
        print(f"The temperature {temp} in Kelvin is {Kelvin}")
    elif int(choose) == 4:
        print(f"The temperature {temp} in Celsius is {Cel}")
        print(f"The temperature {temp} in Fahrenheit is {Fah}")
        print(f"The temperature {temp} in Kelvin is {Kelvin}")
    else:
        print("Invalid choice")
tempConvertor()
def Weightconvertor():
    
    unit_from = input("Enter the current unit (kg, lb, g, oz, ton, mg): ").lower()
    weight = float(input("Enter the weight: "))
    
    conversion_factors = {
        "kg": 1,
        "lb": 0.453592,
        "g": 0.001,
        "oz": 0.0283495,
        "ton": 1000,
        "mg": 0.000001
    }

    if unit_from in conversion_factors:
        # Convert weight to kilograms first
        weight_in_kg = weight * conversion_factors[unit_from]
        
        # Convert from kilograms to all units
        converted_weights = {unit: weight_in_kg / factor for unit, factor in conversion_factors.items()}
        
        print(f"The weight in all units:")
        for unit, converted_weight in converted_weights.items():
            print(f"{round(converted_weight, 6)} {unit}")
    else:
        print("Invalid unit")

Weightconvertor()

    
print('''Are you here for
               1. Weight Converter
               2. Temperature Converter
               ''')
Sel = input("Please Select one of them = ")
if Sel == '1':
    Weightconvertor()  # Ensure this function is defined elsewhere in your code
elif Sel == '2':
    tempConvertor()  # Ensure this function is defined elsewhere in your code
else:
    print("Invalid selection")



    
