import sys
import json
from bin.dj_ast import *

def main():
	files = sys.argv[1:]
	out = open('reports/test_report.txt', 'w')
	for f in files:
		t = open(f)
		ast = dj_ast(f)
		out.write("File: " + f + "\n")
		out.write("Code: \n\n" + t.read() + "\n")
		out.write("AST: \n\n" + repr(ast.raw_tree))
		out.write("\n\n##########################\n\n")
		t.close()

	out.close()

if __name__ == '__main__':
	main()
