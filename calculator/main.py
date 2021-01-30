import art


def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": multiply,
  "/": divide
}
def calculator():
  print(art.logo)
  should_continue = True
  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)

  while should_continue:
    op_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    #calculo de inputs
    answer = operations[op_symbol](num1, num2)

    #resultado operacion
    print(f"{num1} {op_symbol} {num2} = {answer}")
      
    #continuar?
    ask_user = input(f"Type 'y' to keep calculating with {answer}, or type 'n' to start from zero: ")
    if ask_user == 'y':
      should_continue = True
      num1 = answer
    else:
      should_continue = False
      calculator()
      







  
  






