import random

class Solve:
  def __init__(self, words, verbose=False):
    self.verbose = verbose
    self.words = words

  def solve(self, soln):
    if self.verbose:
      print('solve:', soln)
    path = []
    candidates = self.words
    while True:
      guess = random.choice(candidates)
      path.append(guess)
      if guess == soln:
        break
      # no match, filter candidates
      results = check(guess, soln)
      if self.verbose:
        print('guess:', guess, results)
      candidates = [w for w in candidates if word_ok(guess, w, results)]
    # return the solution path
    if self.verbose:
      print('path:', ' '.join(path))
    return path

def word_ok(w0, w, results):
  for c0, c, r in zip(w0, w, results):
    if r == 'B' and c0 in w:
      return False
    if r == 'G' and c0 != c:
      return False
    if r == 'Y' and c0 == c:
      return False
    if r == 'Y' and c0 not in w:
      return False
  return True

def check(guess, soln):
  results = ['B'] * len(guess)
  for i, c in enumerate(guess):
    if c == soln[i]:
      results[i] = 'G'
    elif c in soln:
      results[i] = 'Y'
  return ''.join(results)
