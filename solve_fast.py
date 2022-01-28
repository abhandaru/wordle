import random
import solve as s

class SolveFast:
  def __init__(self, words, verbose=False):
    self.verbose = verbose
    self.words = words
    self.correct = {}
    for c in 'abcdefghijklmnopqrstuvwxyz':
      self.correct[c] = [[] for i in range(len(words[0]))]
    for w in words:
      for i, c in enumerate(w):
        self.correct[c][i].append(w)

    # Score words
    self.freqs = {}
    for w in words:
      for c in w:
        cc = self.freqs.get(c, 0)
        self.freqs[c] = cc + 1
    self.scores = {}
    for w in words:
      score = sum(self.freqs.get(c, 0) for c in set(w))
      self.scores[w] = score

  def solve(self, soln):
    if self.verbose:
      print('solve:', soln)
    path = []
    candidates = self.words
    while True:
      guess = self.next_guess(candidates)
      path.append(guess)
      if guess == soln:
        break
      # no match, filter candidates
      results = s.check(guess, soln)
      if self.verbose:
        print('guess:', guess, results)
      pass1 = self.filter_pass1(candidates, guess, results)
      candidates = [w for w in pass1 if s.word_ok(guess, w, results)]
    # return the solution path
    if self.verbose:
      print('path:', ' '.join(path))
    return path

  def filter_pass1(self, candidates, w0, results):
    intersect = set(candidates)
    for i, [c0, r] in enumerate(zip(w0, results)):
      if r == 'G':
        intersect = intersect.intersection(self.correct[c0][i])
    return intersect

  def next_guess(self, candidates):
    return random.choice(candidates)
    # scored = [(w, self.scores[w]) for w in candidates]
    # scored = sorted(scored, key = lambda t: t[1])
    # return scored[0][0]
