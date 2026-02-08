def factorials(num):
    if num == 1:
        return 1
    return num * factorials(num-1)
print(factorials(5))