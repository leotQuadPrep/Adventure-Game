class DisplayRelocator:
    def __init__(self, dis1, dis2, input1):
        self.dis1 = dis1
        self.dis1_st_y = self.dis1.y
        self.dis2 = dis2
        self.dis2_st_y = self.dis2.y
        self.input1 = input1
        self.input1_st_y = self.input1.y

    def relocate(self):
        self.dis2.y = self.dis1.y + self.dis1.h + 10
        self.input1.y = self.dis1.y + self.dis1.h + self.dis2.y + self.dis2.h + 20
