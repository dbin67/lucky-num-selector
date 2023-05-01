import random
import sys

print(*[sorted(random.sample(range(1, 46), 6)) for _ in range(int(sys.argv[1]))], sep="\n")
