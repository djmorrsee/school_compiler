from bin.load_source import *
from bin.dj_ast import *
from bin.dj_test import *

from pprint import pprint
import compiler, sys, os;

import bin.dj_lex as dj_lex

def write_assembly(flat_ast, open_file):
	vnum = len(flat_ast.vars)

	# Hard Coded ASM Boilerplate
	w = open_file.write
	w('.code32\n')
	w('.globl main\n')
	w('.type main, @function\n')
	w('main:\n\n')
	w('pushl %ebp\n')
	w('movl %esp, %ebp\n')
	w('subl $' + str(4 * vnum) + ', %esp\n')
	for i in flat_ast.statements: # Our compiled statements
		w(repr(i) + '\n')
	w('movl $0, %eax\n')
	w('leave\nret\n')


def main():
	# Extract Name
	f = sys.argv[1]
	name = os.path.splitext(f)[0]
	
	# Get our parser
	parser = dj_lex.parser
	pst = parser.parse(open(f).read())
	
	if pst is None:
		pst = []
	else:
		pst = list(pst)
		
	# My parser does not get the module or statement nodes
	pst = Module('', Stmt(pst))

	# Create Tree (flattening happens here)
	t = flattened_ast(pst)
	
	# Write output
	out = open(name + '.s', 'w')
	write_assembly(t, out)
	out.close()

if __name__ == '__main__':
	main()
