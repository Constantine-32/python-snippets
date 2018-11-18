import time


def timing(str):
  def decorate(func):
    def call(*arg, **kw):
      ts = time.time()
      res = func(*arg, **kw)
      te = time.time()
      print(str.format(te - ts))
      return res
    return call
  return decorate


@timing('Time elapsed {:.2f}s')
def heavy():
  for i in range(100000000):
    pass


heavy()