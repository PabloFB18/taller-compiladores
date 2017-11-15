class Visitor(object):
    def __init__(self):
        self.expression_string = ''


    # ejemplos internet
    def visit_operation(self, operation):
        operation.arg1.accept(self)
        self.expression_string += ' ' + operation.op + ' '
        operation.arg2.accept(self)

    def visit_integer(self, number):
        self.expression_string += number.num

    def visit_float(self, number):
        self.expression_string += number.num
