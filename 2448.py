

def recursive(n):
    if n == 3:
        return ["  *  "," * * ","*****"]
    n = n//2
    a = recursive(n)
    top = [" " * ((len(a[0])+1)//2) + i + " " * ((len(a[0])+1)//2) for i in a]
    bottom = [i + " " + i for i in a]
    return top+bottom

for i in recursive(int(input())):
    print(i)