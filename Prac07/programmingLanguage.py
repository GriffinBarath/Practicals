class ProgrammingLanguage:
    """represents a programming language object"""

    def __init__(self, name="", typing="", reflection=bool, year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return"{}, {} Typing, Reflection={}, First appeared in {}.".format(self.name, self.typing, self.reflection, self.year)

    def isDynamic(self, typing):
        if typing == "Dynamic":
            return True




