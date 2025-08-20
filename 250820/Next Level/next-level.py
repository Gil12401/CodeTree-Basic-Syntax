user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User: 
    def __init__(self, u_id="", u_lv=0):
        self.u_id = u_id
        self.u_lv = u_lv

User1 = User("codetree", 10)

User2 = User()
User2.u_id = user2_id
User2.u_lv = user2_level

print("user",User1.u_id,"lv",User1.u_lv)
print("user",User2.u_id,"lv",User2.u_lv)





