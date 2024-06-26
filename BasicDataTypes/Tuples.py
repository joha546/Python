if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    int_tup=tuple(integer_list)
    r=hash(int_tup)
    print(r)