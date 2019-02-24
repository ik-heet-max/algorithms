START = 32
END = 127
j = 0
for i in range(START, END + 1):
    if j % 10 == 0 and j != 0:
        print('\n', '{:>5}'.format(i), '{:>1}'.format(chr(i)), end=' ')
    else:
        print('{:>6}'.format(i), '{:>2}'.format(chr(i)), end='')
    j += 1