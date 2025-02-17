def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print(f"call {oncall.calls} to {func.__name__}")
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self, a,b,c): return a + b + c

c = C()
print(c.spam(1, 2, 3))
print(c.spam('a', 'b', 'c'))