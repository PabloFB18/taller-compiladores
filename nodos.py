

# ejemplos de internet
class Operation(object):
    def __init__(self, op, arg1, arg2):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    def accept(self, visitor):
        visitor.visit_operation(self)


class Integer(object):
    def __init__(self, num):
        self.num = num

    def accept(self, visitor):
        visitor.visit_integer(self)


class Float(object):
    def __init__(self, num):
        self.num = num

    def accept(self, visitor):
        visitor.visit_float(self)


expression = Operation('+', Integer('5'), Operation('*', Integer('2'), Float('444.1')))