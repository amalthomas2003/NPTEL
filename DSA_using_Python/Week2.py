def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeproduct(n):
    if n < 4:
        return False

    for i in range(2, n // 2 + 1):
        if is_prime(i) and n % i == 0:
            factor = n // i
            if is_prime(factor):
                return True

    return False


def delchar(s,c):
    if len(c)>1:
        return s
    newstr=""
    for i in s:
        if i==c:
            continue
        else:
            newstr+=i
    return newstr


def shuffle(l1,l2):
    newlist=[]
    l1len=len(l1)
    l2len=len(l2)
    if l1len>=l2len:
        n=l1len
    else:
        n=l2len
        
    for i in range(n):
        if i>=l1len:
            pass
        else:
            newlist.append(l1[i])
        if i>=l2len:
            pass
        else:
            newlist.append(l2[i])
    return(newlist)

