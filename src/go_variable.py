import warnings
warnings.filterwarnings("ignore")

import ply.lex as lex
import ply.yacc as yacc

reserved={'var':'var','bool':'bool','string':'string','int':'int','float32':'float32','complex64':'complex64',
          'byte':'byte','uint32':'uint32'}

tokens=['EQUAL','EQEQ','NOTEQ','LPAREN','RPAREN','NUMBER','ID','PLUS','LESS','MORE','MINUS','STAR','CARET',
        'DIVIDE','NEXT','LESSEQ','MOREEQ','OROR','ANDAND','DECLAR','COMMA','DOUBQUO']+list(reserved.values())

t_ignore=' '
t_EQUAL=r'\='
t_NEXT = '\\n'
t_EQEQ=r'\=='
t_NOTEQ=r'\!='
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_LESS=r'\<'
t_MORE=r'\>'
t_STAR=r'\*'
t_CARET=r'\^'
t_DIVIDE=r'\\'
t_LESSEQ=r'\<='
t_MOREEQ=r'\>='
t_OROR=r'\|\|'
t_ANDAND=r'\&&'
t_DECLAR=r'\:='
t_COMMA=r'\,'
t_DOUBQUO=r'\"'

def t_NUMBER(t):
   r'\d+'
   t.value=int(t.value)
   return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def p_variable(p):
    '''assign : var multipleids datatypes EQUAL expression NEXT
              | multipleids DECLAR expression NEXT
              | var multipleids EQUAL expression NEXT
              | var multipleids NEXT
              | var multipleids datatypes NEXT
              | var LPAREN NEXT multidec RPAREN NEXT
    '''
    print("Syntax is correct .");

def p_multidec(p):
    '''multidec : multipleids datatypes EQUAL expression NEXT multidec
                | NEXT
    '''

def p_multipleids(p):
    '''multipleids : id
                   | multipleids COMMA multipleids
    '''

def p_datatypes(p):
    '''datatypes : bool
                 | string
                 | int
                 | float32
                 | complex64
                 | byte
                 | uint32
    '''

def p_expression(p):
    '''expression : unaryexpr
                  | expression EQEQ expression
                  | expression EQUAL expression
                  | expression NOTEQ expression
                  | expression LESS expression
                  | expression MORE expression
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression CARET expression
                  | expression STAR expression
                  | expression DIVIDE expression
                  | expression LESSEQ expression
                  | expression MOREEQ expression
                  | expression OROR expression
                  | expression ANDAND expression
    '''

def p_unaryexpr(p):
    '''unaryexpr : num
                 | id
                 | DOUBQUO id DOUBQUO
                 | LPAREN expression RPAREN
                 | unaryop unaryexpr
    '''

def p_unaryop(p):
    '''unaryop : PLUS
               | MINUS
               | CARET
               | STAR
    '''

def p_id(p):
 'id : ID'

def p_num(p):
 'num : NUMBER'

def p_error(p):
  print("Syntax error .");

def t_error(p):
    print("Syntax incorrect");

lex.lex();
yacc.yacc();

data=''' var (
hello string = " hey "
sup int = 5

)
''';

yacc.parse(data)