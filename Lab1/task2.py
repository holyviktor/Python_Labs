import sys
import operator

ops = {
    'add' : operator.add,
    'sub' : operator.sub,
    'mul' : operator.mul,
    'div' : operator.truediv,
}

if not sys.argv[2].isdigit() or not sys.argv[3].isdigit() or sys.argv[1] not in "add sub mul div".split() or len(sys.argv) > 4:
	print("Wrong data!")
else:
	print(ops[sys.argv[1]](int(sys.argv[2]), int(sys.argv[3])))
    	
	