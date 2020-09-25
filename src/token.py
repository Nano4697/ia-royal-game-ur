class Token:

    def __init__(self, id):
        self.id = id
        self.pos = 0

    def reset_pos(self):
        self.pos = 0

    def move_pos(self, moves):
        if self.pos < 15:
            self.pos = self.pos + moves
            if self.pos > 15:
                self.pos = 15

        return self.pos

    def get_pos(self):
        return self.pos

    def print(self):
        print("\tToken id:", self.id, "pos:", self.pos)
