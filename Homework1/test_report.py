import sys, os
import json
import compiler
from bin.dj_ast import *
from bin.blais.print_ast import printAst


def main():
	files = sys.argv[1:]

	out = open('reports/test_report' '.txt', 'w')
	for f in files:
		ast = flattened_ast(compiler.parseFile(f))
		t = open(f)	
		out.write("File: " + f + "\n")
		out.write("Code: \n\n" + t.read() + "\n")
		out.write("AST: \n")
		printAst(ast.raw_ast, stream=out, initlevel=1)
		printAst(ast.raw_ast)
		out.write("\n\n##########################\n\n")
		t.close()

	out.close()

if __name__ == '__main__':
	main()
