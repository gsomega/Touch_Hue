

class Settings:
    def __init__(self):

        # Card settings
        self.card_width = 100
        self.card_height = 100
        self.base_card_color = 0, 0, 0

        # Board settings
        self.cards_in_width = 6
        self.cards_in_height = 6

        # Board indexes: defaults to the 4 corners
        self.TL = 0
        self.TR = self.cards_in_width-1
        self.BL = (self.cards_in_height-1)*self.cards_in_width
        self.BR = (self.cards_in_height*self.cards_in_width)-1
        self.locked_card_indexes = [self.TL, self.TR, self.BL, self.BR]

        # Screen settings
        self.screen_width = self.cards_in_width*self.card_width
        self.screen_height = self.cards_in_height*self.card_height
        self.bg_color = (255, 255, 255)

        # Gradient settings
        self.TL_color = [255,0,0]
        self.TR_color = [255,255,200]
        self.BL_color = [0,0,255]
        self.BR_color = [40,200,200]