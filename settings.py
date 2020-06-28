#

class Settings():
    def __init__(self):
        # screen config
        self.screen_width = 980
        self.screen_heigt = 600
        self.bg_collor = (230, 230, 230)

        # ship config
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet config
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien config
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10

        # fleet_direction = 1 set move right; -1 set move left
        self.fleet_direction = 1
