import json

def create_test_report():
	out = open("p0src/trees.txt")
	for i in range(1, 6):
		filename = "p0src/" + int(i) + ".py"
		ast = dj_ast(filename)
		f = open(filename)

		out.write(filename)
		out.write(f.read())
		f.close()
		out.write(ast.raw_tree)

	out.close()

