n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Person_info():
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

Person_infos = [Person_info(name[i], street_address[i], region[i]) for i in range(n)]
sorted_Person_info = sorted(Person_infos, key=lambda p: p.name, reverse=True)

print("name",sorted_Person_info[0].name)
print("addr",sorted_Person_info[0].address)
print("city",sorted_Person_info[0].region)
