secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Secret_appointment:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time 

Secret_appointment1 = Secret_appointment(secret_code, meeting_point, time)
print("secret code :",Secret_appointment1.secret_code)
print("meeting point :",Secret_appointment1.meeting_point)
print("time :",Secret_appointment1.time)