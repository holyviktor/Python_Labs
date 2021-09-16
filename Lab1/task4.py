weights = input('Enter weights: ').split()
capacity = int(input('Enter capacity of bag: '))


def getValues():
    value = [int(item) for item in weights]
    return value


def createMatrix(capacity):
      value = getValues()
      length = len(value)
      matrix = [[0 for a in range(capacity+1)] for i in range(length+1)]
      for rows in range(length+1):
            for cols in range(capacity+1):
                  if not rows or not cols:
                        matrix[rows][cols] = 0
                  elif value[rows-1] <= cols:
                        matrix[rows][cols] = max(value[rows-1] + matrix[rows-1][cols-value[rows-1]], matrix[rows-1][cols])
                  else:
                        matrix[rows][cols] = matrix[rows-1][cols]
      return matrix, value


def getRes(func, capacity):
      matrix, area = func(capacity)
      length = len(area)
      res = matrix[length][capacity]
      return res


result = getRes(createMatrix, capacity)
print('Maximum weight of gold:', result)
