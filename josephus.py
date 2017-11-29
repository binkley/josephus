"""
>>> Rebels(40).disband()
[13, 28]
"""


class RebelsIterator:
    def __init__(self, rebels):
        def _max():
            curr = rebels.curr
            while curr.right > curr:
                curr = curr.right
            return curr

        self.first = _max().right
        self.curr = self.first
        self.repeated = False

    def __next__(self):
        if self.curr == self.first:
            if self.repeated:
                raise StopIteration
            else:
                self.repeated = True
        curr = self.curr
        self.curr = curr.right
        return curr


class Rebels:
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
        self.curr = Soldier.one()
        curr = self.curr
        while 1 < count:
            curr = curr.join()
            count -= 1

    def __iter__(self):
        return RebelsIterator(self)

    def disband(self):
        """
        >>> Rebels(1).disband()
        [1]
        >>> Rebels(2).disband()
        [1, 2]
        >>> Rebels(3).disband()
        [1, 2]
        >>> Rebels(4).disband()
        [1, 4]
        >>> Rebels(5).disband()
        [2, 4]
        """
        while True:
            victim = self.curr.right.right
            if victim == self.curr:
                return self
            self.curr = victim.right
            victim.leave()

    def __repr__(self):
        """
        >>> x = Rebels(4)
        >>> x.curr = x.curr.left
        >>> x
        [1, 2, 3, 4]
        """
        return str(list(map(lambda s: s.num, self)))


class Soldier:
    @staticmethod
    def one():
        """
        >>> solo = Soldier.one()
        >>> solo.num
        1
        """
        solo = Soldier(1, None, None)
        solo.left = solo
        solo.right = solo
        return solo

    def __init__(self, num, left, right):
        self.num = num
        self.left = left
        self.right = right

    def join(self):
        center = Soldier(self.num + 1, self, self.right)
        self.right.left = center
        self.right = center
        return center

    def leave(self):
        """
        >>> left = Soldier.one()
        >>> center = left.join()
        >>> right = center.join()
        >>> left
        3\\1/2
        >>> center
        1\\2/3
        >>> right
        2\\3/1
        >>> center.leave()
        >>> left
        3\\1/3
        >>> right
        1\\3/1
        """
        self.left.right = self.right
        self.right.left = self.left
        self.left = None
        self.right = None

    def __gt__(self, other):
        return self.num > other.num

    def __repr__(self):
        return "{}\\{}/{}".format(
            self.left.num, self.num, self.right.num)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
