from itertools import product


def sigmaStar(sigma, length):
  sigmaS = [''.join(w) for i in range(length+1) for w in product(sigma, repeat=i)]
  sigmaS[0] = 'lambda'
  return sigmaS


def pregunta11():
  # Lenguaje sobre el alfabeto Sigma = {a,b}.
  sigmaS = sigmaStar('ab', 6)
  # L1 el lenguaje de las palabras que tienen menos de tres a's.
  L1 = [w for w in sigmaS if w.count('a') < 3]
  # L2 el lenguaje de las palabras que tienen menos de dos b's.
  L2 = [w for w in sigmaS if w.count('b') > 2]
  # L3 = L1 \ L2
  L3 = [w for w in sigmaS if w in L1 and w not in L2]
  # Las primeras siete palabras en orden cuasi-lexicografico de L3
  return L3[:10]


def pregunta20():
  # Lenguaje sobre el alfabeto Sigma = {a,b}.
  sigmaS = sigmaStar('ab', 6)
  # L1 el lenguaje de las palabras que tienen menos de tres a's.
  L1 = [w for w in sigmaS if w.count('a') < 3]
  # L2 el lenguaje de las palabras que tienen menos de dos b's.
  L2 = [w for w in sigmaS if w.count('b') > 2]
  # L3 = L1 interjeccion L2
  L3 = [w for w in sigmaS if w in L1 and w in L2]
  # Las primeras siete palabras en orden cuasi-lexicografico de L3
  return L3[:7]


def main():
  print('Pregunta 11: ' + ', '.join(pregunta11()))
  print('Pregunta 20: ' + ', '.join(pregunta20()))


if __name__ == '__main__':
  main()
