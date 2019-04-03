import fire


class BrokenCalculator(object):

    def __init__(self, offset: int = 3000):
        self._offset = offset

    def add(self, x: int, y: int) -> str:
        z = len(x)
        return x + y + self._offset

    def multiply(self, x, y):
        return x * y + self._offset


if __name__ == '__main__':
    # Usage:
    # python broken_calc_obj.py add 9 9 --offset=0
    fire.Fire(BrokenCalculator)
