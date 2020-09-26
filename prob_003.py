# Determining whether the number is prime or not
def primeq(n):
    if n==1 or n==0:
        return False
    elif n==2 or n==3 or n==5 or n==7:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3, n//2, 2):
            if n%i==0:
                return False
        return True

# Factorization fucntion
def factor(n):
    if primeq(n)==True:
        return [n]
    else:
        ans = []
        integer = 2
        while n!=1:
            if primeq(integer)==True and n%integer==0:
                while n%integer==0:
                    n //= integer
                ans.append(integer)
            integer +=1
        return ans

print(factor(600851475143)[-1])
#output: 6857
