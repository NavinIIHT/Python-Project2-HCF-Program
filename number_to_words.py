
def number_to_words(N):
    L=[]
    if type(N)!=type(" "):
        if N==0:
            return "ZERO"
        while N!=0:
            r=N%10
            N=N//10
            if r==1:
                L.append("ONE")
            elif r==2:
                L.append("TWO")
            elif r==3:
                L.append("THREE")
            elif r==4:
                L.append("FOUR")
            elif r==5:
                L.append("FIVE")
            elif r==6:
                L.append("SIX")
            elif r==7:
                L.append("SEVEN")
            elif r==8:
                L.append("EIGHT")
            elif r==9:
                L.append("NINE")
            elif r==0:
                L.append("ZERO")

        L.reverse()
        s=' '.join(L)
        return s
    else:
        raise ValueError("Number must be integer type")

if __name__=="__main__":
    N=int(input("Enter the N "))
    words=number_to_words(N)
    print("Given number in words")
    print(words)


