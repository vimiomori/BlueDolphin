from typing import Optional
import os

class BlueDolphin(object):
    def __init__(self, blue: str, dolphin: str):
        self.blue = blue,
        self.dolphin = dolphin
    
    @staticmethod
    def blue_dolphin(r):
        added_nums = []
        for i in range(r):
            added_nums.append((lambda x: x + 1)(i))
        if not added_nums:
            return False
        return True

    def blue_dolphins(self, times):
        print((self.blue + self.dolphin) * times)


if __name__ == "__main__":
    blue_dolphin = BlueDolphin("blue", "dolphin")
    blue_dolphin.blue_dolphin(21)
    blue_dolphin.blue_dolphins(21)
