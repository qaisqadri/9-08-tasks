
N = int(input())

if N % 2 != 0:
    print("Weird")
else:
    if(N>=2 and N<=5):
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")
    elif N > 20:
        print("Not Weird")
