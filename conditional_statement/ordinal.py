for num in range(1, 41):
    integer = str(num)
    if int(integer) > 3 and int(integer) < 20:
        print(f'{integer}th')
    else:
        if integer[-1] == '1':
            print(f'{integer}st')
        elif integer[-1] == '2':
            print(f'{integer}nd')
        elif integer[-1] == '3':
            print(f'{integer}rd')
        else: 
            print(f'{integer}th')
