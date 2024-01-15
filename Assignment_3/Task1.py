def print_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            if j <= i:
                print('*', end='')
            else:
                print(' ', end='')

        for j in range(columns):
            if j <= (rows - 1 - i):
                print('*', end='')
            else:
                print(' ', end='')

        for j in range(columns):
            if j >= i:
                print('*', end='')
            else:
                print(' ', end='')

        for j in range(columns):
            if j >= (rows - 1 - i):
                print('*', end='')
            else:
                print(' ', end='')

        print()

rows = 10
columns = 10

print_pattern(rows, columns)