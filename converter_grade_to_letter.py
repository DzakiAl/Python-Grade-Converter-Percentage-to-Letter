def grade_program():
    grade = int(input("Please enter your grade (in percentage): "))

    if grade >= 90:
        print("Your grade is A")
    elif grade >= 80:
        print("Your grade is B")
    elif grade >= 70:
        print("Your grade is C")
    elif grade >= 60:
        print("Your grade is D")
    else:
        print("Your grade is F")
    return

print("Wellcome to Python Grade Converter Percentage to Letter")
print("=======================================================")
print("")
print("1. Enter")
print("2. Exit")

while True:
    try:
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            grade_program()
        elif choice == 2:
            print("Exiting..................")
            break
        else:
            print("Invalid input, try again!")
    except ValueError:
        print("Invalid input, try again!")