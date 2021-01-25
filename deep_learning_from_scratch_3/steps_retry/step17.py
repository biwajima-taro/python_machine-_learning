class obj:
    pass


def f(x):
    print(x)


a = obj()
f(a)
#####################
##############################################################

a = obj()
b = obj()
c = obj()
a.b = b
b.c = c
c.a = a
a = b = c = None
