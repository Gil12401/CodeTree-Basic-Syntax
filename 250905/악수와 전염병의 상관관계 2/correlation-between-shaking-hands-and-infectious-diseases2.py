N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

# 1st infected_dev 
# 0 : negative / 1 : positive 
infected_devs = [1 if i == P-1 else 0 for i in range(N)]
infection_chances = [K if i == P-1 else 0 for i in range(N)]

handshakes = sorted(handshakes, key=lambda x: x[0])

for handshake in handshakes:
    dev_a, dev_b = int(handshake[1]), int(handshake[2])
    
    # 1. dev_a 시점 
    if (infected_devs[dev_a - 1] == 1 and infection_chances[dev_a - 1] > 0):
        infected_devs[dev_b - 1] = 1
        infection_chances[dev_a - 1] = max(0, infection_chances[dev_a - 1] - 1)
    # 2. dev_b 시점 
    if (infected_devs[dev_b - 1] == 1 and infection_chances[dev_b - 1] > 0):
        infected_devs[dev_a - 1] = 1
        infection_chances[dev_b - 1] = max(0, infection_chances[dev_b - 1] - 1)

for dev in infected_devs:
    print(dev,end="")
    
    
    
    
