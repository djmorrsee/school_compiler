import sys
import dj_lex

def main():
	lexer = dj_lex.lexer
	for i in range(1, len(sys.argv)):
		print sys.argv[i]
		text = open(sys.argv[1])
		lexer.input(text.read())
		for j in lexer:
			print j
		print
		
if __name__ == '__main__':
	main()
