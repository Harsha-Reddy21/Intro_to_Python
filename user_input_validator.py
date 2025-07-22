def input_validator():
    while True:
        user_input=input("Enter your age: ")
        if not user_input.strip():
            print("Invalid input. Please enter a valid number.")
            continue

        try:
            value=int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if value<1 or value>120:
            print("Out of range. Please enter a number between 1 and 120.")
            continue

        print(f'You entered a valid age: {value}')
        break

    


if __name__=="__main__":
    input_validator()