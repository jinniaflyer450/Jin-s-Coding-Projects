# Function to input strings and convert strings to floating point numbers:
def convert(str1):
    while True:
        str1 = input("Enter a number: ")
        y = 1
        try: 
            x = float(str1)
        except:
            if str1.upper() == "DONE":
                print("Thank you!")
                quit()
            else:
                print("Invalid input; try again.")
                y = 0
        if y == 0:
            continue
        else:
            return x
            break                

# Calculator:
str1 = None
str2 = None

fl1 = convert(str1)
fl2 = convert(str2)

while True:
    o = input("Enter an operator: ")
    if o == '+':
        answer = fl1 + fl2
        break
    elif o == '-':
        answer = fl1 - fl2
        break
    elif o == '*':
        answer = fl1 * fl2
        break
    elif o == '/':
        answer = fl1 / fl2
        break
    elif o.upper() == "DONE":
        print("Thank you!")
        quit()
    else:
        print("Invalid operator; try again.")
        continue

print("The answer is", answer)