class Life:
    """this class manage the lifes info of the player
    """
    #constants
    _MAXIMUN_LIVES = 3
    _MINIMUN_LIFES = 0

    def __init__(self) -> None:
        self.life_art = '❤️'
        self.total_lifes = self._MAXIMUN_LIVES

    def set_lifes(self,amount:int):
        """this function set a value to total live
           and this can't be less than 0 or more than 3

        Args:
            amount (int): amount of lifes
        """
        self.total_lifes = amount
        if self.total_lifes > self._MAXIMUN_LIVES:
            self.total_lifes = self._MAXIMUN_LIVES
        if self.total_lifes < 0 :
            self.total_lifes = self._MINIMUN_LIFES

    def get_lifes(self):
        """this function return the total lives of the player"""
        return self.total_lifes

    def get_life_art(self):
        """this function return the life art of the player"""
        return self.life_art

    def loose_life(self):
        """this function rest 1 life to the player
        """
        self.total_lifes -= 1
        if self.total_lifes < 0 :
            self.total_lifes = self._MINIMUN_LIFES
    
    def give_live(self):
        """this function add 1 life to the player"""

        self.total_lifes += 1
        if self.total_lifes > self._MAXIMUN_LIVES:
           self.total_lifes = self._MAXIMUN_LIVES
