
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ANDAND CARET COLON COMMA DECLAR DIVIDE DOUBQUO EQEQ EQUAL ID LCURLY LESS LESSEQ LPAREN MINUS MORE MOREEQ NEXT NOTEQ NUMBER OROR PLUS RCURLY RPAREN SEMICOLON STAR bool byte case complex64 default else float32 for if int string switch uint32 varassign : variable\n              | switchstate\n              | forstate\n              | express\n              | ifstate\n     ifstate : if exprif exprif : conditionsub statementsub\n               | conditionsub statementsub elsesub\n    conditionsub : LPAREN expression RPAREN\n                    | expression\n    statementsub : LCURLY NEXT id NEXT RCURLY\n                    | LCURLY NEXT if exprif NEXT RCURLY\n                    | LCURLY NEXT if exprif NEXT id NEXT RCURLY\n                    elsesub : else statementsubexpress : expression NEXT\n              | id DECLAR expression NEXT\n              | var id datatypes EQUAL expression NEXT\n              | var id EQUAL expression NEXT\n    forstate : for sentenceforsentencefor : expression block\n                   | expression nested\n     nested : LCURLY NEXT for sentencefor RCURLY NEXT block : LCURLY NEXT statementlist RCURLY NEXT\n    statementlist : id SEMICOLON NEXTswitchstate : switch sentenceswitchsentenceswitch : id SEMICOLON LCURLY NEXT exprcaseclauselist RCURLY\n                      | id SEMICOLON expression LCURLY NEXT exprcaseclauselist RCURLY\n                      | LCURLY NEXT exprcaseclauselist RCURLY\n                      | expression LCURLY NEXT exprcaseclauselist RCURLY\n    exprcaseclauselist : NEXT\n                         | exprcaseclauselist exprcaseclause\n    exprcaseclause : exprswitchcase COLON id NEXTexprswitchcase : case expression\n                      | default\n    id : IDnum : NUMBERvariable : var multipleids datatypes EQUAL expression NEXT\n                | multipleids DECLAR expression NEXT\n                | var multipleids EQUAL expression NEXT\n                | var multipleids NEXT\n                | var multipleids datatypes NEXT\n                | var LPAREN NEXT multidec RPAREN NEXT\n    multidec : multipleids datatypes EQUAL expression NEXT multidec\n                | NEXT\n    multipleids : id\n                   | multipleids COMMA multipleids\n    datatypes : bool\n                 | string\n                 | int\n                 | float32\n                 | complex64\n                 | byte\n                 | uint32\n    expression : unaryexpr\n                  | expression EQEQ expression\n                  | expression EQUAL expression\n                  | expression NOTEQ expression\n                  | expression LESS expression\n                  | expression MORE expression\n                  | expression PLUS expression\n                  | expression MINUS expression\n                  | expression CARET expression\n                  | expression STAR expression\n                  | expression DIVIDE expression\n                  | expression LESSEQ expression\n                  | expression MOREEQ expression\n                  | expression OROR expression\n                  | expression ANDAND expression\n    unaryexpr : num\n                 | id\n                 | DOUBQUO id DOUBQUO\n                 | LPAREN expression RPAREN\n                 | unaryop unaryexpr\n    unaryop : PLUS\n               | MINUS\n               | CARET\n               | STAR\n    '
    
