num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

operation = input("enter a operation(+, -, x, /)")

if operation == "+":
  result = num1 + num2
  print(result)
elif operation == "-":
  result = num1 - num2
  print(result)
elif operation == "x":
  result = num1 * num2
  print(result)
elif operation == "/":
  result = num1 / num2
  print(result)
else:
    print("You entered incorrectly")

input("Press enter to exit...")
