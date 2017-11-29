"""
>>> Rebels(40).die()
[13, 28]
"""


class RebelsIterator:
    def __init__(self, rebels):
        self.start = rebels.max().right
        self.curr = self.start
        self.repeated = False

    def __next__(self):
        if self.curr == self.start:
            if self.repeated:
                raise StopIteration
            else:
                self.repeated = True
        curr = self.curr
        self.curr = curr.right
        return curr


class Rebels:
    def __iter__(self):
        return RebelsIterator(self)

    def __init__(self, count):
        """
        >>> Rebels(1)
        [1]
        >>> Rebels(2)
        [1, 2]
        >>> Rebels(3)
        [1, 2, 3]
        >>> Rebels(4)
        [1, 2, 3, 4]
        >>> Rebels(5)
        [1, 2, 3, 4, 5]
        """
        self.start = Soldier(1, None, None)
        self.start.left = self.start
        self.start.right = self.start
        while 1 < count:
            self.add()
            count -= 1

    def max(self):
        """
        >>> rebels = Rebels(4)
        >>> rebels.start = rebels.start.left
        >>> rebels.max()
        3\\4/1
        """
        start = self.start
        while start.num < start.right.num:
            start = start.right
        return start

    def add(self):
        start = self.max()
        right = Soldier(start.num + 1, start, start.right)
        start.right = right
        right.right.left = right

    def die(self):
        """
        >>> Rebels(1).die()
        [1]
        >>> Rebels(2).die()
        [1, 2]
        >>> Rebels(3).die()
        [1, 2]
        >>> Rebels(4).die()
        [1, 4]
        >>> Rebels(5).die()
        [2, 4]
        """
        while True:
            victim = self.start.right.right
            if victim == self.start:
                return self
            self.start = victim.right
            victim.die()

    def __repr__(self):
        """
        >>> x = Rebels(4)
        >>> x.start = x.start.left
        >>> x
        [1, 2, 3, 4]
        """
        return str(list(map(lambda s: s.num, self)))


class Soldier:
    def __init__(self, num, left, right):
        """
        >>> solo = Soldier(0, None, None)
        >>> solo.num
        0
        """
        self.num = num
        self.left = left
        self.right = right

    def die(self):
        """
        >>> left = Soldier(1, None, None)
        >>> center = Soldier(2, None, None)
        >>> right = Soldier(3, None, None)
        >>> left.left = right
        >>> left.right = center
        >>> center.left = left
        >>> center.right = right
        >>> right.left = center
        >>> right.right = left
        >>> left
        3\\1/2
        >>> center
        1\\2/3
        >>> right
        2\\3/1
        >>> center.die()
        >>> left
        3\\1/3
        >>> right
        1\\3/1
        """
        self.left.right = self.right
        self.right.left = self.left
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}\\{}/{}".format(
            self.left.num, self.num, self.right.num)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
