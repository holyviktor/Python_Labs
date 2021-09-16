import sys
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

if not sys.argv[1].isdigit() or not sys.argv[3].isdigit() or sys.argv[2] not in "+-*/" or len(sys.argv) > 4:
    print("Wrong data!")
else:
    try:
        print(ops[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3])))
    except:
        print("Division by zero!")
