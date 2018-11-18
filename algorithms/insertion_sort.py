#!/usr/bin/env python
from math import ceil
from random import randint


def insertion(a):
  for i in range(1, len(a)):
    j = i-1
    num = a[i]
    while j >= 0 and a[j] > num:
      a[j+1] = a[j]
      j -= 1
    a[j+1] = num


def main():
  random_list = [randint(100, 999) for _ in range(200)]
  print('# Randomly Generated List')
  for i in range(ceil(len(random_list) // 20)):
    print(random_list[20*i:20*(i+1)])
  insertion(random_list)
  print('# Sorted List')
  for i in range(ceil(len(random_list) // 20)):
    print(random_list[20*i:20*(i+1)])


if __name__ == '__main__':
  main()
