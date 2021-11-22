from os import linesep


variables = []

def is_valid_expression(expr):
    if not balanced_parenthesis(expr):
        return False
    
    i = 0
    for elem in expr:
        elem = elem.strip("[]")
        #for character in "+-*/%":
        #    if character == elem and i % 2 == 0:
        #        return False
        if i % 2 == 0:
            assert elem.isnumeric() or elem in variables
        else:
            assert len(elem) == 1 and elem in '+-*/%'
        i += 1
    return True

def balanced_parenthesis(expr):
    i = 0
    while i < len(expr):
        par_count = 0
        while expr[i][par_count] == "(":
            par_count += 1
        expr[i] = expr[i].replace("(", "[", par_count)
        for i in range(par_count):
            if not check_closes(expr, i):
                #print(expr)
                return False 
        if ")" in expr[i]:
            #print(expr)
            return False
        i += 1
    return True

def check_closes(expr, start):
    for i in range(start, len(expr)):
        if ")" in expr[i]:
            expr[i] = expr[i].replace(")", "]", 1)
            return True
    return False

def var_check(line):
    # ["var", name, "=", ...]
    # Assumes an int
    msg = f"Poorly formatted variable : {line}"
    assert line[0] == "var", msg
    assert not line[1].isnumeric(), msg
    assert line[2] == "=", msg
    if "ARGS" not in line[3:][0]:
        assert is_valid_expression(line[3:]), \
                msg + " "  + f"Invald expression : {line[3:]}"
    variables.append(line[1])
    return True

def var_out(line):
    print(line[1], "=", " ".join(line[3:]))


def validate_bool_expression(expr):
    if not validate_boolean_form(expr):
        return False

# Converstions for my grammar to Python
boolean_terms = {
    "||" : "or",
    "&&" : "and",
    ">=" : ">=",
    ">"  : ">",
    "<"  : "<",
    "<=" : "<=",
    "==" : "==",
    "!=" : "!=",
    "~" : "not"
}

def in_terms(elem):
    for key in boolean_terms:
        if elem == key:
            return True
    return False

def validate_boolean_form(expr):
    is_term = True
    for i in range(1, len(expr)):
        elem = expr[i]
        if elem == "~" and is_term:
            expr[i] = "not"
            continue
        if elem in boolean_terms and is_term:
            return False
        elif in_terms(elem):
            expr[i] = boolean_terms[elem]
        elif not is_term:
            return False
        elif elem == "true" or elem == "false":
            expr[i] = elem.capitalize()
        elif elem not in variables and not elem.isnumeric():
            return False
        
        is_term = not is_term
    return True


def if_check(line, name="if"):
    msg = f"Poorly formatted {name} statement: {line}"
    assert line[0] == name, msg
    if not validate_boolean_form(line):
        return False
    return True

def if_out(line):
    print(line[0] + " " + " ".join(line[1:]) + ":")

def elif_check(line):
    return if_check(line, "elif")

def elif_out(line):
    if_out(line)

def else_check(line):
    return line[0] == "else" and len(line) == 1

def else_out(line):
    print(line[0] + ":")


def is_string(line):
    msg = f"Poorly formatted string: {line}"
    assert line[0][0] == "\"", msg
    assert line[-1][-1] == "\"", msg
    line[0] = line[0][1:]
    line[-1] = line[-1][:len(line[-1]) - 1]
    string = " ".join(line)
    assert "\"" not in line, msg
    return True

def print_check(line):
    msg = f"Poorly formatted print: {line}"
    assert line[0] == "print", msg
    assert is_string(line[1:]) , msg
    return True

def print_out(line):
    print(f'print({" ".join(line[1:])}, end=\'\')')

def println_check(line):
    msg = f"Poorly formatted println: {line}"

    assert line[0] == "println", msg
    assert is_string(line[1:]), msg
    return True

def println_out(line):
    print(f'print({" ".join(line[1:])})')

def printvar_check(line):
    msg = f"Poorly formatted printvar: {line}"

    assert line[0] == "printvar", msg
    assert line[1] in variables, msg
    return True

def printvar_out(line):
    print(f"print({line[1]}, end='')")

def while_check(line):
    return if_check(line, "while")

def while_out(line):
    if_out(line)