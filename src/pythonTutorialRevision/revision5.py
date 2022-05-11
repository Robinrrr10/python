from sample1 import hi
from pack.sample2 import pk
from sample2 import Goat
from sample3 import Dog as dg
import time
hi()
pk()

g1 = Goat()
g1.sound()

d1 = dg()
d1.bite()

def val(**kwargs):
    print(kwargs)

val(name = "Ram", age =67, salary = 78.9)

class NB:
    def jj(self):
        print("Hiiii")
    class OL:
        def oil(self):
            print("ooool")

ol = NB()
ol.jj()

bn = NB.OL()
bn.oil()

print(__name__)

print(time.time())

print("Waiting for 2 sec using below...")
time.sleep(2)

def verify(a, b):
    if a >= b:
        pass
    else:
        print("B is greater")

verify(12, 8)
verify(8, 12)

def check(a, b):
    try:
        result = a / b
    except ValueError as e:
        print("Value error:", e)
    except ZeroDivisionError as z:
        print("Any number cannot be divide by 0")
    except Exception as e:
        print("Something went wrong")
    finally:
        print("ddd")



check(9, 0)
check("33", 8.1)


