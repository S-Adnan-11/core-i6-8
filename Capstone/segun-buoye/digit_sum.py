def digitsum(n):
    n = abs(n)
    if n < 10:
        return n
    return (n%10)+digitsum(n//10)

def digital_root(n):
    n = abs(n)
    if n < 10:
        return n
    return digital_root((n%10)+digital_root(n//10))

print(digital_root(942))

num = int(input("Number: "))
print(digitsum(num))