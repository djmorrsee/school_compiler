from bin.load_source import *
from bin.dj_ast import *
from bin.dj_test import *

from pprint import pprint
import compiler, sys;


def main():
	f = sys.argv[1]
	t = flattened_ast(compiler.parseFile(f))
	out = open('check.py', 'w')
	for x in t.statements:
		out.write(repr(x) + '\n')
	out.close();

if __name__ == '__main__':
	main()
