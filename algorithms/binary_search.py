#!/usr/bin/env python


def binarySearch(list, ele):
  lower = 0
  upper = len(list) - 1

  while lower <= upper:
    pivot = (lower + upper) // 2

    if ele == list[pivot]:
      return True

    if ele < list[pivot]:
      upper = pivot - 1
    else:
      lower = pivot + 1

  return False


def main():
  size = 100
  list = [(i+1)*2 for i in range(size)]

  for i in range(200):
    print(binarySearch(list, i))


if __name__ == '__main__':
  main()
