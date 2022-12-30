try:
    count = 0
    for num in range(100, 10000):
        digits = set(str(num))
        if len(digits) == len(str(num)):
            count += 1
    print(count)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
