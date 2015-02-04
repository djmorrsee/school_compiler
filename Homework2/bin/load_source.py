# Loads file of filename, reads it and returns a string
def load_source(filename):
	f = open(filename, 'r')
	return f.read()
