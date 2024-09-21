data = int(input())
def patterns(pattern):
    for i in range(pattern):
        for j in range(pattern):
            print('* ', end = ' ')
        print('\n')
        
patterns(data)