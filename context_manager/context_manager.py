import json, time
from contextlib import contextmanager


def readDB(path):
  with open(path, 'r') as file:
    return json.load(file)


def writeDB(path, db):
  with open(path, 'w') as file:
    json.dump(db, file, indent=2)


@contextmanager
def contextDB(path):
  db = readDB(path)
  try:
    yield db
  finally:
    writeDB(path, db)


def main():
  with contextDB('database.json') as db:
    print(db)
    db[1]['hp'] = 333
    time.sleep(4)
    print(db)


if __name__ == '__main__':
  main()
