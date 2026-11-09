ile = 0
s = 0
def przeniesienia(a, b):
    global ile
    global s
    m = a%10
    n = b%10
    if m+n+s >= 10:
        ile += 1
        s = 1
    else:
        s = 0
    if(a//10 == 0):
        print(ile)
        return
    przeniesienia(a//10, b//10)

przeniesienia(99999,11111)
