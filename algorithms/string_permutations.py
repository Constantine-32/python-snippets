#!/usr/bin/env python


def permutations(string, step = 0):
  if step == len(string):
    print(''.join(string))

  for i in range(step, len(string)):
    array = [c for c in string]
    array[step], array[i] = array[i], array[step]
    permutations(array, step + 1)


def main():
  permutations('abcd')


if __name__ == '__main__':
  main()
