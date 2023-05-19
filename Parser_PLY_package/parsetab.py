
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUM IDEN STRING PLUS TIMES DIVIDE MOD MINUS LPAREN RPAREN LBRACE RBRACE LSQUAREBR RSQUAREBR COLON COMMA SEMI_COLON LESS_THAN LESS_EQUAL GREATER_THAN GREATER_EQUAL EQ NOT_EQ PARITY NOT QMARK FOR IF ELSE RETURN WHILE TO INT DEF VAR AND OR VECTOR NULLprog : funcprog : func progfunc : DEF type iden LPAREN flist RPAREN LBRACE body RBRACEfunc : DEF type iden LPAREN error RPAREN LBRACE body RBRACEbody : stmtbody : stmt bodystmt : expr SEMI_COLONstmt : defvar SEMI_COLONstmt : IF LPAREN expr RPAREN stmt else_choicestmt : IF LPAREN error RPAREN stmt else_choiceelse_choice : emptyelse_choice : ELSE stmtstmt : funcstmt : FOR LPAREN expr TO expr RPAREN stmtstmt : RETURN expr SEMI_COLONstmt : LBRACE body RBRACEstmt : WHILE LPAREN expr RPAREN stmtexpr : iden LPAREN clist RPARENexpr : iden LPAREN error RPARENexpr : expr LSQUAREBR expr RSQUAREBRexpr : expr LSQUAREBR error RSQUAREBRexpr : expr QMARK expr COLON exprexpr : expr PARITY expr \n                 | expr NOT_EQ expr \n                 | expr DIVIDE expr\n                 | expr TIMES expr\n                 | expr MINUS expr\n                 | expr PLUS expr\n                 | expr MOD expr \n                 | expr GREATER_EQUAL expr \n                 | expr LESS_EQUAL expr \n                 | expr GREATER_THAN expr\n                 | expr LESS_THAN expr\n                 | expr OR expr \n                 | expr AND expr \n                 | expr EQ exprexpr : MINUS expr \n                 | PLUS expr \n                 | NOT exprexpr : LSQUAREBR clist RSQUAREBRexpr : LSQUAREBR error RSQUAREBRexpr : idenexpr : numclist : emptyclist : exprclist : expr COMMA clistdefvar : VAR type idendefvar : VAR type iden EQ exprflist : emptyflist : type idenflist : type iden COMMA flistiden : IDENtype : INT\n                | VECTOR\n                | STRING\n                | NULLnum : NUMempty :'
    
