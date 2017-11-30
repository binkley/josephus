"""
>>> Rebels(40).disband()
[13, 28]
"""


class Soldier:
    @staticmethod
    def one():
        """
        >>> solo = Soldier.one()
        >>> solo.num
        1
        """
        # noinspection PyTypeChecker
        solo = Soldier(1, None, None)
        solo.left = solo
        solo.right = solo
        return solo

    def __init__(self, num: int, left: 'Soldier', right: 'Soldier'):
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
        return "{}\\{}/{}".format(self.left.num, self.num, self.right.num)


class Rebels:
    def __init__(self, count: int):
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
        range(1, count)
        for _ in range(1, count):
            curr = curr.join()

    def __iter__(self):
        return RebelsIterator(self)

    def __len__(self):
        """
        >>> len(Rebels(1))
        1
        >>> len(Rebels(2))
        2
        >>> len(Rebels(3))
        3
        >>> len(Rebels(4))
        4
        >>> len(Rebels(5))
        5
        """
        head = self.curr
        curr = head.right
        i = 1
        while not curr == head:
            i = i + 1
            curr = curr.right
        return i

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


class RebelsIterator:
    def __init__(self, rebels: Rebels):
        def _max() -> Soldier:
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
