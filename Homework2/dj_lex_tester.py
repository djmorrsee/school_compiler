import sys
import dj_lex

def main():
	lexer = dj_lex.lexer
	for i in range(1, len(sys.argv)):
		text = open(sys.argv[1])
		lexer.input(text.read())
		for j in lexer:
			print j
		
if __name__ == '__main__':
	main()
