import warnings
warnings.filterwarnings("ignore")

import ply.lex as lex
import ply.yacc as yacc

reserved={'if':'if','else':'else'}

tokens=['EQUAL','EQEQ','NOTEQ','LPAREN','RPAREN','NUMBER','ID','LCURLY','RCURLY','SEMICOLON','PLUS',
        'LESS','MORE','MINUS','STAR','CARET','DIVIDE','NEXT','COLON','LESSEQ','MOREEQ','OROR','ANDAND']+list(reserved.values())

t_ignore=' '
t_EQUAL=r'\='
t_NEXT = '\\n'
t_EQEQ=r'\=='
t_NOTEQ=r'\!='
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_LCURLY=r'\{'
t_RCURLY=r'\}'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_LESS=r'\<'
t_MORE=r'\>'
t_STAR=r'\*'
t_CARET=r'\^'
t_DIVIDE=r'\\'
t_COLON=r'\:'
t_LESSEQ=r'\<='
t_MOREEQ=r'\>='
t_OROR=r'\|\|'
t_ANDAND=r'\&&'

def t_NUMBER(t):
   r'\d+'
   t.value=int(t.value)
   return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def p_if(p):
    '''assign : for sentence'''
    print("Syntax is correct .");

def p_error(p):
  print("Syntax error .");

def t_error(p):
    print("Syntax incorrect");

lex.lex();
yacc.yacc();

data=''' for 5 == 5 {
for a > b {
statement ;
}
}
''';

yacc.parse(data)

