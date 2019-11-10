n=0
def fun(no):
    global n
    if(no!=0):
        k=no%10
        n+=k
        fun(int(no/10))
    return n

def main():
    print(" Enter a Number")
    m=fun(int(input(" Input :")));
    print(n)
    print(m)
if __name__=="__main__":
    main()


