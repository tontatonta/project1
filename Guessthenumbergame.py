#Guess the number game
import sys
import random
sys.stdout.buffer.write(b'select the minimum number\n')
sys.stdout.flush()
n = int(sys.stdin.buffer.readline())
sys.stdout.buffer.write(b'select the maximum number\n')
sys.stdout.flush()
m = int(sys.stdin.buffer.readline())
ans = random.randint(n,m)
count = 1
player = ans - 1
while True:
    if player == ans:
        break
    player = int(sys.stdin.buffer.readline())
    count  += 1
print(f'Answer is {ans} count {count}')
