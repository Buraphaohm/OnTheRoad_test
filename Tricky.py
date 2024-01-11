def tricky(a, b):
    base = 1000000
    diff = 1000000
    for _ in range(abs(b)):
        diff -= a
    if (a > 0 and b > 0) or (a < 0 and b < 0):
      return abs(base - diff)
    elif (a>0 and b<0):
      return -(base - diff)
    else:
      return base - diff

def read_input():
    input_numbers = list(map(int, input().split()))
    return input_numbers[0], input_numbers[1]

a, b = read_input()
result = tricky(a, b)
print(result)