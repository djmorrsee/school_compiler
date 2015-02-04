reserved = {
	'print' : 'PRINT',
}
tokens = 	['INT', 'PLUS', 'NEGATE', 'ASSIGNMENT', 'NAME', 
			 'LPARAN', 'RPARAN', 'INPUT'] + list(reserved.values())

t_PLUS = r'\+'
t_ASSIGNMENT = r'\='
t_NEGATE = r'\-'
t_LPARAN = r'\('
t_RPARAN = r'\)'

def t_INPUT(t):
	r'input'
	return t

def t_NAME(t):
	r'[a-zA-Z_]+[a-zA-Z\d]*'
	t.type = reserved.get(t.value, 'NAME')
	return t

def t_INT(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except:
		print "int too large", t.value
		t.value = 0
	return t
	
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")
	
def t_error(t):
	print "Illegal Character '%s'" % t.value[0]
	t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

## Parser
from compiler.ast import *
from compiler.ast import Printnl, Add, Const, Name, UnarySub
from compiler.ast import CallFunc, Discard, AssName, Assign, Stmt
from pprint import pprint
import itertools

precedence = (
	('nonassoc', 'PRINT', 'NAME'),
	('right', 'PLUS', 'ASSIGNMENT'),
	('left', 'NEGATE'),
	)
	
def p_statement_recursion(t):
	'''simple_statements : simple_statement 
						 | simple_statement simple_statements'''
	if not t[0]:
		t[0] = []
	for i in t[1:]:
		t[0].append(i)	
		
	## Hacky Flattening Cuz Weird Recursion
	tmp = []
	for i in t[0]:
		if iter(i) and not isinstance(i, Node):
			for j in i:
				tmp.append(j)
		else:
			tmp.append(i)
	t[0] = tmp	
		
def p_simple_statement(t):
	'''simple_statement : expression'''
	t[0] = Discard(t[1])

def p_print_statement(t):
	'simple_statement : PRINT expression'
	t[0] = Printnl([t[2]], None)
		
def p_assign_statement(t):
	'simple_statement : NAME ASSIGNMENT expression'
	t[0] = Assign([AssName(t[1], 'OP_ASSIGN')], t[3])
	
def p_name_expression(t):
	'expression : NAME'
	t[0] = Name(t[1])
	
def p_integer_expression(t):
	'expression : INT'
	t[0] = Const(t[1])
	
def p_negate_expression(t):
	'expression : NEGATE expression'
	t[0] = UnarySub(t[2])
	
def p_addition_expression(t):
	'expression : expression PLUS expression'
	t[0] = Add((t[1], t[3]))
	
def p_input_expression(t):
	'expression : INPUT LPARAN RPARAN'
	t[0] = CallFunc(Name('input'), [], None, None)
	
def p_paran_expression(t):
	'expression : LPARAN expression RPARAN'
	t[0] = t[2]

def p_error(t):
	print "Syntax Error: " + repr(t)
	
import ply.yacc as yacc
parser = yacc.yacc()
