import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
lotto.sort()
print(lotto)