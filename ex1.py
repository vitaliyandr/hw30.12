try:
    x = int(input("Type x: "))
    y = int(input("Type y: "))

    result = x ** y

    print(f"{x} ** {y} = {result}")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
