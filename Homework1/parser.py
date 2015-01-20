from bin.load_source import *

import compiler
import compiler.ast

def main():
	ast = compiler.parse("print - input() + input()")

if __name__ == '__main__':
	main()
