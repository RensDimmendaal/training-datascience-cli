import fire

def hello(name):
  return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
  # python hello2.py rens
  fire.Fire(hello)