_lr_action_items = {'DEF':([0,2,21,22,25,27,31,45,47,64,77,80,101,112,113,115,119,120,122,124,125,126,127,128,129,130,],[3,3,3,3,3,3,-13,-3,-7,-8,-4,-16,-15,3,3,3,-58,-58,-17,-9,-11,3,-10,3,-12,-14,]),'$end':([1,2,4,45,77,],[0,-1,-2,-3,-4,]),'INT':([3,12,20,40,],[6,6,6,6,]),'VECTOR':([3,12,20,40,],[7,7,7,7,]),'STRING':([3,12,20,40,],[8,8,8,8,]),'NULL':([3,12,20,40,],[9,9,9,9,]),'IDEN':([5,6,7,8,9,13,21,22,25,27,31,33,35,36,37,38,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,76,77,80,101,105,111,112,113,114,115,117,119,120,122,124,125,126,127,128,129,130,],[11,-53,-54,-55,-56,11,11,11,11,11,-13,11,11,11,11,11,11,-3,-7,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-8,11,11,11,11,-4,-16,-15,11,11,11,11,11,11,11,-58,-58,-17,-9,-11,11,-10,11,-12,-14,]),'LPAREN':([10,11,24,30,32,34,],[12,-52,43,65,66,68,]),'COMMA':([11,17,24,39,41,72,73,74,75,84,85,86,87,88,89,90,91,92,93,94,95,96,97,103,104,107,108,109,110,118,],[-52,20,-42,-43,-57,105,-37,-38,-39,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-40,-41,-18,-19,-20,-21,-22,]),'RPAREN':([11,12,14,15,16,17,20,23,24,39,41,43,71,72,73,74,75,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,102,103,104,105,107,108,109,110,116,118,121,],[-52,-58,18,19,-49,-50,-58,-51,-42,-43,-57,-58,-44,-45,-37,-38,-39,107,108,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,112,113,115,-40,-41,-58,-18,-19,-20,-21,-46,-22,128,]),'SEMI_COLON':([11,24,28,29,39,41,67,73,74,75,84,85,86,87,88,89,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,118,123,],[-52,-42,47,64,-43,-57,101,-37,-38,-39,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-40,-41,-47,-18,-19,-20,-21,-22,-48,]),'LSQUAREBR':([11,21,22,24,25,27,28,31,33,35,36,37,38,39,41,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,73,74,75,77,80,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,102,103,104,105,107,108,109,110,111,112,113,114,115,117,118,119,120,121,122,123,124,125,126,127,128,129,130,],[-52,35,35,-42,35,35,48,-13,35,35,35,35,35,-43,-57,35,-3,-7,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-8,35,35,48,35,48,48,48,48,-4,-16,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-15,48,-40,-41,35,-18,-19,-20,-21,35,35,35,35,35,35,48,-58,-58,48,-17,48,-9,-11,35,-10,35,-12,-14,]),'QMARK':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,49,-43,-57,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-40,-41,-18,-19,-20,-21,49,49,49,]),'PARITY':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,50,-43,-57,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-40,-41,-18,-19,-20,-21,50,50,50,]),'NOT_EQ':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,51,-43,-57,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-40,-41,-18,-19,-20,-21,51,51,51,]),'DIVIDE':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,52,-43,-57,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-40,-41,-18,-19,-20,-21,52,52,52,]),'TIMES':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,53,-43,-57,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-40,-41,-18,-19,-20,-21,53,53,53,]),'MINUS':([11,21,22,24,25,27,28,31,33,35,36,37,38,39,41,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,73,74,75,77,80,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,102,103,104,105,107,108,109,110,111,112,113,114,115,117,118,119,120,121,122,123,124,125,126,127,128,129,130,],[-52,36,36,-42,36,36,54,-13,36,36,36,36,36,-43,-57,36,-3,-7,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-8,36,36,54,36,54,54,54,54,-4,-16,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-15,54,-40,-41,36,-18,-19,-20,-21,36,36,36,36,36,36,54,-58,-58,54,-17,54,-9,-11,36,-10,36,-12,-14,]),'PLUS':([11,21,22,24,25,27,28,31,33,35,36,37,38,39,41,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,73,74,75,77,80,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,102,103,104,105,107,108,109,110,111,112,113,114,115,117,118,119,120,121,122,123,124,125,126,127,128,129,130,],[-52,37,37,-42,37,37,55,-13,37,37,37,37,37,-43,-57,37,-3,-7,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-8,37,37,55,37,55,55,55,55,-4,-16,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-15,55,-40,-41,37,-18,-19,-20,-21,37,37,37,37,37,37,55,-58,-58,55,-17,55,-9,-11,37,-10,37,-12,-14,]),'MOD':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,56,-43,-57,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-40,-41,-18,-19,-20,-21,56,56,56,]),'GREATER_EQUAL':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,57,-43,-57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-40,-41,-18,-19,-20,-21,57,57,57,]),'LESS_EQUAL':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,58,-43,-57,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-40,-41,-18,-19,-20,-21,58,58,58,]),'GREATER_THAN':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,59,-43,-57,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-40,-41,-18,-19,-20,-21,59,59,59,]),'LESS_THAN':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,60,-43,-57,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-40,-41,-18,-19,-20,-21,60,60,60,]),'OR':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,61,-43,-57,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-40,-41,-18,-19,-20,-21,61,61,61,]),'AND':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,107,108,109,110,118,121,123,],[-52,-42,62,-43,-57,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-40,-41,-18,-19,-20,-21,62,62,62,]),'EQ':([11,24,28,39,41,67,72,73,74,75,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,106,107,108,109,110,118,121,123,],[-52,-42,63,-43,-57,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-40,-41,117,-18,-19,-20,-21,63,63,63,]),'RSQUAREBR':([11,24,35,39,41,69,70,71,72,73,74,75,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,103,104,105,107,108,109,110,116,118,],[-52,-42,-58,-43,-57,103,104,-44,-45,-37,-38,-39,109,110,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-40,-41,-58,-18,-19,-20,-21,-46,-22,]),'COLON':([11,24,39,41,73,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,103,104,107,108,109,110,118,],[-52,-42,-43,-57,-37,-38,-39,111,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-40,-41,-18,-19,-20,-21,-22,]),'TO':([11,24,39,41,73,74,75,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,103,104,107,108,109,110,118,],[-52,-42,-43,-57,-37,-38,-39,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,114,-40,-41,-18,-19,-20,-21,-22,]),'error':([12,35,43,48,65,],[15,70,79,82,99,]),'LBRACE':([18,19,21,22,25,27,31,45,47,64,77,80,101,112,113,115,119,120,122,124,125,126,127,128,129,130,],[21,22,25,25,25,25,-13,-3,-7,-8,-4,-16,-15,25,25,25,-58,-58,-17,-9,-11,25,-10,25,-12,-14,]),'IF':([21,22,25,27,31,45,47,64,77,80,101,112,113,115,119,120,122,124,125,126,127,128,129,130,],[30,30,30,30,-13,-3,-7,-8,-4,-16,-15,30,30,30,-58,-58,-17,-9,-11,30,-10,30,-12,-14,]),'FOR':([21,22,25,27,31,45,47,64,77,80,101,112,113,115,119,120,122,124,125,126,127,128,129,130,],[32,32,32,32,-13,-3,-7,-8,-4,-16,-15,32,32,32,-58,-58,-17,-9,-11,32,-10,32,-12,-14,]),'RETURN':([21,22,25,27,31,45,47,64,77,80,101,112,113,115,119,120,122,124,125,126,127,128,129,130,],[33,33,33,33,-13,-3,-7,-8,-4,-16,-15,33,33,33,-58,-58,-17,-9,-11,33,-10,33,-12,-14,]),'WHILE':([21,22,25,27,31,45,47,64,77,80,101,112,113,115,119,120,122,124,125,126,127,128,129,130,],[34,34,34,34,-13,-3,-7,-8,-4,-16,-15,34,34,34,-58,-58,-17,-9,-11,34,-10,34,-12,-14,]),'NOT':([21,22,25,27,31,33,35,36,37,38,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,77,80,101,105,111,112,113,114,115,117,119,120,122,124,125,126,127,128,129,130,],[38,38,38,38,-13,38,38,38,38,38,38,-3,-7,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-8,38,38,38,-4,-16,-15,38,38,38,38,38,38,38,-58,-58,-17,-9,-11,38,-10,38,-12,-14,]),'VAR':([21,22,25,27,31,45,47,64,77,80,101,112,113,115,119,120,122,124,125,126,127,128,129,130,],[40,40,40,40,-13,-3,-7,-8,-4,-16,-15,40,40,40,-58,-58,-17,-9,-11,40,-10,40,-12,-14,]),'NUM':([21,22,25,27,31,33,35,36,37,38,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,77,80,101,105,111,112,113,114,115,117,119,120,122,124,125,126,127,128,129,130,],[41,41,41,41,-13,41,41,41,41,41,41,-3,-7,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-8,41,41,41,-4,-16,-15,41,41,41,41,41,41,41,-58,-58,-17,-9,-11,41,-10,41,-12,-14,]),'RBRACE':([26,27,31,42,44,45,46,47,64,77,80,101,119,120,122,124,125,127,129,130,],[45,-5,-13,77,80,-3,-6,-7,-8,-4,-16,-15,-58,-58,-17,-9,-11,-10,-12,-14,]),'ELSE':([31,45,47,64,77,80,101,119,120,122,124,125,127,129,130,],[-13,-3,-7,-8,-4,-16,-15,126,126,-17,-9,-11,-10,-12,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,2,],[1,4,]),'func':([0,2,21,22,25,27,112,113,115,126,128,],[2,2,31,31,31,31,31,31,31,31,31,]),'type':([3,12,20,40,],[5,13,13,76,]),'iden':([5,13,21,22,25,27,33,35,36,37,38,43,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,68,76,105,111,112,113,114,115,117,126,128,],[10,17,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,106,24,24,24,24,24,24,24,24,24,]),'flist':([12,20,],[14,23,]),'empty':([12,20,35,43,105,119,120,],[16,16,71,71,71,125,125,]),'body':([21,22,25,27,],[26,42,44,46,]),'stmt':([21,22,25,27,112,113,115,126,128,],[27,27,27,27,119,120,122,129,130,]),'expr':([21,22,25,27,33,35,36,37,38,43,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,68,105,111,112,113,114,115,117,126,128,],[28,28,28,28,67,72,73,74,75,72,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,72,118,28,28,121,28,123,28,28,]),'defvar':([21,22,25,27,112,113,115,126,128,],[29,29,29,29,29,29,29,29,29,]),'num':([21,22,25,27,33,35,36,37,38,43,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,68,105,111,112,113,114,115,117,126,128,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'clist':([35,43,105,],[69,78,116,]),'else_choice':([119,120,],[124,127,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> func','prog',1,'p_prog1','grammer.py',15),
  ('prog -> func prog','prog',2,'p_prog2','grammer.py',29),
  ('func -> DEF type iden LPAREN flist RPAREN LBRACE body RBRACE','func',9,'p_func','grammer.py',42),
  ('func -> DEF type iden LPAREN error RPAREN LBRACE body RBRACE','func',9,'p_func_error','grammer.py',55),
  ('body -> stmt','body',1,'p_body1','grammer.py',68),
  ('body -> stmt body','body',2,'p_body2','grammer.py',78),
  ('stmt -> expr SEMI_COLON','stmt',2,'p_stmt1','grammer.py',90),
  ('stmt -> defvar SEMI_COLON','stmt',2,'p_stmt2','grammer.py',101),
  ('stmt -> IF LPAREN expr RPAREN stmt else_choice','stmt',6,'p_stmt3','grammer.py',113),
  ('stmt -> IF LPAREN error RPAREN stmt else_choice','stmt',6,'p_stmt3_error','grammer.py',124),
  ('else_choice -> empty','else_choice',1,'p_else_choice1','grammer.py',138),
  ('else_choice -> ELSE stmt','else_choice',2,'p_else_choice2','grammer.py',148),
  ('stmt -> func','stmt',1,'p_stmt4','grammer.py',159),
  ('stmt -> FOR LPAREN expr TO expr RPAREN stmt','stmt',7,'p_stmt5','grammer.py',170),
  ('stmt -> RETURN expr SEMI_COLON','stmt',3,'p_stmt6','grammer.py',181),
  ('stmt -> LBRACE body RBRACE','stmt',3,'p_stmt7','grammer.py',191),
  ('stmt -> WHILE LPAREN expr RPAREN stmt','stmt',5,'p_stmt8','grammer.py',202),
  ('expr -> iden LPAREN clist RPAREN','expr',4,'p_expr1','grammer.py',215),
  ('expr -> iden LPAREN error RPAREN','expr',4,'p_expr1_error','grammer.py',226),
  ('expr -> expr LSQUAREBR expr RSQUAREBR','expr',4,'p_expr2','grammer.py',239),
  ('expr -> expr LSQUAREBR error RSQUAREBR','expr',4,'p_expr2_error','grammer.py',249),
  ('expr -> expr QMARK expr COLON expr','expr',5,'p_expr3','grammer.py',263),
  ('expr -> expr PARITY expr','expr',3,'p_expr4','grammer.py',273),
  ('expr -> expr NOT_EQ expr','expr',3,'p_expr4','grammer.py',274),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr4','grammer.py',275),
  ('expr -> expr TIMES expr','expr',3,'p_expr4','grammer.py',276),
  ('expr -> expr MINUS expr','expr',3,'p_expr4','grammer.py',277),
  ('expr -> expr PLUS expr','expr',3,'p_expr4','grammer.py',278),
  ('expr -> expr MOD expr','expr',3,'p_expr4','grammer.py',279),
  ('expr -> expr GREATER_EQUAL expr','expr',3,'p_expr4','grammer.py',280),
  ('expr -> expr LESS_EQUAL expr','expr',3,'p_expr4','grammer.py',281),
  ('expr -> expr GREATER_THAN expr','expr',3,'p_expr4','grammer.py',282),
  ('expr -> expr LESS_THAN expr','expr',3,'p_expr4','grammer.py',283),
  ('expr -> expr OR expr','expr',3,'p_expr4','grammer.py',284),
  ('expr -> expr AND expr','expr',3,'p_expr4','grammer.py',285),
  ('expr -> expr EQ expr','expr',3,'p_expr4','grammer.py',286),
  ('expr -> MINUS expr','expr',2,'p_expr5','grammer.py',296),
  ('expr -> PLUS expr','expr',2,'p_expr5','grammer.py',297),
  ('expr -> NOT expr','expr',2,'p_expr5','grammer.py',298),
  ('expr -> LSQUAREBR clist RSQUAREBR','expr',3,'p_expr6','grammer.py',308),
  ('expr -> LSQUAREBR error RSQUAREBR','expr',3,'p_expr6_error','grammer.py',318),
  ('expr -> iden','expr',1,'p_expr7','grammer.py',332),
  ('expr -> num','expr',1,'p_expr9','grammer.py',342),
  ('clist -> empty','clist',1,'p_clist1','grammer.py',367),
  ('clist -> expr','clist',1,'p_clist2','grammer.py',377),
  ('clist -> expr COMMA clist','clist',3,'p_clist3','grammer.py',387),
  ('defvar -> VAR type iden','defvar',3,'p_defvar1','grammer.py',400),
  ('defvar -> VAR type iden EQ expr','defvar',5,'p_defvar2','grammer.py',412),
  ('flist -> empty','flist',1,'p_flist1','grammer.py',423),
  ('flist -> type iden','flist',2,'p_flist2','grammer.py',433),
  ('flist -> type iden COMMA flist','flist',4,'p_flist3','grammer.py',443),
  ('iden -> IDEN','iden',1,'p_iden','grammer.py',455),
  ('type -> INT','type',1,'p_type','grammer.py',477),
  ('type -> VECTOR','type',1,'p_type','grammer.py',478),
  ('type -> STRING','type',1,'p_type','grammer.py',479),
  ('type -> NULL','type',1,'p_type','grammer.py',480),
  ('num -> NUM','num',1,'p_num','grammer.py',493),
  ('empty -> <empty>','empty',0,'p_empty','grammer.py',503),
]
