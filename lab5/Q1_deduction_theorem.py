def _and(a, b):
    return a and b


def _or(a, b):
    return a or b


def _implies(a, b):
    return _or(not a, b)


operation_func = {'^': _and, 'V': _or, '=>': _implies}


def evaluate_expression(exp, values):
    idx = 0
    left = ""
    right = ""
    operation = ""
    l = len(exp)

    if l == 1:
        return values[exp[0]]
    elif l == 2:
        return str((int(values[exp[1]]) + 1) % 2)

    while idx < l:
        if exp[idx] == '^' or exp[idx] == 'V' or exp[idx] == '=':
            operation = exp[idx]
            break
        left += exp[idx]
        idx += 1
    idx += 1

    if exp[idx] == '>':
        operation += exp[idx]
        idx += 1
    while idx < l:
        right += exp[idx]
        idx += 1

    if left[0] == '~':
        left_value = values[left[1]]
    else:
        left_value = values[left[0]]

    if right[0] == '~':
        right_value = values[right[1]]
    else:
        right_value = values[right[0]]

    res = operation_func[operation](int(left_value), int(right_value))
    return str(res)


def simplify(query, values):
    stack = []
    for i, c in enumerate(query):
        if c == ")":
            exp = []
            while stack[-1] != "(":
                exp.append(stack.pop())
            stack.append(evaluate_expression(exp[::-1], values))
        else:
            stack.append(c)
    if stack[-1] == "1":
        return True
    return False


def split_and_check_clauses(query, values):
    stack = []
    index = 0

    for i, c in enumerate(query):
        if c == ")":
            stack.pop()
            if len(stack) == 0:
                index = i
                break
        elif c == "(":
            stack.append(c)

    if "=>" in query:
        left = query[:i + 1]
        right = query[i + 3:]
        if simplify(left, values):
            if not simplify(right, values):
                return "Not a Theorem"


if __name__ == "__main__":
    flag = False
    query = str(input("Enter an expression to parse: "))
    variable = set([x for x in query if x not in ['=', '>', '~', ')', '(', '^', 'V']])
    print("Parsing...")
    print("Evaluating...")
    for i in range(2 ** len(variable)):
        values = {'0': '0', '1': '1'}
        temp = format(i, '0' + str(len(variable)) + 'b')
        for i, c in enumerate(variable):
            values[c] = temp[i]
        if split_and_check_clauses(query, values) == "Not a Theorem":
            flag = True
    if flag:
        print("The expression is NOT A THEOREM!")
    else:
        print("The expression is a THEOREM!")
