# cook your dish here
cases = int(input())
for c in range(cases):
    a, b, c = map(int, input().split())
    avg = (a+b)/2
    if(avg > c):
        print("yes")
    else:
        print("no")
