from compiler.ast import *;

def num_nodes(ast):
	if isinstance(n, Module)
		return 1 + num_nodes(n.node)
	elif isinstance(n, Stmt)
		return sum([num_nodes(x) for x in n.nodes])
	elif isinstance(n, Printnl):
		return 1 + num_nodes(n.nodes[0])
	elif isinstance(n, Assign):
		return 1 + num_nodes(n.nodes[0]) + num_nodes(n.expr)
	elif isinstance(n, AssName):
		return 1
	elif isinstance(n, Discard):
		return 1 + num_nodes(n.expr)
	elif isinstance(n, Const):
		return 1
	elif isinstance(n, Name):
		return 1
	elif isinstance(n, Add):
		return 1 + num_nodes(n.left) + num_nodes(n.right)
	elif isinstance(n, UnarySub):
		return 1 + num_nodes(n.expr)
	elif isinstance(n, CallFunc):
		return 1 + num_nodes(n.node)
	else
		raise Exception('Error, Unrecognized AST Node!')
