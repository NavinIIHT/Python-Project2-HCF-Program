
def get_hcf(x,y):
    if type(x)==type(1) and type(y)==type(1):
        hcf=0
        if x>y:
            smaller=y
        else:
            smaller=x
        for i in range(1, smaller+1):
            if((x%i==0) and (y%i==0)):
                hcf = i
        return hcf
    else:
        raise ValueError("Input should be integer type for both x and y")



if __name__=="__main__":

    x,y=(int(n) for n in input("Enter the 2 integers").split())
    print("The H.C.F. is", get_hcf(x,y))


