import fire

def add(x, y):
  return x + y

def multiply(x, y):
  return x * y

def dont_include_this_func(x,y):
  pass

if __name__ == '__main__':
  # Usage:
  # python calculator_fun.py dont_include_this_func 9 9 
  # python calculator_fun.py add 9 9 
  fire.Fire({
      'add': add,
      'multiply': multiply,
  })