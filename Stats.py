

class Stats:
    def __init__(self, *args, **kwargs):
        self.str  = 0
        self.int  = 0
        self.spt  = 0
        self.end  = 0
        self.hp   = 0
        self.atk  = 0
        self.name = ""

    def attack(recipient):
        recipient.hp -= self.str + self.atk