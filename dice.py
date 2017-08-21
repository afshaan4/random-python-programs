import random

k = [1, 2, 3, 4, 5, 6]

r = random.SystemRandom()

def roll():
    print (r.choice(k))

roll()
