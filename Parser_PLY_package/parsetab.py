
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'lefterrorleftANDORleftNOTLESS_EQUALGREATER_EQUALNOT_EQPARITYLESS_THANGREATER_THANleftEQQMARKCOLONleftPLUSMINUSleftTIMESDIVIDEMODleftLPARENRPARENLBRACERBRACENUM COMMENT STR IDEN PLUS TIMES DIVIDE MOD MINUS LPAREN RPAREN LBRACE RBRACE LSQUAREBR RSQUAREBR COLON COMMA SEMI_COLON LESS_THAN LESS_EQUAL GREATER_THAN GREATER_EQUAL EQ NOT_EQ PARITY NOT QMARK FOR IF ELSE RETURN WHILE TO INT DEF VAR AND OR VECTOR NULLprog : funcprog : func progfunc : DEF type iden LPAREN flist RPAREN LBRACE body RBRACEfunc : DEF type iden LPAREN error RPAREN LBRACE body RBRACEbody : stmtbody : stmt bodystmt : expr SEMI_COLONstmt : defvar SEMI_COLONstmt : IF LPAREN expr RPAREN stmt else_choicestmt : IF LPAREN error RPAREN stmt else_choiceelse_choice : emptyelse_choice : ELSE stmtstmt : funcstmt : FOR LPAREN iden EQ expr TO expr RPAREN stmtstmt : RETURN expr SEMI_COLONstmt : LBRACE body RBRACEexpr : expr LSQUAREBR expr RSQUAREBRexpr : expr LSQUAREBR error RSQUAREBRexpr : iden LPAREN clist RPARENexpr : iden LPAREN error RPARENexpr : expr QMARK expr COLON exprexpr : expr PARITY expr \n                 | expr NOT_EQ expr \n                 | expr DIVIDE expr\n                 | expr TIMES expr\n                 | expr MINUS expr\n                 | expr PLUS expr\n                 | expr MOD expr \n                 | expr GREATER_EQUAL expr \n                 | expr LESS_EQUAL expr \n                 | expr GREATER_THAN expr\n                 | expr LESS_THAN expr\n                 | expr OR expr \n                 | expr AND expr \n                 | expr EQ exprexpr : MINUS expr \n                 | PLUS expr \n                 | NOT exprexpr : LSQUAREBR clist RSQUAREBRexpr : LSQUAREBR error RSQUAREBRexpr : idenexpr : numclist : emptyclist : exprclist : expr COMMA clistdefvar : VAR type idendefvar : VAR type iden EQ exprflist : emptyflist : type idenflist : type iden COMMA flistiden : IDENtype : INT\n                | VECTOR\n                | NULLnum : NUMempty :'
    
