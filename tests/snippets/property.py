from testutils import assertRaises


class Fubar:
    def __init__(self):
        self.x = 100

    @property
    def foo(self):
        value = self.x
        self.x += 1
        return value


f = Fubar()
assert f.foo == 100
assert f.foo == 101


null_property = property()
assert type(null_property) is property

p = property(lambda x: x[0])
assert p.__get__((2,), tuple) == 2
# TODO owner parameter is optional
# assert p.__get__((2,)) == 2

with assertRaises(AttributeError):
    null_property.__get__((), tuple)

with assertRaises(TypeError):
    property.__new__(object)


p1 = property("a", "b", "c")

assert p1.fget == "a"
assert p1.fset == "b"
assert p1.fdel == "c"

assert p1.getter(1).fget == 1
assert p1.setter(2).fset == 2
assert p1.deleter(3).fdel == 3

assert p1.getter(None).fget == "a"
assert p1.setter(None).fset == "b"
assert p1.deleter(None).fdel == "c"
