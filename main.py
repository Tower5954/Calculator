from art import logo

def add(n1,n2):
  """Adds n1 and n2 together"""
  return n1 + n2

def subtract (n1, n2):
  """Subtracts n1 from n2"""
  return n1 - n2

def multiply (n1, n2):
  """Yes we multiply"""
  return n1 * n2

def divide (n1, n2):
  """Divides n1 from n2"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}  

def calculator():
  print(logo)
  num1 = float(input("What is your first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbols = input("Pick an operation: ")
    num2 = float(input("What is your next number?: "))
    calculation_function = operations[operation_symbols]
    answer =  calculation_function(num1, num2)
    print(f"{num1} {operation_symbols} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue == False
      calculator()
calculator()