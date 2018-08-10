if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))
    l=[i for i in arr]
    m=max(l)
    l2=[a for a in l if a < m]
    m=max(l2)
    print(m)
    
