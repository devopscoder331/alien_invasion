#

class Settings():
    def __init__(self):
        ''' initialize the game's static settings '''
        # screen config
        self.screen_width = 980
        self.screen_heigt = 600
        self.bg_color = (230, 230, 230)

        # ship config
        self.ship_limit = 30

        # bullet config
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien config
        self.fleet_drop_speed = 10

        # game speed up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        # fleet_direction = 1 set move right; -1 set move left
        self.fleet_direction = 1
        # point for aliens
        self.alien_points = 50

    def increase_speed(self):
        ''' increase speed settings '''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
