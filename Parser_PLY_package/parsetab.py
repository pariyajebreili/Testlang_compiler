
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'lefterrorleftANDORleftNOTLESS_EQUALGREATER_EQUALNOT_EQPARITYLESS_THANGREATER_THANleftEQQMARKCOLONleftPLUSMINUSleftTIMESDIVIDEMODleftLPARENRPARENLBRACERBRACENUM COMMENT STR IDEN PLUS TIMES DIVIDE MOD MINUS LPAREN RPAREN LBRACE RBRACE LSQUAREBR RSQUAREBR COLON COMMA SEMI_COLON LESS_THAN LESS_EQUAL GREATER_THAN GREATER_EQUAL EQ NOT_EQ PARITY NOT QMARK VOID FOR IF ELSE RETURN WHILE TO IN INT DEF VAR AND OR TRUE FALSE VECTOR NULLprog : funcprog : func progfunc : DEF type iden LPAREN flist RPAREN LBRACE body RBRACEfunc : DEF type iden LPAREN error RPAREN LBRACE body RBRACEbody : stmtbody : stmt bodystmt : expr SEMI_COLONstmt : defvar SEMI_COLONstmt : IF LPAREN expr RPAREN stmt else_choicestmt : IF LPAREN error RPAREN stmt else_choiceelse_choice : emptyelse_choice : ELSE stmtstmt : RETURN expr SEMI_COLONstmt : LBRACE body RBRACEexpr : expr LSQUAREBR expr RSQUAREBRexpr : expr LSQUAREBR error RSQUAREBRexpr : iden LPAREN clist RPARENexpr : iden LPAREN error RPARENexpr : expr QMARK expr COLON exprexpr : expr PARITY expr \n                 | expr NOT_EQ expr \n                 | expr DIVIDE expr\n                 | expr TIMES expr\n                 | expr MINUS expr\n                 | expr PLUS expr\n                 | expr MOD expr \n                 | expr GREATER_EQUAL expr \n                 | expr LESS_EQUAL expr \n                 | expr GREATER_THAN expr\n                 | expr LESS_THAN expr\n                 | expr OR expr \n                 | expr AND expr \n                 | expr EQ exprexpr : MINUS expr \n                 | PLUS expr \n                 | NOT exprexpr : LSQUAREBR clist RSQUAREBRexpr : LSQUAREBR error RSQUAREBRexpr : idenexpr : iden EQ exprexpr : numclist : emptyclist : exprclist : expr COMMA clistdefvar : VAR type idendefvar : VAR type iden EQ exprflist : emptyflist : type idenflist : type iden COMMA flistiden : IDENtype : INT\n                | VECTOR\n                | NULLnum : NUMempty :'
    
