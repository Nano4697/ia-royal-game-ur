class Token:

    def __init__(self):
        self.id = id
        self.pos = 0

    def reset_pos(self):
        self.pos = 0

    def move_pos(self, moves):
        if self.pos < 15:
            self.pos = self.pos + moves
