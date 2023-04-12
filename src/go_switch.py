import warnings
warnings.filterwarnings("ignore")

import ply.lex as lex
import ply.yacc as yacc

reserved={'switch':'switch','case':'case','default':'default'}

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
t_SEMICOLON=r'\;'
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

def p_switchstate(p):
    '''assign : switch sentence'''
    print("Syntax is correct .");

def p_id(p):
 'id : ID'

def p_num(p):
 'num : NUMBER'

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
                 | LPAREN expression RPAREN
                 | unaryop unaryexpr
    '''

def p_unaryop(p):
    '''unaryop : PLUS
               | MINUS
               | CARET
               | STAR
    '''

def p_sentence(p):
    '''sentence : id SEMICOLON LCURLY NEXT exprcaseclauselist RCURLY
                | id SEMICOLON expression LCURLY NEXT exprcaseclauselist RCURLY
                | LCURLY NEXT exprcaseclauselist RCURLY
                | expression LCURLY NEXT exprcaseclauselist RCURLY
    '''

def p_exprcaseclauselist(p):
    '''exprcaseclauselist : NEXT
                         | exprcaseclauselist exprcaseclause
    '''
def p_exprcaseclause(p):
    '''exprcaseclause : exprswitchcase COLON id NEXT'''

def p_exprswitchcase(p):
    '''exprswitchcase : case expression
                      | default
    '''

def p_error(p):
  print("Syntax error .");

def t_error(p):
    print("Syntax incorrect");

lex.lex();
yacc.yacc();

data='''switch statement ; {

case 2=2 : statement
case 3=4 : statement
default : statement
}''';

yacc.parse(data)
