
class AbstractVariable:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        if not isinstance(other, AbstractVariable):
            return False

        return self.name == other.name and self.__class__ == other.__class__


class ModelVariable(AbstractVariable):
    pass


class SlackVariable(AbstractVariable):
    pass


class ArtificialVariable(AbstractVariable):
    pass
