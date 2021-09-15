formula = input()
formula = formula.strip()
length = len(formula) - 1


def check(index):
    if formula == "" or not formula[0].isdigit() or not formula[length].isdigit():
        return False
    elif formula[index] in "+-" and formula[index+1] in "+-":
        return False
    elif not formula[index].isdigit() and formula[index] not in "+-":
        return False
    if index == length:
        return True
    return check(index+1)


if check(0):
    print("True,", eval(formula))
else:
    print("False, None")
