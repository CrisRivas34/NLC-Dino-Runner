from nlc_dino_runner.Components.powerups.powerup import Powerup
from nlc_dino_runner.utils.constants import PACMAN_POWER_UP

class Pacman(Powerup):
    def __init__(self):
        self.image = PACMAN_POWER_UP
        self.type = "pacman"
        super().__init__(self.image, self.type)