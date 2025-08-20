unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Unlock_info:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

    @property 
    def seconds(self):
        return self._seconds


    @seconds.setter
    def seconds(self, value):
        if( value < 1 or value > 60):
             raise ValueError("Valid Range : 1 <= seconds <= 60")
        self._seconds = value


unlock_info = Unlock_info(unlock_code, wire_color, seconds)
print("code :",unlock_code)
print("color :",wire_color)
print("second :",seconds)