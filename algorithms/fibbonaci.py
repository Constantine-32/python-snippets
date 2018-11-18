# Fibbonacci
def fibo(n):
  a = [1, 1]
  if n == 0 or n == 1:
    return n
  for _ in range(n-1):
    a.append(sum(a[-2:]))
  return a[-1]


# Tribonacci
def tribo(n):
  a = [0, 1, 1]
  if n > 2:
    for _ in range(n - 2):
      a.append(sum(a[-3:]))
  return a[-1]


# Tetrabonacci
def tetrabo(n):
  a = [0, 0, 1, 1]
  if n > 3:
    for _ in range(n - 3):
      a.append(sum(a[-4:]))
  return a[-1]


# Some counting problem solution I don't remeber
def count(n):
  return 2 ** n - tribo(n + 2)