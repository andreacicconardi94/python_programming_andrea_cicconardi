#!/home/andrea/anaconda3/bin/python3
#compute the Fibonacci sequence in an iterative way


import sys

def FibIter(n):
    F=[0,0]
    if n<=2:
        return 1
    else:
        F[0]=1
        F[1]=1
    for i in range(2,n):
        tmp = F[i-1] + F[i-2]
        F.append(tmp)
    return print(F[n-1])



if __name__ == "__main__":
    n=int(sys.argv[1])
    FibIter(n)
