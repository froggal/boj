banbok = int(input())

for _ in range(banbok) :
    data = []
    data = input().split(' ')
    data[0] = 'god'
    print(str.join('', data))