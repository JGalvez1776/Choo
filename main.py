import sys
from grammar import *

def open_files(args):
    assert len(args) >= 1, "Include at least the file to read"
    assert '.txt' in args[0], "Make sure you input a txt file"
    original_name = args[0]

    if len(args) == 1:
        out_name = original_name[:len(args[0]) - 4] + ".py"
    else:
        out_name = args[1]
        assert ".py" in args[1], "Output must be a .py file"

    file = open(original_name, 'r')
    content = file.readlines()
    file.close()
    out = open(out_name, 'w')
    return content, out

def out_arguements(file, out_file):
    line = file[0]
    line = line.strip().split(" ")
    msg = "Argument count formatted incorrectly. "
    msg += "Must be \"Arguments = INTEGER\""
    assert len(line) == 3, msg
    assert line[0] == "Arguments", msg
    assert line[1] == "=", msg
    assert line[2].isnumeric(), msg
    count = int(line[2])
    for i in range(1, count + 1):
        variables.append(f"ARGS[{i}]")

    print("import sys") 
    print("ARGS = sys.argv[1:]")
    print(f"while len(ARGS) < {count}:")
    print("\tARGS.append(0)")
    print("for i in range(len(ARGS)):")
    print("\tARGS[i] = int(ARGS[i])")
    print()
    

def main(args):
    file, out = open_files(args)
    #sys.stdout = out


    out_arguements(file, out)
    expected_indentation = 0
    for line in file[1:]:
        line, indentation = format_line(line)
        if expected_indentation != indentation:
            assert False, "Incorrect indentation"

        if len(line) == 0:
            continue
        
        if line[0][0] == "#":
            print(' '.join(line))
            continue

        if line[0] in grammar:
            grammar_rule = grammar[line[0]]
            if grammar_rule["indent_next"]:
                expected_indentation += 1
            if grammar_rule["check"](line):
                print("\t" * indentation, end="")
                grammar_rule["out"](line)
            else:
                assert False, f"Invalid handling of {line[0]}"
        elif line[0] == "END":
            expected_indentation -= 1
        elif line[0] in variables or line[0].startswith("ARGS"):
            line = ["var"] + line
            grammar_rule = grammar["var"]
            if grammar_rule["check"](line):
                print("\t" * indentation, end="")
                grammar_rule["out"](line)
            else:
                assert False, f"Invalid handling of {line[0]}"
        else:
            assert False, "Poorly formatted line found"

        #print(f"\"{line}\" {indentation}")

    out.close()

def format_line(line):
    line = line.strip("\n").split(" ")
    indentation = get_indentation(line)
    return line, indentation

def format_args(args):
    return [int(elem) for elem in args]

def get_indentation(line):
    i = 0
    while i < len(line) and line[i] == "":
        i += 1
    # TODO: This caps the size of indentations
    i = int(i / 4)
    while "" in line:
        line.remove("")
    #while len(line) > 0 and line[0] == "":
    #    line.pop(0)
    
    return i

if __name__ == "__main__":
    main(sys.argv[1:])  