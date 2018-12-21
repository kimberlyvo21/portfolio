# Kimberly Vo
# kv3nw

def ellipsis(s):
    elli=('...')
    beg= s[0:2]
    end=s[-2:]
    return (beg+elli+end)
def eighteen(s):
    num= len(s)
    num=num-2
    beg = s[0]
    end = s[-1]
    return beg+str(num)+end
def allit(s,t):
    s.lower()
    t.lower()
    if s[0] == t[0]:
        return True
    else:
        return False
def between(s,t):
    beg = s.find(t)
    end = s.rfind(t)
    strbeg= s[beg]
    strend = s[end]
    if strbeg == strend:
        return s[beg+1:end]
    else:
        return " "
