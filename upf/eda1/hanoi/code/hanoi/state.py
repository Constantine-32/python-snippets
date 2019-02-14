from .hanoi_exception import HanoiException


class State:
    """
    Class for storing and managing Hanoi game states.
    """

    DISC_CHAR = '#'
    NON_DISC_CHAR = '.'
    ROD_CHAR = '|'

    def __init__(self, move_id, depth, moved_disc, source, target, towers, n_discs):
        """
        Initializes a state with all the information needed to represent it in the requested format.

        :param move_id: Identifier of the move. Ideally, the step number.
        :param depth: Recursion depth at which this state is generated.
        :param moved_disc: The disc moved to reach this state. Ideally, a disk is defined just by its size.
        :param source: Tower from which the disc is moved.
        :param target: Tower to which the disc is moved.
        :param towers: Towers of the game.
        :param n_discs: Number of discs of the game.
        """
        self.move_id = move_id
        self.depth = depth
        self.moved_disc = moved_disc
        self.source = source
        self.target = target
        # How the towers will be stored? Directly? Is that a good idea?
        self.towers = [tower.as_list() for tower in towers]
        self.n_discs = n_discs

    def get_tower(self, idx):
        """
        Returns the tower corresponding to the idx. Depending on the implementation of the state, this method can be
        invalid. If so, raise an exception and justify it in the report.

        :param idx: Index of the tower.
        :return: The tower corresponding to the idx.
        """
        try:
            return self.towers[idx]
        except IndexError:
            raise HanoiException('The index is out of range.')

    def __repr__(self):
        """
        Returns a string with the internal representation of the state. This method can be used to represent the state
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        return 'move_id: {}, rec_depth: {}, last_move: disk {} from {} to {}, towers: [{}]'\
            .format(self.move_id, self.depth, self.moved_disc, self.source, self.target,
                    ', '.join(repr(tower) for tower in self.towers))

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format
        """
        result = []

        if self.move_id is not None and self.depth is not None:
            result.append('Move id {} Rec Depth {}'.format(self.move_id, self.depth))
            result.append('Last move: {} Disk, from {} to {}'.format(self.moved_disc, self.source+1, self.target+1))

        for index in reversed(range(self.n_discs)):
            line = []
            for tower in self.towers:
                disc_size = tower[index] if (index < len(tower)) else 0
                half_line = self.NON_DISC_CHAR * (self.n_discs - disc_size) + self.DISC_CHAR * disc_size
                line.append(half_line + self.ROD_CHAR + half_line[::-1])
            result.append(' '.join(line) + ' ')

        spacing = ' ' * (self.n_discs - 3)
        tower_string = spacing + 'Tower {}' + spacing
        tower_list = [tower_string.format(n+1) for n in range(len(self.towers))]
        result.append(' '.join(tower_list) + ' ')

        return '\n' + '\n'.join(result) + '\n'
