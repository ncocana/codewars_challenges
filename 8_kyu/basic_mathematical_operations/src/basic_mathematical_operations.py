import operator

def basic_op(operator1, value1, value2):
    
    
    ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

    return ops[operator1](value1,value2)