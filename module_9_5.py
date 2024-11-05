class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
             raise StepValueError
        self.start, self.stop, self.step, self.pointer = start, stop, step, 0

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        self.pointer += self.step
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StepValueError
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

def control_iterator(object):
    try:
        for i in object:
            print(i, end=' ')
    except StepValueError:
        print('The end')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

control_iterator(iter2)
control_iterator(iter3)
control_iterator(iter4)
control_iterator(iter5)