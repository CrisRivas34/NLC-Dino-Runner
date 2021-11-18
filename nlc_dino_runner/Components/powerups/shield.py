from nlc_dino_runner.Components.powerups.powerup import Powerup
from nlc_dino_runner.utils.constants import SHIELD

class Shield(Powerup):
    def __init__(self):
        self.image = SHIELD
        self.type = "shield"
        super().__init__(self.image, self.type)
