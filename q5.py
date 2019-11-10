n=1
def fun(no):
    global n
    if(no!=0):
        n*=no
        fun(no-1)
    return n

def main():
    print(" Enter a Number")
    m=fun(int(input(" Input :")));
    print("Output=",n)
    print("Output=",m)
if __name__=="__main__":
    main()

