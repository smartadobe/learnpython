from decimal import Decimal
from functools import singledispatch
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

@fun.register(complex)
def _(arg, verbose=False):
    if verbose:
        print("Better than complicated.", end=" ")
    print(arg.real, arg.imag)


def nothing(arg, verbose=False):
    print("Nothing.{}" .format(arg))

fun.register(tuple, nothing)

@fun.register(float)
@fun.register(Decimal)
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number:", end=" ")
    print(arg / 2)

# fun("Hello, world.")
# fun("test.", verbose=True)
# fun(42, verbose=True)
# fun([1,2,3],verbose=True)
# fun(5+2j,True)

fun((1,2))
fun(1.2 , True)
