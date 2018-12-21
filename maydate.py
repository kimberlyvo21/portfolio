# Kimberly Vo
# kv3nw

def creepy(a,b):
    a= int(a)
    b= int(b)
    if b>a:
        age= int((b/2)+7)
        if age>a:
            return True
        else:
            return False
    else:
        age = int((a/2)+7)
        if age>b:
            return True
        else:
            return False
