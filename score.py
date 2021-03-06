import random
class Score:
    """this class manage the score of the player and controls the attemps of the player"""
    #constants
    _MAXIMUN_SCORE = 999
    _MINIMUN_SCORE = 0
    _ATTEMPS = 0
    _MINIMUN_ATTEMPS = 0
    _MAXIMUN_ATTEMPS = 9    
    _SCORE_ART = '🏆'
    _ATTEMPS_ART = '💥'

    def __init__(self) -> None:
        self.score = 0
        self.attemps = self._ATTEMPS
        self.score_art = self._SCORE_ART
        self.attemps_art = self._ATTEMPS_ART

    def increase_score(self):
        """this function increase the score by 1 to a maximum of 999"""
        ramdom_points = random.randrange(10,50)
        self.score += ramdom_points
        if self.score > self._MAXIMUN_SCORE:
            self.score = self._MAXIMUN_SCORE
    
    def decrease_score(self):
        """this function decrease the score by 1 to a minimum of 0"""
        self.score -= 1
        if self.score < self._MINIMUN_SCORE:
            self.score = self._MINIMUN_SCORE
    
    def decrease_attemps(self):
        """this function decrease the attemps by 1 to a minimum of 0"""
        self.attemps -= 1
        if self.attemps < self._MINIMUN_ATTEMPS:
            self.attemps = self._MINIMUN_ATTEMPS
    
    def increase_attemps(self):
        """this function increase the attemps by 1 to a maximum of 9"""
        self.attemps += 1
        if self.attemps > self._MAXIMUN_ATTEMPS:
            self.attemps = self._MAXIMUN_ATTEMPS   
    
    def get_score(self):
        """this function return the score of the player"""
        return self.score
    
    def get_attemps(self):
        """this function return the attemps of the player"""
        return self.attemps
    
    def set_attemps(self,attemps):
        """this function set the attemps of the player"""
        self.attemps = attemps
        
    def get_maximun_attemps(self):
        """this function return the maximun attemps of the player"""
        return self._MAXIMUN_ATTEMPS

    def get_score_art(self):
        """this function return the score art of the player"""
        return self.score_art
    
    def get_attemps_art(self):
        """this function return the attemps art of the player"""
        return self.attemps_art
    