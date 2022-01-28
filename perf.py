import time
import random

from solve import Solve
from solve_fast import SolveFast

seed = random.randint(0, 100)
cycles = 1000

# get all the words
with open('5-letters.txt') as f:
  lines = f.readlines()
words = [l.strip() for l in lines]

def perf(engine):
  r = random.Random(seed)
  start = time.process_time_ns()
  guesses = 0
  for i in range(cycles):
    w = r.choice(words)
    guesses += len(engine.solve(w))
  timing = time.process_time_ns() - start
  return (timing / 1e9, guesses)

print(perf(Solve(words)))
print(perf(SolveFast(words)))
# print(SolveFast(words, verbose=True).solve('mount'))
