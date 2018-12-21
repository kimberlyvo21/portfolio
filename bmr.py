# Kimberly Vo
# kv3nw

def st_jeor(m,h,a,s):
    """
    calculates a persons bmr given parameters
    :param m: mass
    :param h: height
    :param a: age
    :param s: sex
    :return: total bmr
    """
    m=float(m)
    h=float(h)
    a=float(a)
    bmr = 10.0*m+6.25*h-5.0*a
    if s == "male":
        bmr = bmr+5
    else:
        bmr = bmr-161
    return bmr
