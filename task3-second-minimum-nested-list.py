def myf(a):
    return a[1]

def find_secondMax(st):
    st.sort(key=myf)
    mg2=st[1][1]
    out=[s[0] for s in st if s[1]==mg2]
    out.sort()
    for s in out:
        print(s)

def find_secondMax2(st):
    m=st[0]
    for item in st:
        if item[1] < m[1]:
            m = item
    
    out=[s for s in st if s[1]>m[1]]
    m=out[0]
    for item in out:
        if item[1] < m[1]:
            m = item
    fout=[s[0] for s in out if s[1]==m[1]]
    fout.sort()
    for s in fout:
        print(s)

        
        
if __name__ == '__main__':
    student=list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    #find_secondMax(student)
    find_secondMax2(student)
