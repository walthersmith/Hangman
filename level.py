class Level:
    _MAXIMUN_LEVEL = 999

    def __init__(self) -> None:
        self.level = 1


    def increase_level(self):
        """this function increase the level by 1 to a maximum of 9"""
        self.level += 1
        if self.level > self._MAXIMUN_LEVEL:
            self.level = self._MAXIMUN_LEVEL

    def get_level(self):
        """this function return the level of the game"""
        return self.level