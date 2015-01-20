from bin.load_source import *
from bin.dj_ast import *

import compiler
import compiler.ast

def main():
	first_ast = dj_ast("p0src/3.py")
	print first_ast.raw_tree
	print first_ast.flattened_tree
	test = compiler.compile(first_ast.raw_tree, "test.py", 'exec')

if __name__ == '__main__':
	main()
