class Fibonacci:
    def __init__(self, steps):

        self.steps = steps
        self.current_step = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current_step >= self.steps:
            raise StopIteration

        if self.current_step == 0:
            self.current_step += 1
            return self.a

        self.current_step += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a



steps = 11
fib = Fibonacci(steps)

for number in fib:
    print(number)