_lr_action_items = {'DEF':([0,2,42,72,],[3,3,-3,-4,]),'$end':([1,2,4,42,72,],[0,-1,-2,-3,-4,]),'INT':([3,11,19,36,],[6,6,6,6,]),'VECTOR':([3,11,19,36,],[7,7,7,7,]),'NULL':([3,11,19,36,],[8,8,8,8,]),'IDEN':([5,6,7,8,12,20,21,24,26,30,31,32,33,34,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,71,76,96,99,105,106,107,109,111,112,114,115,116,117,118,],[10,-51,-52,-53,10,10,10,10,10,10,10,10,10,10,10,10,-7,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-8,10,10,-14,-13,10,10,10,10,10,-55,-55,-9,-11,10,-10,-12,]),'LPAREN':([9,10,23,29,],[11,-50,39,62,]),'COMMA':([10,16,23,35,37,67,68,69,70,75,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,98,101,102,103,104,110,],[-50,19,-39,-41,-54,99,-34,-35,-36,-40,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-38,-17,-18,-15,-16,-19,]),'RPAREN':([10,11,13,14,15,16,19,22,23,35,37,39,66,67,68,69,70,73,74,75,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,101,102,103,104,108,110,],[-50,-55,17,18,-47,-48,-55,-49,-39,-41,-54,-55,-42,-43,-34,-35,-36,101,102,-40,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,106,107,-37,-38,-55,-17,-18,-15,-16,-44,-19,]),'EQ':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,100,101,102,103,104,110,113,],[-50,40,60,-41,-54,60,60,-34,-35,60,-40,60,60,60,60,-22,-23,-24,-25,-26,60,60,60,60,60,60,-33,60,-37,-38,109,-17,-18,-15,-16,-19,60,]),'SEMI_COLON':([10,23,27,28,35,37,63,68,69,70,75,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,98,100,101,102,103,104,110,113,],[-50,-39,44,61,-41,-54,96,-34,-35,-36,-40,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-38,-45,-17,-18,-15,-16,-19,-46,]),'LSQUAREBR':([10,20,21,23,24,26,27,30,31,32,33,34,35,37,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,68,69,70,75,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,101,102,103,104,105,106,107,109,110,111,112,113,114,115,116,117,118,],[-50,31,31,-39,31,31,45,31,31,31,31,31,-41,-54,31,31,-7,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-8,31,45,45,-34,-35,-36,-40,-14,45,45,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,45,-13,-37,-38,31,-17,-18,-15,-16,31,31,31,31,-19,-55,-55,45,-9,-11,31,-10,-12,]),'QMARK':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,46,-41,-54,46,46,-34,-35,46,-40,46,46,46,46,-22,-23,-24,-25,-26,46,46,46,46,46,46,-33,46,-37,-38,-17,-18,-15,-16,-19,46,]),'PARITY':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,47,-41,-54,47,47,-34,-35,-36,-40,47,47,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,47,47,-33,47,-37,-38,-17,-18,-15,-16,-19,47,]),'NOT_EQ':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,48,-41,-54,48,48,-34,-35,-36,-40,48,48,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,48,48,-33,48,-37,-38,-17,-18,-15,-16,-19,48,]),'DIVIDE':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,49,-41,-54,49,49,49,49,49,49,49,49,49,49,-22,-23,49,49,-26,49,49,49,49,49,49,49,49,-37,-38,-17,-18,-15,-16,49,49,]),'TIMES':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,50,-41,-54,50,50,50,50,50,50,50,50,50,50,-22,-23,50,50,-26,50,50,50,50,50,50,50,50,-37,-38,-17,-18,-15,-16,50,50,]),'MINUS':([10,20,21,23,24,26,27,30,31,32,33,34,35,37,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,68,69,70,75,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,101,102,103,104,105,106,107,109,110,111,112,113,114,115,116,117,118,],[-50,32,32,-39,32,32,51,32,32,32,32,32,-41,-54,32,32,-7,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-8,32,51,51,-34,-35,51,51,-14,51,51,51,51,-22,-23,-24,-25,-26,51,51,51,51,51,51,51,51,-13,-37,-38,32,-17,-18,-15,-16,32,32,32,32,51,-55,-55,51,-9,-11,32,-10,-12,]),'PLUS':([10,20,21,23,24,26,27,30,31,32,33,34,35,37,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,68,69,70,75,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,101,102,103,104,105,106,107,109,110,111,112,113,114,115,116,117,118,],[-50,33,33,-39,33,33,52,33,33,33,33,33,-41,-54,33,33,-7,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-8,33,52,52,-34,-35,52,52,-14,52,52,52,52,-22,-23,-24,-25,-26,52,52,52,52,52,52,52,52,-13,-37,-38,33,-17,-18,-15,-16,33,33,33,33,52,-55,-55,52,-9,-11,33,-10,-12,]),'MOD':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,53,-41,-54,53,53,53,53,53,53,53,53,53,53,-22,-23,53,53,-26,53,53,53,53,53,53,53,53,-37,-38,-17,-18,-15,-16,53,53,]),'GREATER_EQUAL':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,54,-41,-54,54,54,-34,-35,-36,-40,54,54,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,54,54,-33,54,-37,-38,-17,-18,-15,-16,-19,54,]),'LESS_EQUAL':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,55,-41,-54,55,55,-34,-35,-36,-40,55,55,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,55,55,-33,55,-37,-38,-17,-18,-15,-16,-19,55,]),'GREATER_THAN':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,56,-41,-54,56,56,-34,-35,-36,-40,56,56,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,56,56,-33,56,-37,-38,-17,-18,-15,-16,-19,56,]),'LESS_THAN':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,57,-41,-54,57,57,-34,-35,-36,-40,57,57,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,57,57,-33,57,-37,-38,-17,-18,-15,-16,-19,57,]),'OR':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,58,-41,-54,58,58,-34,-35,-36,-40,58,58,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,58,-37,-38,-17,-18,-15,-16,-19,58,]),'AND':([10,23,27,35,37,63,67,68,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,101,102,103,104,110,113,],[-50,-39,59,-41,-54,59,59,-34,-35,-36,-40,59,59,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,59,-37,-38,-17,-18,-15,-16,-19,59,]),'RSQUAREBR':([10,23,31,35,37,64,65,66,67,68,69,70,75,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,98,99,101,102,103,104,108,110,],[-50,-39,-55,-41,-54,97,98,-42,-43,-34,-35,-36,-40,103,104,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-38,-55,-17,-18,-15,-16,-44,-19,]),'COLON':([10,23,35,37,68,69,70,75,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,98,101,102,103,104,110,],[-50,-39,-41,-54,-34,-35,-36,-40,105,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-38,-17,-18,-15,-16,-19,]),'error':([11,31,39,45,62,],[14,65,74,78,95,]),'LBRACE':([17,18,20,21,24,26,44,61,76,96,106,107,111,112,114,115,116,117,118,],[20,21,24,24,24,24,-7,-8,-14,-13,24,24,-55,-55,-9,-11,24,-10,-12,]),'IF':([20,21,24,26,44,61,76,96,106,107,111,112,114,115,116,117,118,],[29,29,29,29,-7,-8,-14,-13,29,29,-55,-55,-9,-11,29,-10,-12,]),'RETURN':([20,21,24,26,44,61,76,96,106,107,111,112,114,115,116,117,118,],[30,30,30,30,-7,-8,-14,-13,30,30,-55,-55,-9,-11,30,-10,-12,]),'NOT':([20,21,24,26,30,31,32,33,34,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,76,96,99,105,106,107,109,111,112,114,115,116,117,118,],[34,34,34,34,34,34,34,34,34,34,34,-7,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-8,34,-14,-13,34,34,34,34,34,-55,-55,-9,-11,34,-10,-12,]),'VAR':([20,21,24,26,44,61,76,96,106,107,111,112,114,115,116,117,118,],[36,36,36,36,-7,-8,-14,-13,36,36,-55,-55,-9,-11,36,-10,-12,]),'NUM':([20,21,24,26,30,31,32,33,34,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,76,96,99,105,106,107,109,111,112,114,115,116,117,118,],[37,37,37,37,37,37,37,37,37,37,37,-7,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-8,37,-14,-13,37,37,37,37,37,-55,-55,-9,-11,37,-10,-12,]),'RBRACE':([25,26,38,41,43,44,61,76,96,111,112,114,115,117,118,],[42,-5,72,76,-6,-7,-8,-14,-13,-55,-55,-9,-11,-10,-12,]),'ELSE':([44,61,76,96,111,112,114,115,117,118,],[-7,-8,-14,-13,116,116,-9,-11,-10,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,2,],[1,4,]),'func':([0,2,],[2,2,]),'type':([3,11,19,36,],[5,12,12,71,]),'iden':([5,12,20,21,24,26,30,31,32,33,34,39,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,71,99,105,106,107,109,116,],[9,16,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,100,23,23,23,23,23,23,]),'flist':([11,19,],[13,22,]),'empty':([11,19,31,39,99,111,112,],[15,15,66,66,66,115,115,]),'body':([20,21,24,26,],[25,38,41,43,]),'stmt':([20,21,24,26,106,107,116,],[26,26,26,26,111,112,118,]),'expr':([20,21,24,26,30,31,32,33,34,39,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,99,105,106,107,109,116,],[27,27,27,27,63,67,68,69,70,67,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,67,110,27,27,113,27,]),'defvar':([20,21,24,26,106,107,116,],[28,28,28,28,28,28,28,]),'num':([20,21,24,26,30,31,32,33,34,39,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,99,105,106,107,109,116,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'clist':([31,39,99,],[64,73,108,]),'else_choice':([111,112,],[114,117,]),}

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
  ('stmt -> RETURN expr SEMI_COLON','stmt',3,'p_stmt6','grammer.py',164),
  ('stmt -> LBRACE body RBRACE','stmt',3,'p_stmt7','grammer.py',174),
  ('expr -> expr LSQUAREBR expr RSQUAREBR','expr',4,'p_expr1','grammer.py',187),
  ('expr -> expr LSQUAREBR error RSQUAREBR','expr',4,'p_expr1_error','grammer.py',198),
  ('expr -> iden LPAREN clist RPAREN','expr',4,'p_expr2','grammer.py',213),
  ('expr -> iden LPAREN error RPAREN','expr',4,'p_expr2_error','grammer.py',223),
  ('expr -> expr QMARK expr COLON expr','expr',5,'p_expr3','grammer.py',238),
  ('expr -> expr PARITY expr','expr',3,'p_expr4','grammer.py',248),
  ('expr -> expr NOT_EQ expr','expr',3,'p_expr4','grammer.py',249),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr4','grammer.py',250),
  ('expr -> expr TIMES expr','expr',3,'p_expr4','grammer.py',251),
  ('expr -> expr MINUS expr','expr',3,'p_expr4','grammer.py',252),
  ('expr -> expr PLUS expr','expr',3,'p_expr4','grammer.py',253),
  ('expr -> expr MOD expr','expr',3,'p_expr4','grammer.py',254),
  ('expr -> expr GREATER_EQUAL expr','expr',3,'p_expr4','grammer.py',255),
  ('expr -> expr LESS_EQUAL expr','expr',3,'p_expr4','grammer.py',256),
  ('expr -> expr GREATER_THAN expr','expr',3,'p_expr4','grammer.py',257),
  ('expr -> expr LESS_THAN expr','expr',3,'p_expr4','grammer.py',258),
  ('expr -> expr OR expr','expr',3,'p_expr4','grammer.py',259),
  ('expr -> expr AND expr','expr',3,'p_expr4','grammer.py',260),
  ('expr -> expr EQ expr','expr',3,'p_expr4','grammer.py',261),
  ('expr -> MINUS expr','expr',2,'p_expr5','grammer.py',271),
  ('expr -> PLUS expr','expr',2,'p_expr5','grammer.py',272),
  ('expr -> NOT expr','expr',2,'p_expr5','grammer.py',273),
  ('expr -> LSQUAREBR clist RSQUAREBR','expr',3,'p_expr6','grammer.py',283),
  ('expr -> LSQUAREBR error RSQUAREBR','expr',3,'p_expr6_error','grammer.py',293),
  ('expr -> iden','expr',1,'p_expr7','grammer.py',307),
  ('expr -> iden EQ expr','expr',3,'p_expr8','grammer.py',319),
  ('expr -> num','expr',1,'p_expr9','grammer.py',331),
  ('clist -> empty','clist',1,'p_clist1','grammer.py',344),
  ('clist -> expr','clist',1,'p_clist2','grammer.py',354),
  ('clist -> expr COMMA clist','clist',3,'p_clist3','grammer.py',364),
  ('defvar -> VAR type iden','defvar',3,'p_defvar1','grammer.py',377),
  ('defvar -> VAR type iden EQ expr','defvar',5,'p_defvar2','grammer.py',390),
  ('flist -> empty','flist',1,'p_flist1','grammer.py',402),
  ('flist -> type iden','flist',2,'p_flist2','grammer.py',412),
  ('flist -> type iden COMMA flist','flist',4,'p_flist3','grammer.py',422),
  ('iden -> IDEN','iden',1,'p_iden','grammer.py',434),
  ('type -> INT','type',1,'p_type','grammer.py',446),
  ('type -> VECTOR','type',1,'p_type','grammer.py',447),
  ('type -> NULL','type',1,'p_type','grammer.py',448),
  ('num -> NUM','num',1,'p_num','grammer.py',460),
  ('empty -> <empty>','empty',0,'p_empty','grammer.py',470),
]
