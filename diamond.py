for i in range(1,6):
    for j in range(5-i, 0, -1):
        print(' ', end=' ')
    for k in range(i):
        print('*', end=' ')
    for m in range(i-1):
        if i != 1:
            print('*', end=' ')
    print()
    
for i in range(1,5):
    for j in range(i):
        print(' ', end=' ')
    for k in range(5-i, 0, -1):
        print('*', end=' ')
    for m in range(4-i):
        print('*', end=' ')
    print()
        
    
