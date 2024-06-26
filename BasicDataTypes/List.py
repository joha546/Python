N=int(input())
ls=[]

for i in range(N):
    command, *key= input().split()
    item=list(map(int,key))

    if command=='insert':
        ls.insert(item[0],item[1])
    elif command=='print':
        print(ls)
    elif command=='remove':
        ls.remove(item[0])
    elif command=='append':
        ls.append(item[0])
    elif command=='sort':
        ls.sort()
    elif command=='pop':
        ls.pop()
    elif command=='reverse':
        ls.reverse()