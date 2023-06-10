
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'lefterrorleftANDORleftNOTLESS_EQUALGREATER_EQUALNOT_EQPARITYLESS_THANGREATER_THANleftEQQMARKCOLONleftPLUSMINUSleftTIMESDIVIDEMODleftLPARENRPARENLBRACERBRACENUM IDEN STRING PLUS TIMES DIVIDE MOD MINUS LPAREN RPAREN LBRACE RBRACE LSQUAREBR RSQUAREBR COLON COMMA SEMI_COLON LESS_THAN LESS_EQUAL GREATER_THAN GREATER_EQUAL EQ NOT_EQ PARITY NOT QMARK FOR IF ELSE RETURN WHILE TO INT DEF VAR AND OR VECTOR NULL\n    prog : func\n    \n    prog : func prog\n    func : DEF type iden LPAREN flist RPAREN LBRACE body RBRACE\n    body : stmt \n         | stmt body\n    \n    stmt : expr SEMI_COLON\n         | defvar SEMI_COLON\n         | IF LPAREN expr RPAREN stmt\n         | IF LPAREN expr RPAREN stmt ELSE stmt\n         | WHILE LPAREN expr RPAREN stmt\n         | FOR LPAREN expr TO expr RPAREN stmt\n         | RETURN expr SEMI_COLON\n         | LBRACE body RBRACE\n    \n    expr : iden LPAREN clist RPAREN\n         | expr LSQUAREBR expr RSQUAREBR\n         | expr EQ expr\n         | expr PLUS expr\n         | expr MINUS expr\n         | expr TIMES expr\n         | expr DIVIDE expr\n         | expr MOD expr\n         | expr LESS_THAN expr\n         | expr GREATER_THAN expr\n         | expr PARITY expr\n         | expr NOT_EQ expr\n         | expr LESS_EQUAL expr\n         | expr GREATER_EQUAL expr\n         | expr OR expr\n         | expr AND expr\n         | NOT expr\n         | MINUS expr\n         | PLUS expr\n         | LPAREN expr RPAREN\n         | iden\n         | num\n    \n    flist : type iden\n          | type iden COMMA flist\n          |\n    \n    clist : expr \n          | expr COMMA clist\n          |\n    defvar : VAR type iden EQ expr\n    type : INT \n         | VECTOR\n         | NULL\n    \n    num : NUM\n    \n    iden : IDEN\n    '
    
