#!/usr/bin/env python
import math

def isPrime(n):
  if n <= 1: return False
  if n <= 3: return True
  if n % 2 == 0 or n % 3 == 0: return False
  for i in range(5, int(math.sqrt(n)+1), 6):
    if n % i == 0 or n % (i + 2) == 0: return False
  return True


def nextPrime(n):
  n += 1
  while True:
    if isPrime(n): return n
    n += 1


def factors(n, f=False):
  ps = [2]
  ds = []
  i = 0
  while n not in ps:
    while i < len(ps) and n % ps[i] != 0: i += 1
    if i < len(ps) and n % ps[i] == 0:
      ds.append(ps[i])
      n //= ps[i]
      i = 0
    else: ps.append(nextPrime(ps[-1]))
  ds.append(n)
  dss = list(set(ds))
  dss.sort()
  fs = [[p, ds.count(p)] for p in dss]
  if f: return '[' + ' * '.join(['{}^{}'.format(f[0], f[1]) for f in fs]) + ']'
  else: return fs


def gcd(a, b):
  ad = [f[0] for f in factors(a)]
  bd = [f[0] for f in factors(b)]
  cd = list(set(ad) & set(bd))
  cd.sort()
  return cd[-1]


def lcm(a, b):
  return a // gcd(a, b) * b


def main():
  a = 3**7 * 5**3 * 7**3 * 11**2 * 2357
  b = 2**11 * 3**5 * 5**9 * 11 * 2357

  lcmab = lcm(a, b)
  print(a, b, lcmab, lcmab / a, lcmab / b)


if __name__ == '__main__':
  main()
