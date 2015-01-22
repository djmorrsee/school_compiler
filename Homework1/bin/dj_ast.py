import compiler
import copy
from compiler.ast import *

import os.path

class flattened_ast ():
	def __init__(self, root):
		self.raw_ast = root
		self.vars = {}
		self.statements = []

	def add_var(name):
		pass
	def add_statement(node):
		pass
	def process(n):
		# Certain Nodes should be Extracted into statements
		# Other nodes should be given variables instead of real nodes
		if isinstance(n, Add):
			
		pass
		

def flatten_node(n):
	if isinstance(n, Module):
		n.node = flatten_node(n.node)
		return n
	elif isinstance(n, Stmt):
		for i in range(0, len(n.nodes)):
			n.nodes[i] = flatten_node(n.nodes[i])
		return n
	elif isinstance(n, Printnl):
		n.nodes[0] = flatten_node(n.nodes[0])
		return n
	elif isinstance(n, Assign):
		n.expr = flatten_node(n.expr)
		return n
	elif isinstance (n, AssName):
		return n
	elif isinstance(n, Discard):
		n.expr = flatten_node(n.expr)
		return n
	elif isinstance(n, Const):
		return n
	elif isinstance(n, Name):
		return n
	elif isinstance(n, Add):
		n.left = flatten_node(n.left)
		n.right = flatten_node(n.right)
		return n #Const(n.left.value + n.right.value) # as a flattened left and right node should be numerical Const
	elif isinstance(n, UnarySub):
		n.expr = flatten_node(n.expr)
		return n # Const(-n.expr.value)
	elif isinstance(n, CallFunc):
		n.node = flatten_node(n.node)
		return n
	else:
		raise Exception('Unknown AST Node' + n)

class dj_ast():

	# Call Flatten on Children, Process, then return self/new tree
			
			
	def __init__(self, src_file):
		self.filename = os.path.basename(src_file)
		self.raw_tree = compiler.parseFile(src_file)
		self.flattened_tree = flatten_node(copy.deepcopy(self.raw_tree))		

	
