# Choo
This is a basic programming language made for a school project. Running this script compiles code into a py file that can then be run.

## Usage
To run insert the files to compile in the same directory (Python can be a little wierd opening files in other directories). Then run the following command:

```shell
python3 main.py [ORIGIN] >> [OUTPUT] 
```
- `[ORIGIN]` The name of the file to be compiled. Make sure it ends with the extension **txtx**

- `[OUTPUT]` The name for the new compiled file.

The now "compiled" (Python is interpreted) code can be run with the following command:

```
python3 [OUTPUT] [ARG]
```

- `[ARG]` A command line arguement. Seperate multiple with spaces and there can be a maximum amount of arguements which is defined by the original file.

## Syntax

Refer to the language grammar for more details. The use of whitespace is intentional. Any syntax that is shown with spaces **requires** the spaces due to how the language is parsed.

**All indentations must be 4 spaces.**

All uses of `[]` are to denote some non-explicit value. **Do not write the brackets.**

### File Structure:

**Note**: All files must follow the following constraints

1. Must have the **txt** file extension.
2. The first line must be of the form:
    `Arguments = [INTEGER]`
    Where `[INTEGER]` is the **maximum** amount of command line arguements. Any arguements not passed in by the user default to `0`.

### Variables
A can be any sequence of characters made up of letters and/or numbers. Can not be all numbers. While not enforced, using a keyword as a variable may result in the created program not working as intended.



### Variable Assignment
To assign a new variable use the following syntax:
`var [VARIABLE] = [INTEGER EXPRESSION]`

Once assigned, you may modify that variable by doing:
`[VARIABLE] = [INTEGER EXPRESSION]`

**Note:** This syntax requires that the variable is already assigned to work.

Examples:
```
var x = 0
```
```
x = x + 1
```

### Integer Expressions

`[INTEGER EXPRESSION] [OPERATION] [INTEGER/VARIABLE]`

`[OPERATION]` +, -, /, *, %

Example:
    `1 + (2 / 3 * (4 - 2)) % 1`
Whitespace is needed between terms, however parenthesis should be the character before or after a term.

### Boolean Expressions / Comparisons
**Note:** Terms in boolean/comparisons expression can not contain integer expression. If that is required, save the value to a variable first then use that. Parenthesis are not supported.

|Operator|Meaning|
| --- | --- |
| `||` | Logical or |
| `&&` | Logical and |
| `> `| Greater than |
| `< `| Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |
| `~ ` | Logical not |

Example:
`false || 3 == 2 && 1 > a || ~ true`

### Blocks
Blocks are denoted by the following syntax:
```
[START] [CONDITION]
    # Code
    END
```
`[START]` if, elif, else, while
`[CONDITION]` A boolean expression

### Conditionals
Examples:
```
if false || 3 == 2 && 1 > a
    # Code
    END
```

```
if [CONDITION]
    # Code
    END
else
    # Code
    END

```

```
if [CONDITION]
    # Code
    END
elif [CONDITION]
    # Code
    END
else
    # Code    
    END
```

**Note:** There may be as many elif blocks, however there must be only a single else.

### While
Example:
```
while [CONDITION]
    # Code
    END
```

### Printing
All version of print accept **exactly** one arguement.

Print a given string **without** a newline added.
```
print [STRING]
```

Print a given string **with** a new line added.
```
println [STRING]
```

Print the value of a variable.
```
printvar [VARIABLE]
```

Strings are only used with prints they can not be saved to variables.

### Command Line Arguements
Command line arguements can be access using:

```
ARGS[0]
```

```
ARGS[1]
```

```
ARGS[2]
```

```
...
```

**NOTE HERE YOU ACTUALLY WRITE THE BRACKETS**