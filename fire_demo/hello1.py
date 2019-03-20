import fire

def hello(name):
  return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
  # usage: python example.py hello Rens
  fire.Fire()