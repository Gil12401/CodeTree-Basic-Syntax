N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

# 1st infected_dev 
# 0 : negative / 1 : positive 
infected_devs = [1 if i == P-1 else 0 for i in range(N)]
infection_chances = [K if i == P-1 else 0 for i in range(N)]

handshakes = sorted(handshakes, key=lambda x: x[0])

for handshake in handshakes:
    idx_a, idx_b = int(handshake[1]) - 1, int(handshake[2]) - 1
    dev_a, dev_b = infected_devs[idx_a], infected_devs[idx_b]

    # Case 1 ) positive & negative or negative & positive 
    #dev_a : negative / dev_b : positive
    if(dev_a != dev_b and dev_a < dev_b and infection_chances[idx_b] > 0):
        infected_devs[idx_a] = 1
        infection_chances[idx_a] = K
        infection_chances[idx_b] = max(0, infection_chances[idx_b] - 1)
        
    #dev_a : positive / dev_b : negative
    elif(dev_a != dev_b and dev_a > dev_b and infection_chances[idx_a] > 0):
        infected_devs[idx_b] = 1
        infection_chances[idx_b] = K
        infection_chances[idx_a] = max(0, infection_chances[idx_a] - 1)
        
    # Case 2 ) positive & positive
    if (dev_a == 1 and dev_b == 1):
        infection_chances[idx_a] = max(0, infection_chances[idx_a] - 1)
        infection_chances[idx_b] = max(0, infection_chances[idx_b] - 1)
        
        
    
for dev in infected_devs:
    print(dev,end="")