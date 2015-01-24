from bin.load_source import *
from bin.dj_ast import *
from bin.dj_test import *

from pprint import pprint
import compiler, sys, os;

def write_assembly(flat_ast, open_file):
	vnum = len(flat_ast.vars)

	w = open_file.write
	w('.code32\n')
	w('.globl main\n')
	w('.type main, @function\n')
	w('main:\n\n')
	w('pushl %ebp\n')
	w('movl %esp, %ebp\n')
	w('subl $' + str(4 * vnum) + ', %esp\n')
	for i in flat_ast.statements:
		w(repr(i) + '\n')
	w('movl $0, %eax\n')
	w('leave\nret\n')


def main():
	f = sys.argv[1]
	name = os.path.splitext(f)[0]

	t = flattened_ast(compiler.parseFile(f))
	
	out = open(name + '.s', 'w')
	write_assembly(t, out)
	out.close()

if __name__ == '__main__':
	main()
