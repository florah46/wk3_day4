def power(x,n):
    if (n == 1):
        return x
    else:
        return x*power(x,n-1)


if __name__ == "__main__" : 

    print(power(3,2))