from .hanoi_exception import HanoiException


class Tower:
    """
    Class for storing and managing Hanoi game towers.
    """

    def __init__(self):
        """
        Initializes the tower.
        """
        self.discs = []

    def is_empty(self):
        """
        Returns if a tower is empty or not, it is, if the tower has no discs.

        :return: True if is empty, it is, if the tower has no discs, False otherwise
        """
        return self.size() == 0

    def size(self):
        """
        Returns the size (number of discs) of the tower.

        :return: The size (number of discs) of the tower.
        """
        return len(self.discs)

    def pop_disc(self):
        """
        Removes a disc from the top of the tower and returns it.
        Raises an HanoiException if the tower is empty.

        :return: The disc removed from the top of the tower.
        """
        if self.is_empty():
            raise HanoiException('The tower is empty!')

        return self.discs.pop()

    def push_disc(self, disc):
        """
        Adds a disc to the top of the tower.
        Raises an HanoiException if the disc is bigger that the disc at the top of the tower.

        :param disc: The disc to be added to the top of the tower.
        """
        if not self.is_empty() and disc > self.discs[-1]:
            raise HanoiException('The disc is bigger than the disc at the top of the tower!')

        self.discs.append(disc)

    def as_list(self):
        """
        Returns the discs of the tower as a new list (it means that if the internal representation of the tower is a
        list, it should return a copy of it).

        :return: A list containing the discs of the tower.
        """
        return self.discs.copy()

    def __repr__(self):
        """
        Returns a string with the internal representation of the tower. This method can be used to represent the tower
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        return '[{}]'.format(', '.join(str(element) for element in self.discs))

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format
        """
        result = []
        for disc in reversed(self.discs):
            half_line = ' ' * (len(self.discs) - disc) + '#' * disc
            result.append(half_line + '|' + half_line[::-1])
        return '\n'.join(result)
