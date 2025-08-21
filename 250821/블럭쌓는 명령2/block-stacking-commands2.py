n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
block_stacks=[0 for _ in range(n)]

def stack_up_blocks(command):
    start, end = command
    for i in range(start-1,end):
        block_stacks[i] += 1 

for i in range(k):
    stack_up_blocks(commands[i])

sorted_block_stacks = sorted(block_stacks)
print(sorted_block_stacks[-1])


