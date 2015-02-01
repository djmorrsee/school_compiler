import sys
import dj_lex
import compiler

from pprint import pprint

def main():
	yacc = dj_lex.parser
	
	for i in range(1, len(sys.argv)):
		text = open(sys.argv[i]).read()
		yres = yacc.parse(text)
		cres = compiler.parse(text)
		x = cres.node.nodes
		y = yres
		pprint(x)
		print
		pprint(y)
		print;print

if __name__ == '__main__':
	main()
