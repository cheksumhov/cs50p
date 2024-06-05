# Main asks the user twice for input and then passes the entered string into two functions, dollars_to_float, and percent_to_float
# Calculate dollars * percent and store the result in the tip variable
# Format the value and print the result
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Removes the dollar sign with the rstrip function and converts the string to a float
# If no dollar sign is found, output an error
def dollars_to_float(d):
    if "$" in d:
        return float(d.lstrip("$"))
    else:
        print("You didn't enter a dollar sign!")
        exit()

# Removes the percent sign using the rstrip method and converts the string to a float
# If no percent sign is found, output an error
def percent_to_float(p):
    if "%" in p:
        return float(p.rstrip("%")) / 100
    else:
        print("You didn't enter a percent sign!")
        exit()


main()
