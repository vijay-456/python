print("this is my second python file")

def fun(*ar, **kwar):
    new_ar = ar
    print(new_ar,type(ar))
    new_kwar = kwar
    print(new_kwar,type(kwar))

fun(1,2,a=234,b=456)
