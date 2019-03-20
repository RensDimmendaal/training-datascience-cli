import fire

class Calculator(object):

  def add(self, x, y):
    return x + y

  def multiply(self, x, y):
    return x * y

if __name__ == '__main__':
  # python calculator_obj add 9 9 
  calculator = Calculator()
  fire.Fire(calculator)