_lr_action_items = {'DEF':([0,2,39,],[3,3,-3,]),'$end':([1,2,4,39,],[0,-1,-2,-3,]),'INT':([3,11,16,34,],[6,6,6,6,]),'VECTOR':([3,11,16,34,],[7,7,7,7,]),'NULL':([3,11,16,34,],[8,8,8,8,]),'IDEN':([5,6,7,8,12,17,20,21,23,29,30,31,32,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,69,88,91,93,94,95,96,98,99,102,103,104,105,],[10,-43,-44,-45,10,10,10,10,10,10,10,10,10,10,-6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-7,10,10,10,10,-13,-12,10,10,10,10,10,-8,-10,10,10,-9,-11,]),'LPAREN':([9,10,17,19,20,21,23,26,27,28,29,30,31,32,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,69,88,91,93,94,95,96,98,99,102,103,104,105,],[11,-47,20,36,20,20,20,58,59,60,20,20,20,20,20,-6,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-7,20,20,20,-13,-12,20,20,20,20,20,-8,-10,20,20,-9,-11,]),'COMMA':([10,14,19,33,35,62,63,64,67,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,90,92,],[-47,16,-34,-35,-46,-32,-31,-30,91,-33,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-14,-15,]),'RPAREN':([10,11,13,14,16,18,19,33,35,36,37,62,63,64,66,67,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,97,100,],[-47,-38,15,-36,-38,-37,-34,-35,-46,-41,68,-32,-31,-30,90,-39,-33,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,93,94,-14,-41,-15,-40,103,]),'SEMI_COLON':([10,19,24,25,33,35,61,62,63,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,90,92,101,],[-47,-34,41,57,-35,-46,88,-32,-31,-30,-33,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-14,-15,-42,]),'LSQUAREBR':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,42,-35,-46,42,42,-32,-31,-30,42,-33,42,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,42,42,42,-14,-15,42,42,]),'EQ':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,92,100,101,],[-47,-34,43,-35,-46,43,43,-32,-31,43,43,-33,43,-16,-17,-18,-19,-20,-21,43,43,43,43,43,43,43,43,43,43,43,96,-14,-15,43,43,]),'PLUS':([10,17,19,20,21,23,24,29,30,31,32,33,35,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,93,94,95,96,98,99,100,101,102,103,104,105,],[-47,30,-34,30,30,30,44,30,30,30,30,-35,-46,30,44,-6,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-7,30,30,30,44,-32,-31,44,44,-33,-13,44,44,-17,-18,-19,-20,-21,44,44,44,44,44,44,44,44,44,44,44,-12,-14,30,-15,30,30,30,30,-8,-10,44,44,30,30,-9,-11,]),'MINUS':([10,17,19,20,21,23,24,29,30,31,32,33,35,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,93,94,95,96,98,99,100,101,102,103,104,105,],[-47,31,-34,31,31,31,45,31,31,31,31,-35,-46,31,45,-6,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-7,31,31,31,45,-32,-31,45,45,-33,-13,45,45,-17,-18,-19,-20,-21,45,45,45,45,45,45,45,45,45,45,45,-12,-14,31,-15,31,31,31,31,-8,-10,45,45,31,31,-9,-11,]),'TIMES':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,46,-35,-46,46,46,46,46,46,46,-33,46,46,46,46,-19,-20,-21,46,46,46,46,46,46,46,46,46,46,46,-14,-15,46,46,]),'DIVIDE':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,47,-35,-46,47,47,47,47,47,47,-33,47,47,47,47,-19,-20,-21,47,47,47,47,47,47,47,47,47,47,47,-14,-15,47,47,]),'MOD':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,48,-35,-46,48,48,48,48,48,48,-33,48,48,48,48,-19,-20,-21,48,48,48,48,48,48,48,48,48,48,48,-14,-15,48,48,]),'LESS_THAN':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,49,-35,-46,49,49,-32,-31,-30,49,-33,49,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,49,49,49,49,49,-14,-15,49,49,]),'GREATER_THAN':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,50,-35,-46,50,50,-32,-31,-30,50,-33,50,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,50,50,50,50,50,-14,-15,50,50,]),'PARITY':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,51,-35,-46,51,51,-32,-31,-30,51,-33,51,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,51,51,51,51,51,-14,-15,51,51,]),'NOT_EQ':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,52,-35,-46,52,52,-32,-31,-30,52,-33,52,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,52,52,52,52,52,-14,-15,52,52,]),'LESS_EQUAL':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,53,-35,-46,53,53,-32,-31,-30,53,-33,53,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,53,53,53,53,53,-14,-15,53,53,]),'GREATER_EQUAL':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,54,-35,-46,54,54,-32,-31,-30,54,-33,54,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,54,54,54,54,54,-14,-15,54,54,]),'OR':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,55,-35,-46,55,55,-32,-31,-30,55,-33,55,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,55,55,55,-14,-15,55,55,]),'AND':([10,19,24,33,35,37,61,62,63,64,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,92,100,101,],[-47,-34,56,-35,-46,56,56,-32,-31,-30,56,-33,56,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,56,56,56,-14,-15,56,56,]),'RSQUAREBR':([10,19,33,35,62,63,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,90,92,],[-47,-34,-35,-46,-32,-31,-30,-33,92,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-14,-15,]),'TO':([10,19,33,35,62,63,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,90,92,],[-47,-34,-35,-46,-32,-31,-30,-33,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,95,-14,-15,]),'LBRACE':([15,17,21,23,41,57,69,88,93,94,98,99,102,103,104,105,],[17,21,21,21,-6,-7,-13,-12,21,21,-8,-10,21,21,-9,-11,]),'IF':([17,21,23,41,57,69,88,93,94,98,99,102,103,104,105,],[26,26,26,-6,-7,-13,-12,26,26,-8,-10,26,26,-9,-11,]),'WHILE':([17,21,23,41,57,69,88,93,94,98,99,102,103,104,105,],[27,27,27,-6,-7,-13,-12,27,27,-8,-10,27,27,-9,-11,]),'FOR':([17,21,23,41,57,69,88,93,94,98,99,102,103,104,105,],[28,28,28,-6,-7,-13,-12,28,28,-8,-10,28,28,-9,-11,]),'RETURN':([17,21,23,41,57,69,88,93,94,98,99,102,103,104,105,],[29,29,29,-6,-7,-13,-12,29,29,-8,-10,29,29,-9,-11,]),'NOT':([17,20,21,23,29,30,31,32,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,69,88,91,93,94,95,96,98,99,102,103,104,105,],[32,32,32,32,32,32,32,32,32,-6,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-7,32,32,32,-13,-12,32,32,32,32,32,-8,-10,32,32,-9,-11,]),'VAR':([17,21,23,41,57,69,88,93,94,98,99,102,103,104,105,],[34,34,34,-6,-7,-13,-12,34,34,-8,-10,34,34,-9,-11,]),'NUM':([17,20,21,23,29,30,31,32,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,69,88,91,93,94,95,96,98,99,102,103,104,105,],[35,35,35,35,35,35,35,35,35,-6,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-7,35,35,35,-13,-12,35,35,35,35,35,-8,-10,35,35,-9,-11,]),'RBRACE':([22,23,38,40,41,57,69,88,98,99,104,105,],[39,-4,69,-5,-6,-7,-13,-12,-8,-10,-9,-11,]),'ELSE':([41,57,69,88,98,99,104,105,],[-6,-7,-13,-12,-8,-10,-9,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,2,],[1,4,]),'func':([0,2,],[2,2,]),'type':([3,11,16,34,],[5,12,12,65,]),'iden':([5,12,17,20,21,23,29,30,31,32,36,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,65,91,93,94,95,96,102,103,],[9,14,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,89,19,19,19,19,19,19,19,]),'flist':([11,16,],[13,18,]),'body':([17,21,23,],[22,38,40,]),'stmt':([17,21,23,93,94,102,103,],[23,23,23,98,99,104,105,]),'expr':([17,20,21,23,29,30,31,32,36,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,91,93,94,95,96,102,103,],[24,37,24,24,61,62,63,64,67,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,67,24,24,100,101,24,24,]),'defvar':([17,21,23,93,94,102,103,],[25,25,25,25,25,25,25,]),'num':([17,20,21,23,29,30,31,32,36,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,91,93,94,95,96,102,103,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'clist':([36,91,],[66,97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> func','prog',1,'p_program_single','middle_code_generator.py',165),
  ('prog -> func prog','prog',2,'p_program_multiple','middle_code_generator.py',172),
  ('func -> DEF type iden LPAREN flist RPAREN LBRACE body RBRACE','func',9,'p_function','middle_code_generator.py',179),
  ('body -> stmt','body',1,'p_body_function','middle_code_generator.py',257),
  ('body -> stmt body','body',2,'p_body_function','middle_code_generator.py',258),
  ('stmt -> expr SEMI_COLON','stmt',2,'p_statement','middle_code_generator.py',271),
  ('stmt -> defvar SEMI_COLON','stmt',2,'p_statement','middle_code_generator.py',272),
  ('stmt -> IF LPAREN expr RPAREN stmt','stmt',5,'p_statement','middle_code_generator.py',273),
  ('stmt -> IF LPAREN expr RPAREN stmt ELSE stmt','stmt',7,'p_statement','middle_code_generator.py',274),
  ('stmt -> WHILE LPAREN expr RPAREN stmt','stmt',5,'p_statement','middle_code_generator.py',275),
  ('stmt -> FOR LPAREN expr TO expr RPAREN stmt','stmt',7,'p_statement','middle_code_generator.py',276),
  ('stmt -> RETURN expr SEMI_COLON','stmt',3,'p_statement','middle_code_generator.py',277),
  ('stmt -> LBRACE body RBRACE','stmt',3,'p_statement','middle_code_generator.py',278),
  ('expr -> iden LPAREN clist RPAREN','expr',4,'p_define_expression','middle_code_generator.py',475),
  ('expr -> expr LSQUAREBR expr RSQUAREBR','expr',4,'p_define_expression','middle_code_generator.py',476),
  ('expr -> expr EQ expr','expr',3,'p_define_expression','middle_code_generator.py',477),
  ('expr -> expr PLUS expr','expr',3,'p_define_expression','middle_code_generator.py',478),
  ('expr -> expr MINUS expr','expr',3,'p_define_expression','middle_code_generator.py',479),
  ('expr -> expr TIMES expr','expr',3,'p_define_expression','middle_code_generator.py',480),
  ('expr -> expr DIVIDE expr','expr',3,'p_define_expression','middle_code_generator.py',481),
  ('expr -> expr MOD expr','expr',3,'p_define_expression','middle_code_generator.py',482),
  ('expr -> expr LESS_THAN expr','expr',3,'p_define_expression','middle_code_generator.py',483),
  ('expr -> expr GREATER_THAN expr','expr',3,'p_define_expression','middle_code_generator.py',484),
  ('expr -> expr PARITY expr','expr',3,'p_define_expression','middle_code_generator.py',485),
  ('expr -> expr NOT_EQ expr','expr',3,'p_define_expression','middle_code_generator.py',486),
  ('expr -> expr LESS_EQUAL expr','expr',3,'p_define_expression','middle_code_generator.py',487),
  ('expr -> expr GREATER_EQUAL expr','expr',3,'p_define_expression','middle_code_generator.py',488),
  ('expr -> expr OR expr','expr',3,'p_define_expression','middle_code_generator.py',489),
  ('expr -> expr AND expr','expr',3,'p_define_expression','middle_code_generator.py',490),
  ('expr -> NOT expr','expr',2,'p_define_expression','middle_code_generator.py',491),
  ('expr -> MINUS expr','expr',2,'p_define_expression','middle_code_generator.py',492),
  ('expr -> PLUS expr','expr',2,'p_define_expression','middle_code_generator.py',493),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_define_expression','middle_code_generator.py',494),
  ('expr -> iden','expr',1,'p_define_expression','middle_code_generator.py',495),
  ('expr -> num','expr',1,'p_define_expression','middle_code_generator.py',496),
  ('flist -> type iden','flist',2,'p_variable_multiple','middle_code_generator.py',862),
  ('flist -> type iden COMMA flist','flist',4,'p_variable_multiple','middle_code_generator.py',863),
  ('flist -> <empty>','flist',0,'p_variable_multiple','middle_code_generator.py',864),
  ('clist -> expr','clist',1,'p_variable_array','middle_code_generator.py',887),
  ('clist -> expr COMMA clist','clist',3,'p_variable_array','middle_code_generator.py',888),
  ('clist -> <empty>','clist',0,'p_variable_array','middle_code_generator.py',889),
  ('defvar -> VAR type iden EQ expr','defvar',5,'p_define_variable','middle_code_generator.py',916),
  ('type -> INT','type',1,'p_variabel_type','middle_code_generator.py',933),
  ('type -> VECTOR','type',1,'p_variabel_type','middle_code_generator.py',934),
  ('type -> NULL','type',1,'p_variabel_type','middle_code_generator.py',935),
  ('num -> NUM','num',1,'p_expr_num','middle_code_generator.py',942),
  ('iden -> IDEN','iden',1,'p_expr_iden','middle_code_generator.py',949),
]
