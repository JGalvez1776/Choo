from utils import *

grammar = {
    "var"     : {"check" : var_check,
                 "out" : var_out,
                 "indent_next" : False},

    "if"      : {"check" : if_check,
                 "out" : if_out,
                 "indent_next" : True},

    "elif"    : {"check" : elif_check,
                 "out" : elif_out,
                 "indent_next" : True},

    "else"    : {"check" : else_check,
                 "out" : else_out,
                 "indent_next" : True},

    "print"   : {"check" : print_check,
                 "out" : print_out,
                 "indent_next" : False},

    "println" : {"check" : println_check,
                 "out" : println_out,
                 "indent_next" : False},
    
    "printvar" : {"check" : printvar_check,
                  "out" : printvar_out,
                  "indent_next" : False},

    "while"   : {"check" : while_check,
                 "out" : while_out,
                 "indent_next" : True}

}   