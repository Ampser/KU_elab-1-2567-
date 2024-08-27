class Radio():
    def __init__(self,mode="FM",frequency=87.5):
        self.mode = mode
        self.frequency = frequency
    def get_mode(self):
        return self.mode
    def get_frequency(self):
        return self.frequency
    def set_mode(self,mode="FM"):
        self.mode = mode
        if mode =="FM":
            self.frequency= 87.5
        else: self.frequency = 150
    def set_frequency(self,frequency):
        if self.mode == "FM" and frequency >= 87.5 and frequency <=108 :
            self.frequency = frequency
        elif self.mode == "AM" and frequency >= 150 and frequency <=280:
            self.frequency = frequency
    def adjust_frequency(self,frequency):
        if self.mode == "FM" and self.frequency+frequency >= 87.5 and self.frequency+frequency <=108 :
            self.frequency += frequency
            return True
        elif self.mode == "AM" and (self.frequency+frequency >= 150 and self.frequency+frequency <=280):
            self.frequency += frequency
            return True
        else: return False
    def __str__(self):
        if (self.mode == "FM") :return f"{self.mode} Radio: {self.frequency:.1f} MHz"
        else :return f"{self.mode} Radio: {self.frequency:.1f} kHz"