_lr_action_items = {'var':([0,],[7,]),'switch':([0,],[11,]),'for':([0,116,],[12,137,]),'if':([0,120,],[14,141,]),'ID':([0,7,10,11,12,14,16,17,18,19,22,23,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,61,70,72,91,102,108,116,120,133,137,141,144,148,164,165,],[20,20,20,20,20,20,-74,-75,-76,-77,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'DOUBQUO':([0,10,11,12,14,16,17,18,19,20,23,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,58,61,72,91,102,108,133,137,141,144,],[22,22,22,22,22,-74,-75,-76,-77,-35,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,101,22,22,22,22,22,22,22,22,22,]),'LPAREN':([0,7,10,11,12,14,16,17,18,19,23,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,61,72,91,102,108,133,137,141,144,],[10,26,10,10,10,56,-74,-75,-76,-77,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,56,10,]),'NUMBER':([0,10,11,12,14,16,17,18,19,23,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,61,72,91,102,108,133,137,141,144,],[24,24,24,24,24,-74,-75,-76,-77,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'PLUS':([0,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,56,57,59,61,72,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,97,100,101,102,104,108,109,112,121,122,126,133,137,141,144,149,156,],[16,36,16,16,16,-70,16,-54,-74,-75,-76,-77,-35,-69,16,-36,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,36,-70,-70,36,36,16,16,36,-73,16,16,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-72,16,36,36,-71,16,36,16,36,36,-72,36,36,16,16,16,16,36,36,]),'MINUS':([0,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,56,57,59,61,72,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,97,100,101,102,104,108,109,112,121,122,126,133,137,141,144,149,156,],[17,37,17,17,17,-70,17,-54,-74,-75,-76,-77,-35,-69,17,-36,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,37,-70,-70,37,37,17,17,37,-73,17,17,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-72,17,37,37,-71,17,37,17,37,37,-72,37,37,17,17,17,17,37,37,]),'CARET':([0,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,56,57,59,61,72,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,97,100,101,102,104,108,109,112,121,122,126,133,137,141,144,149,156,],[18,38,18,18,18,-70,18,-54,-74,-75,-76,-77,-35,-69,18,-36,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,38,-70,-70,38,38,18,18,38,-73,18,18,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-72,18,38,38,-71,18,38,18,38,38,-72,38,38,18,18,18,18,38,38,]),'STAR':([0,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,56,57,59,61,72,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,97,100,101,102,104,108,109,112,121,122,126,133,137,141,144,149,156,],[19,39,19,19,19,-70,19,-54,-74,-75,-76,-77,-35,-69,19,-36,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,39,-70,-70,39,39,19,19,39,-73,19,19,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-72,19,39,39,-71,19,39,19,39,39,-72,39,39,19,19,19,19,39,39,]),'$end':([1,2,3,4,5,6,30,47,51,54,62,94,95,98,103,110,117,118,123,127,130,139,142,143,145,150,157,160,163,166,168,169,173,],[0,-1,-2,-3,-4,-5,-15,-25,-19,-6,-40,-20,-21,-7,-41,-38,-16,-8,-39,-18,-28,-14,-37,-42,-17,-29,-26,-23,-11,-27,-22,-12,-13,]),'DECLAR':([8,13,20,74,75,],[28,53,-35,-46,-45,]),'COMMA':([8,13,20,25,27,74,75,107,],[29,-45,-35,29,-45,29,-45,29,]),'NEXT':([9,13,15,20,21,24,25,26,27,46,49,59,60,63,64,65,66,67,68,69,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,96,97,98,99,101,104,109,111,115,118,122,124,126,128,129,139,140,147,151,153,155,156,159,161,163,165,169,170,173,],[30,-70,-54,-35,-69,-36,62,70,-45,-70,92,-73,103,-47,-48,-49,-50,-51,-52,-53,105,110,-46,-45,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-72,113,115,116,117,-7,120,-71,123,127,128,113,-8,142,143,145,113,147,-14,154,113,160,162,164,165,167,168,-11,105,-12,172,-13,]),'EQEQ':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[31,-70,-54,-35,-69,-36,31,-70,-70,31,31,31,-73,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-72,31,31,-71,31,31,31,-72,31,31,31,31,]),'EQUAL':([9,13,15,20,21,24,25,27,45,46,48,50,52,57,59,60,63,64,65,66,67,68,69,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,125,126,149,156,],[32,-70,-54,-35,-69,-36,61,72,32,-70,-70,32,32,32,-73,102,-47,-48,-49,-50,-51,-52,-53,108,32,-46,-45,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-72,32,32,-71,32,32,32,-72,32,144,32,32,32,]),'NOTEQ':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[33,-70,-54,-35,-69,-36,33,-70,-70,33,33,33,-73,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-72,33,33,-71,33,33,33,-72,33,33,33,33,]),'LESS':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[34,-70,-54,-35,-69,-36,34,-70,-70,34,34,34,-73,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-72,34,34,-71,34,34,34,-72,34,34,34,34,]),'MORE':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[35,-70,-54,-35,-69,-36,35,-70,-70,35,35,35,-73,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-72,35,35,-71,35,35,35,-72,35,35,35,35,]),'DIVIDE':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[40,-70,-54,-35,-69,-36,40,-70,-70,40,40,40,-73,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-72,40,40,-71,40,40,40,-72,40,40,40,40,]),'LESSEQ':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[41,-70,-54,-35,-69,-36,41,-70,-70,41,41,41,-73,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-72,41,41,-71,41,41,41,-72,41,41,41,41,]),'MOREEQ':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[42,-70,-54,-35,-69,-36,42,-70,-70,42,42,42,-73,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-72,42,42,-71,42,42,42,-72,42,42,42,42,]),'OROR':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[43,-70,-54,-35,-69,-36,43,-70,-70,43,43,43,-73,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-72,43,43,-71,43,43,43,-72,43,43,43,43,]),'ANDAND':([9,13,15,20,21,24,45,46,48,50,52,57,59,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,100,101,104,109,112,121,122,126,149,156,],[44,-70,-54,-35,-69,-36,44,-70,-70,44,44,44,-73,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-72,44,44,-71,44,44,44,-72,44,44,44,44,]),'LCURLY':([11,15,20,21,24,46,48,50,52,55,57,59,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,101,112,119,121,],[49,-54,-35,-69,-36,-70,-70,93,96,99,-10,-73,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-72,111,-71,129,99,-9,]),'RPAREN':([15,20,21,24,45,46,59,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,100,101,105,106,171,],[-54,-35,-69,-36,90,-70,-73,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-72,121,-71,-44,124,-43,]),'COLON':([15,20,21,24,46,59,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,101,132,134,149,],[-54,-35,-69,-36,-70,-73,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-72,-71,148,-34,-33,]),'bool':([20,25,27,74,75,107,],[-35,63,63,-46,-45,63,]),'string':([20,25,27,74,75,107,],[-35,64,64,-46,-45,64,]),'int':([20,25,27,74,75,107,],[-35,65,65,-46,-45,65,]),'float32':([20,25,27,74,75,107,],[-35,66,66,-46,-45,66,]),'complex64':([20,25,27,74,75,107,],[-35,67,67,-46,-45,67,]),'byte':([20,25,27,74,75,107,],[-35,68,68,-46,-45,68,]),'uint32':([20,25,27,74,75,107,],[-35,69,69,-46,-45,69,]),'SEMICOLON':([20,48,138,],[-35,91,153,]),'RCURLY':([94,95,113,114,131,135,136,146,152,154,158,160,162,164,167,168,172,],[-20,-21,-30,130,-31,150,151,157,161,163,166,-23,-24,169,-32,-22,173,]),'else':([98,163,169,173,],[119,-11,-12,-13,]),'case':([113,114,131,135,146,158,167,],[-30,133,-31,133,133,133,-32,]),'default':([113,114,131,135,146,158,167,],[-30,134,-31,134,134,134,-32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assign':([0,],[1,]),'variable':([0,],[2,]),'switchstate':([0,],[3,]),'forstate':([0,],[4,]),'express':([0,],[5,]),'ifstate':([0,],[6,]),'multipleids':([0,7,29,70,165,],[8,25,74,107,107,]),'expression':([0,10,11,12,14,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,61,72,91,102,108,133,137,141,144,],[9,45,50,52,57,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,97,100,104,109,112,122,126,149,52,57,156,]),'id':([0,7,10,11,12,14,22,23,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,61,70,72,91,102,108,116,120,133,137,141,144,148,164,165,],[13,27,46,48,46,46,58,46,46,75,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,75,46,46,46,46,138,140,46,46,46,46,159,170,75,]),'unaryexpr':([0,10,11,12,14,23,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,61,72,91,102,108,133,137,141,144,],[15,15,15,15,15,59,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'num':([0,10,11,12,14,23,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,61,72,91,102,108,133,137,141,144,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'unaryop':([0,10,11,12,14,23,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,53,56,61,72,91,102,108,133,137,141,144,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'sentenceswitch':([11,],[47,]),'sentencefor':([12,137,],[51,152,]),'exprif':([14,141,],[54,155,]),'conditionsub':([14,141,],[55,55,]),'datatypes':([25,27,107,],[60,71,125,]),'block':([52,],[94,]),'nested':([52,],[95,]),'statementsub':([55,119,],[98,139,]),'multidec':([70,165,],[106,171,]),'exprcaseclauselist':([92,115,128,147,],[114,135,146,158,]),'elsesub':([98,],[118,]),'exprcaseclause':([114,135,146,158,],[131,131,131,131,]),'exprswitchcase':([114,135,146,158,],[132,132,132,132,]),'statementlist':([116,],[136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assign","S'",1,None,None,None),
  ('assign -> variable','assign',1,'p_main','Go_Syntax.py',50),
  ('assign -> switchstate','assign',1,'p_main','Go_Syntax.py',51),
  ('assign -> forstate','assign',1,'p_main','Go_Syntax.py',52),
  ('assign -> express','assign',1,'p_main','Go_Syntax.py',53),
  ('assign -> ifstate','assign',1,'p_main','Go_Syntax.py',54),
  ('ifstate -> if exprif','ifstate',2,'p_ifstate','Go_Syntax.py',59),
  ('exprif -> conditionsub statementsub','exprif',2,'p_exprif','Go_Syntax.py',62),
  ('exprif -> conditionsub statementsub elsesub','exprif',3,'p_exprif','Go_Syntax.py',63),
  ('conditionsub -> LPAREN expression RPAREN','conditionsub',3,'p_conditionsub','Go_Syntax.py',67),
  ('conditionsub -> expression','conditionsub',1,'p_conditionsub','Go_Syntax.py',68),
  ('statementsub -> LCURLY NEXT id NEXT RCURLY','statementsub',5,'p_statementsub','Go_Syntax.py',71),
  ('statementsub -> LCURLY NEXT if exprif NEXT RCURLY','statementsub',6,'p_statementsub','Go_Syntax.py',72),
  ('statementsub -> LCURLY NEXT if exprif NEXT id NEXT RCURLY','statementsub',8,'p_statementsub','Go_Syntax.py',73),
  ('elsesub -> else statementsub','elsesub',2,'p_elsesub','Go_Syntax.py',77),
  ('express -> expression NEXT','express',2,'p_express','Go_Syntax.py',80),
  ('express -> id DECLAR expression NEXT','express',4,'p_express','Go_Syntax.py',81),
  ('express -> var id datatypes EQUAL expression NEXT','express',6,'p_express','Go_Syntax.py',82),
  ('express -> var id EQUAL expression NEXT','express',5,'p_express','Go_Syntax.py',83),
  ('forstate -> for sentencefor','forstate',2,'p_forstate','Go_Syntax.py',87),
  ('sentencefor -> expression block','sentencefor',2,'p_sentencefor','Go_Syntax.py',90),
  ('sentencefor -> expression nested','sentencefor',2,'p_sentencefor','Go_Syntax.py',91),
  ('nested -> LCURLY NEXT for sentencefor RCURLY NEXT','nested',6,'p_nested','Go_Syntax.py',95),
  ('block -> LCURLY NEXT statementlist RCURLY NEXT','block',5,'p_block','Go_Syntax.py',98),
  ('statementlist -> id SEMICOLON NEXT','statementlist',3,'p_statementlist','Go_Syntax.py',102),
  ('switchstate -> switch sentenceswitch','switchstate',2,'p_switchstate','Go_Syntax.py',105),
  ('sentenceswitch -> id SEMICOLON LCURLY NEXT exprcaseclauselist RCURLY','sentenceswitch',6,'p_sentenceswitch','Go_Syntax.py',108),
  ('sentenceswitch -> id SEMICOLON expression LCURLY NEXT exprcaseclauselist RCURLY','sentenceswitch',7,'p_sentenceswitch','Go_Syntax.py',109),
  ('sentenceswitch -> LCURLY NEXT exprcaseclauselist RCURLY','sentenceswitch',4,'p_sentenceswitch','Go_Syntax.py',110),
  ('sentenceswitch -> expression LCURLY NEXT exprcaseclauselist RCURLY','sentenceswitch',5,'p_sentenceswitch','Go_Syntax.py',111),
  ('exprcaseclauselist -> NEXT','exprcaseclauselist',1,'p_exprcaseclauselist','Go_Syntax.py',115),
  ('exprcaseclauselist -> exprcaseclauselist exprcaseclause','exprcaseclauselist',2,'p_exprcaseclauselist','Go_Syntax.py',116),
  ('exprcaseclause -> exprswitchcase COLON id NEXT','exprcaseclause',4,'p_exprcaseclause','Go_Syntax.py',119),
  ('exprswitchcase -> case expression','exprswitchcase',2,'p_exprswitchcase','Go_Syntax.py',122),
  ('exprswitchcase -> default','exprswitchcase',1,'p_exprswitchcase','Go_Syntax.py',123),
  ('id -> ID','id',1,'p_id','Go_Syntax.py',127),
  ('num -> NUMBER','num',1,'p_num','Go_Syntax.py',130),
  ('variable -> var multipleids datatypes EQUAL expression NEXT','variable',6,'p_variable','Go_Syntax.py',133),
  ('variable -> multipleids DECLAR expression NEXT','variable',4,'p_variable','Go_Syntax.py',134),
  ('variable -> var multipleids EQUAL expression NEXT','variable',5,'p_variable','Go_Syntax.py',135),
  ('variable -> var multipleids NEXT','variable',3,'p_variable','Go_Syntax.py',136),
  ('variable -> var multipleids datatypes NEXT','variable',4,'p_variable','Go_Syntax.py',137),
  ('variable -> var LPAREN NEXT multidec RPAREN NEXT','variable',6,'p_variable','Go_Syntax.py',138),
  ('multidec -> multipleids datatypes EQUAL expression NEXT multidec','multidec',6,'p_multidec','Go_Syntax.py',142),
  ('multidec -> NEXT','multidec',1,'p_multidec','Go_Syntax.py',143),
  ('multipleids -> id','multipleids',1,'p_multipleids','Go_Syntax.py',147),
  ('multipleids -> multipleids COMMA multipleids','multipleids',3,'p_multipleids','Go_Syntax.py',148),
  ('datatypes -> bool','datatypes',1,'p_datatypes','Go_Syntax.py',152),
  ('datatypes -> string','datatypes',1,'p_datatypes','Go_Syntax.py',153),
  ('datatypes -> int','datatypes',1,'p_datatypes','Go_Syntax.py',154),
  ('datatypes -> float32','datatypes',1,'p_datatypes','Go_Syntax.py',155),
  ('datatypes -> complex64','datatypes',1,'p_datatypes','Go_Syntax.py',156),
  ('datatypes -> byte','datatypes',1,'p_datatypes','Go_Syntax.py',157),
  ('datatypes -> uint32','datatypes',1,'p_datatypes','Go_Syntax.py',158),
  ('expression -> unaryexpr','expression',1,'p_expression','Go_Syntax.py',162),
  ('expression -> expression EQEQ expression','expression',3,'p_expression','Go_Syntax.py',163),
  ('expression -> expression EQUAL expression','expression',3,'p_expression','Go_Syntax.py',164),
  ('expression -> expression NOTEQ expression','expression',3,'p_expression','Go_Syntax.py',165),
  ('expression -> expression LESS expression','expression',3,'p_expression','Go_Syntax.py',166),
  ('expression -> expression MORE expression','expression',3,'p_expression','Go_Syntax.py',167),
  ('expression -> expression PLUS expression','expression',3,'p_expression','Go_Syntax.py',168),
  ('expression -> expression MINUS expression','expression',3,'p_expression','Go_Syntax.py',169),
  ('expression -> expression CARET expression','expression',3,'p_expression','Go_Syntax.py',170),
  ('expression -> expression STAR expression','expression',3,'p_expression','Go_Syntax.py',171),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','Go_Syntax.py',172),
  ('expression -> expression LESSEQ expression','expression',3,'p_expression','Go_Syntax.py',173),
  ('expression -> expression MOREEQ expression','expression',3,'p_expression','Go_Syntax.py',174),
  ('expression -> expression OROR expression','expression',3,'p_expression','Go_Syntax.py',175),
  ('expression -> expression ANDAND expression','expression',3,'p_expression','Go_Syntax.py',176),
  ('unaryexpr -> num','unaryexpr',1,'p_unaryexpr','Go_Syntax.py',180),
  ('unaryexpr -> id','unaryexpr',1,'p_unaryexpr','Go_Syntax.py',181),
  ('unaryexpr -> DOUBQUO id DOUBQUO','unaryexpr',3,'p_unaryexpr','Go_Syntax.py',182),
  ('unaryexpr -> LPAREN expression RPAREN','unaryexpr',3,'p_unaryexpr','Go_Syntax.py',183),
  ('unaryexpr -> unaryop unaryexpr','unaryexpr',2,'p_unaryexpr','Go_Syntax.py',184),
  ('unaryop -> PLUS','unaryop',1,'p_unaryop','Go_Syntax.py',188),
  ('unaryop -> MINUS','unaryop',1,'p_unaryop','Go_Syntax.py',189),
  ('unaryop -> CARET','unaryop',1,'p_unaryop','Go_Syntax.py',190),
  ('unaryop -> STAR','unaryop',1,'p_unaryop','Go_Syntax.py',191),
]