_lr_action_items = {'DEF':([0,2,20,21,24,26,30,43,45,62,74,77,98,108,109,114,115,118,119,120,121,123,125,126,],[3,3,3,3,3,3,-13,-3,-7,-8,-4,-16,-15,3,3,-56,-56,-9,-11,3,-10,-12,3,-14,]),'$end':([1,2,4,43,74,],[0,-1,-2,-3,-4,]),'INT':([3,11,19,38,],[6,6,6,6,]),'VECTOR':([3,11,19,38,],[7,7,7,7,]),'NULL':([3,11,19,38,],[8,8,8,8,]),'IDEN':([5,6,7,8,12,20,21,24,26,30,32,33,34,35,36,41,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,73,74,77,98,101,107,108,109,110,112,114,115,118,119,120,121,122,123,125,126,],[10,-52,-53,-54,10,10,10,10,10,-13,10,10,10,10,10,10,-3,-7,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-8,10,10,10,-4,-16,-15,10,10,10,10,10,10,-56,-56,-9,-11,10,-10,10,-12,10,-14,]),'LPAREN':([9,10,23,29,31,],[11,-51,41,63,64,]),'COMMA':([10,16,23,37,39,69,70,71,72,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,103,104,105,106,113,],[-51,19,-41,-42,-55,101,-36,-37,-38,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-39,-40,-19,-20,-17,-18,-21,]),'RPAREN':([10,11,13,14,15,16,19,22,23,37,39,41,68,69,70,71,72,75,76,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,103,104,105,106,111,113,124,],[-51,-56,17,18,-48,-49,-56,-50,-41,-42,-55,-56,-43,-44,-36,-37,-38,103,104,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,108,109,-39,-40,-56,-19,-20,-17,-18,-45,-21,125,]),'SEMI_COLON':([10,23,27,28,37,39,65,70,71,72,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,102,103,104,105,106,113,117,],[-51,-41,45,62,-42,-55,98,-36,-37,-38,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-39,-40,-46,-19,-20,-17,-18,-21,-47,]),'LSQUAREBR':([10,20,21,23,24,26,27,30,32,33,34,35,36,37,39,41,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,69,70,71,72,74,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,99,100,101,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,],[-51,33,33,-41,33,33,46,-13,33,33,33,33,33,-42,-55,33,-3,-7,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-8,33,46,46,-36,-37,-38,-4,-16,46,46,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,46,-15,-39,-40,33,-19,-20,-17,-18,33,33,33,33,33,-21,-56,-56,46,46,-9,-11,33,-10,33,-12,46,33,-14,]),'QMARK':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,47,-42,-55,47,47,-36,-37,47,47,47,47,47,-24,-25,-26,-27,-28,47,47,47,47,47,47,-35,47,-39,-40,-19,-20,-17,-18,-21,47,47,47,]),'PARITY':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,48,-42,-55,48,48,-36,-37,-38,48,48,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,48,48,-35,48,-39,-40,-19,-20,-17,-18,-21,48,48,48,]),'NOT_EQ':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,49,-42,-55,49,49,-36,-37,-38,49,49,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,49,49,-35,49,-39,-40,-19,-20,-17,-18,-21,49,49,49,]),'DIVIDE':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,50,-42,-55,50,50,50,50,50,50,50,50,50,-24,-25,50,50,-28,50,50,50,50,50,50,50,50,-39,-40,-19,-20,-17,-18,50,50,50,50,]),'TIMES':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,51,-42,-55,51,51,51,51,51,51,51,51,51,-24,-25,51,51,-28,51,51,51,51,51,51,51,51,-39,-40,-19,-20,-17,-18,51,51,51,51,]),'MINUS':([10,20,21,23,24,26,27,30,32,33,34,35,36,37,39,41,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,69,70,71,72,74,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,99,100,101,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,],[-51,34,34,-41,34,34,52,-13,34,34,34,34,34,-42,-55,34,-3,-7,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-8,34,52,52,-36,-37,52,-4,-16,52,52,52,52,-24,-25,-26,-27,-28,52,52,52,52,52,52,52,52,-15,-39,-40,34,-19,-20,-17,-18,34,34,34,34,34,52,-56,-56,52,52,-9,-11,34,-10,34,-12,52,34,-14,]),'PLUS':([10,20,21,23,24,26,27,30,32,33,34,35,36,37,39,41,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,69,70,71,72,74,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,99,100,101,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,],[-51,35,35,-41,35,35,53,-13,35,35,35,35,35,-42,-55,35,-3,-7,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-8,35,53,53,-36,-37,53,-4,-16,53,53,53,53,-24,-25,-26,-27,-28,53,53,53,53,53,53,53,53,-15,-39,-40,35,-19,-20,-17,-18,35,35,35,35,35,53,-56,-56,53,53,-9,-11,35,-10,35,-12,53,35,-14,]),'MOD':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,54,-42,-55,54,54,54,54,54,54,54,54,54,-24,-25,54,54,-28,54,54,54,54,54,54,54,54,-39,-40,-19,-20,-17,-18,54,54,54,54,]),'GREATER_EQUAL':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,55,-42,-55,55,55,-36,-37,-38,55,55,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,55,55,-35,55,-39,-40,-19,-20,-17,-18,-21,55,55,55,]),'LESS_EQUAL':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,56,-42,-55,56,56,-36,-37,-38,56,56,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,56,56,-35,56,-39,-40,-19,-20,-17,-18,-21,56,56,56,]),'GREATER_THAN':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,57,-42,-55,57,57,-36,-37,-38,57,57,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,57,57,-35,57,-39,-40,-19,-20,-17,-18,-21,57,57,57,]),'LESS_THAN':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,58,-42,-55,58,58,-36,-37,-38,58,58,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,58,58,-35,58,-39,-40,-19,-20,-17,-18,-21,58,58,58,]),'OR':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,59,-42,-55,59,59,-36,-37,-38,59,59,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,59,-39,-40,-19,-20,-17,-18,-21,59,59,59,]),'AND':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,103,104,105,106,113,116,117,124,],[-51,-41,60,-42,-55,60,60,-36,-37,-38,60,60,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,60,-39,-40,-19,-20,-17,-18,-21,60,60,60,]),'EQ':([10,23,27,37,39,65,69,70,71,72,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,99,100,102,103,104,105,106,113,116,117,124,],[-51,-41,61,-42,-55,61,61,-36,-37,61,61,61,61,61,-24,-25,-26,-27,-28,61,61,61,61,61,61,-35,61,110,-39,-40,112,-19,-20,-17,-18,-21,61,61,61,]),'RSQUAREBR':([10,23,33,37,39,66,67,68,69,70,71,72,78,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,101,103,104,105,106,111,113,],[-51,-41,-56,-42,-55,99,100,-43,-44,-36,-37,-38,105,106,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-39,-40,-56,-19,-20,-17,-18,-45,-21,]),'COLON':([10,23,37,39,70,71,72,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,103,104,105,106,113,],[-51,-41,-42,-55,-36,-37,-38,107,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-39,-40,-19,-20,-17,-18,-21,]),'TO':([10,23,37,39,70,71,72,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,103,104,105,106,113,116,],[-51,-41,-42,-55,-36,-37,-38,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-39,-40,-19,-20,-17,-18,-21,122,]),'error':([11,33,41,46,63,],[14,67,76,79,96,]),'LBRACE':([17,18,20,21,24,26,30,43,45,62,74,77,98,108,109,114,115,118,119,120,121,123,125,126,],[20,21,24,24,24,24,-13,-3,-7,-8,-4,-16,-15,24,24,-56,-56,-9,-11,24,-10,-12,24,-14,]),'IF':([20,21,24,26,30,43,45,62,74,77,98,108,109,114,115,118,119,120,121,123,125,126,],[29,29,29,29,-13,-3,-7,-8,-4,-16,-15,29,29,-56,-56,-9,-11,29,-10,-12,29,-14,]),'FOR':([20,21,24,26,30,43,45,62,74,77,98,108,109,114,115,118,119,120,121,123,125,126,],[31,31,31,31,-13,-3,-7,-8,-4,-16,-15,31,31,-56,-56,-9,-11,31,-10,-12,31,-14,]),'RETURN':([20,21,24,26,30,43,45,62,74,77,98,108,109,114,115,118,119,120,121,123,125,126,],[32,32,32,32,-13,-3,-7,-8,-4,-16,-15,32,32,-56,-56,-9,-11,32,-10,-12,32,-14,]),'NOT':([20,21,24,26,30,32,33,34,35,36,41,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,74,77,98,101,107,108,109,110,112,114,115,118,119,120,121,122,123,125,126,],[36,36,36,36,-13,36,36,36,36,36,36,-3,-7,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-8,36,-4,-16,-15,36,36,36,36,36,36,-56,-56,-9,-11,36,-10,36,-12,36,-14,]),'VAR':([20,21,24,26,30,43,45,62,74,77,98,108,109,114,115,118,119,120,121,123,125,126,],[38,38,38,38,-13,-3,-7,-8,-4,-16,-15,38,38,-56,-56,-9,-11,38,-10,-12,38,-14,]),'NUM':([20,21,24,26,30,32,33,34,35,36,41,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,74,77,98,101,107,108,109,110,112,114,115,118,119,120,121,122,123,125,126,],[39,39,39,39,-13,39,39,39,39,39,39,-3,-7,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-8,39,-4,-16,-15,39,39,39,39,39,39,-56,-56,-9,-11,39,-10,39,-12,39,-14,]),'RBRACE':([25,26,30,40,42,43,44,45,62,74,77,98,114,115,118,119,121,123,126,],[43,-5,-13,74,77,-3,-6,-7,-8,-4,-16,-15,-56,-56,-9,-11,-10,-12,-14,]),'ELSE':([30,43,45,62,74,77,98,114,115,118,119,121,123,126,],[-13,-3,-7,-8,-4,-16,-15,120,120,-9,-11,-10,-12,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,2,],[1,4,]),'func':([0,2,20,21,24,26,108,109,120,125,],[2,2,30,30,30,30,30,30,30,30,]),'type':([3,11,19,38,],[5,12,12,73,]),'iden':([5,12,20,21,24,26,32,33,34,35,36,41,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,73,101,107,108,109,110,112,120,122,125,],[9,16,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,97,102,23,23,23,23,23,23,23,23,23,]),'flist':([11,19,],[13,22,]),'empty':([11,19,33,41,101,114,115,],[15,15,68,68,68,119,119,]),'body':([20,21,24,26,],[25,40,42,44,]),'stmt':([20,21,24,26,108,109,120,125,],[26,26,26,26,114,115,123,126,]),'expr':([20,21,24,26,32,33,34,35,36,41,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,101,107,108,109,110,112,120,122,125,],[27,27,27,27,65,69,70,71,72,69,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,69,113,27,27,116,117,27,124,27,]),'defvar':([20,21,24,26,108,109,120,125,],[28,28,28,28,28,28,28,28,]),'num':([20,21,24,26,32,33,34,35,36,41,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,101,107,108,109,110,112,120,122,125,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'clist':([33,41,101,],[66,75,111,]),'else_choice':([114,115,],[118,121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> func','prog',1,'p_prog1','grammer.py',17),
  ('prog -> func prog','prog',2,'p_prog2','grammer.py',31),
  ('func -> DEF type iden LPAREN flist RPAREN LBRACE body RBRACE','func',9,'p_func','grammer.py',46),
  ('func -> DEF type iden LPAREN error RPAREN LBRACE body RBRACE','func',9,'p_func_error','grammer.py',59),
  ('body -> stmt','body',1,'p_body1','grammer.py',72),
  ('body -> stmt body','body',2,'p_body2','grammer.py',82),
  ('stmt -> expr SEMI_COLON','stmt',2,'p_stmt1','grammer.py',94),
  ('stmt -> defvar SEMI_COLON','stmt',2,'p_stmt2','grammer.py',105),
  ('stmt -> IF LPAREN expr RPAREN stmt else_choice','stmt',6,'p_stmt3','grammer.py',117),
  ('stmt -> IF LPAREN error RPAREN stmt else_choice','stmt',6,'p_stmt3_error','grammer.py',128),
  ('else_choice -> empty','else_choice',1,'p_else_choice1','grammer.py',142),
  ('else_choice -> ELSE stmt','else_choice',2,'p_else_choice2','grammer.py',152),
  ('stmt -> func','stmt',1,'p_stmt4','grammer.py',163),
  ('stmt -> FOR LPAREN iden EQ expr TO expr RPAREN stmt','stmt',9,'p_stmt5','grammer.py',174),
  ('stmt -> RETURN expr SEMI_COLON','stmt',3,'p_stmt6','grammer.py',185),
  ('stmt -> LBRACE body RBRACE','stmt',3,'p_stmt7','grammer.py',195),
  ('expr -> expr LSQUAREBR expr RSQUAREBR','expr',4,'p_expr1','grammer.py',217),
  ('expr -> expr LSQUAREBR error RSQUAREBR','expr',4,'p_expr1_error','grammer.py',228),
  ('expr -> iden LPAREN clist RPAREN','expr',4,'p_expr2','grammer.py',243),
  ('expr -> iden LPAREN error RPAREN','expr',4,'p_expr2_error','grammer.py',253),
  ('expr -> expr QMARK expr COLON expr','expr',5,'p_expr3','grammer.py',268),
  ('expr -> expr PARITY expr','expr',3,'p_expr4','grammer.py',278),
  ('expr -> expr NOT_EQ expr','expr',3,'p_expr4','grammer.py',279),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr4','grammer.py',280),
  ('expr -> expr TIMES expr','expr',3,'p_expr4','grammer.py',281),
  ('expr -> expr MINUS expr','expr',3,'p_expr4','grammer.py',282),
  ('expr -> expr PLUS expr','expr',3,'p_expr4','grammer.py',283),
  ('expr -> expr MOD expr','expr',3,'p_expr4','grammer.py',284),
  ('expr -> expr GREATER_EQUAL expr','expr',3,'p_expr4','grammer.py',285),
  ('expr -> expr LESS_EQUAL expr','expr',3,'p_expr4','grammer.py',286),
  ('expr -> expr GREATER_THAN expr','expr',3,'p_expr4','grammer.py',287),
  ('expr -> expr LESS_THAN expr','expr',3,'p_expr4','grammer.py',288),
  ('expr -> expr OR expr','expr',3,'p_expr4','grammer.py',289),
  ('expr -> expr AND expr','expr',3,'p_expr4','grammer.py',290),
  ('expr -> expr EQ expr','expr',3,'p_expr4','grammer.py',291),
  ('expr -> MINUS expr','expr',2,'p_expr5','grammer.py',301),
  ('expr -> PLUS expr','expr',2,'p_expr5','grammer.py',302),
  ('expr -> NOT expr','expr',2,'p_expr5','grammer.py',303),
  ('expr -> LSQUAREBR clist RSQUAREBR','expr',3,'p_expr6','grammer.py',313),
  ('expr -> LSQUAREBR error RSQUAREBR','expr',3,'p_expr6_error','grammer.py',323),
  ('expr -> iden','expr',1,'p_expr7','grammer.py',337),
  ('expr -> num','expr',1,'p_expr9','grammer.py',361),
  ('clist -> empty','clist',1,'p_clist1','grammer.py',374),
  ('clist -> expr','clist',1,'p_clist2','grammer.py',384),
  ('clist -> expr COMMA clist','clist',3,'p_clist3','grammer.py',394),
  ('defvar -> VAR type iden','defvar',3,'p_defvar1','grammer.py',407),
  ('defvar -> VAR type iden EQ expr','defvar',5,'p_defvar2','grammer.py',420),
  ('flist -> empty','flist',1,'p_flist1','grammer.py',432),
  ('flist -> type iden','flist',2,'p_flist2','grammer.py',442),
  ('flist -> type iden COMMA flist','flist',4,'p_flist3','grammer.py',452),
  ('iden -> IDEN','iden',1,'p_iden','grammer.py',464),
  ('type -> INT','type',1,'p_type','grammer.py',476),
  ('type -> VECTOR','type',1,'p_type','grammer.py',477),
  ('type -> NULL','type',1,'p_type','grammer.py',478),
  ('num -> NUM','num',1,'p_num','grammer.py',490),
  ('empty -> <empty>','empty',0,'p_empty','grammer.py',500),
]
