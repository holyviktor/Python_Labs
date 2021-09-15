weights = input('Enter weights: ').split()
capacity = int(input('Enter capacity of bag: '))
stuffdict = {}


def getValues():
    value = [int(item) for item in weights]
    return value


def createMatrix(stuffdict, capacity):
      value = getValues()
      length = len(value)
      matrix = [[0 for a in range(capacity+1)] for i in range(length+1)]
      for rows in range(length+1):
            for cols in range(capacity+1):
                  if rows == 0 or cols == 0:
                        matrix[rows][cols] = 0
                  elif value[rows-1] <= cols:
                        matrix[rows][cols] = max(value[rows-1] + matrix[rows-1][cols-value[rows-1]], matrix[rows-1][cols])
                  else:
                        matrix[rows][cols] = matrix[rows-1][cols]
      return matrix, value


def getRes(stuffdict, func, capacity):
      matrix, area = func(stuffdict, capacity)
      length = len(area)
      res = matrix[length][capacity]
      return res


result = getRes(stuffdict, createMatrix, capacity)
print('Maximum weight of gold:', result)
