class A:
    def method(self):
        print("this method belongs to class A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d =D()
d.method()