# musician.py

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class 
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])
     
    # def tune(self):
    #     print("Be with you in a moment")
    #     print("Twoning, sproing,slang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["bum!", "brrum!", "brrrumble!!!!"])
        
    def count(self, length):
        for i in range(length):
            print("{} and...".format(i + 1))
        print("BOOM!!!")
        
nigel = Guitarist()
nigel.solo(6)
print(nigel.sounds)

George = Bassist()
George.solo(14)

Kim = Drummer()
Kim.solo(5)
Kim.count(4)