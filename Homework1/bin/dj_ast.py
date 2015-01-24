import compiler
import copy
from compiler.ast import *

import os.path

class Var():
	def __init__(self, name, index):
		self.name = name
		self.index = index
		self.mapping = '-' + str(4 * (index + 1)) + '(%ebp)'

	def __repr__(self):
		return str(self.name)

	def stack_mapping(self):
		return str(self.mapping)

class Statement(object):
	def __init__(self, py_text, as_text):
		self.py_text = py_text
		self.as_text = as_text

	def __repr__(self):
		return str(self.as_text)

class Assignment(Statement):
	def __init__(self, store, val):
		py_text = str(store) + ' = '  + str(val)
		s_text = 'movl ' + str(val) + store.mapping	
		super(Assignment, self).__init__(py_text, s_text)

class Addition(Statement):
	def __init__(self, store, val):
		py_text = str (store) + ' = ' + str(store) + ' + ' + str(val)
		s_text = 'addl ' + str(val) + store.mapping
		super(Addition, self).__init__(py_text, s_text)

class Negate(Statement):
	def __init__(self, store):
		py_text = str (store) + ' = ' + '-' + str(store)
		s_text = 'negl ' + store.mapping
		super(Negate, self).__init__(py_text, s_text)

class Print(Statement):
	def __init__(self, val):
		py_text = 'print ' + str(val)
		s_text = 'pushl ' + val.mapping + '\ncall print_int_nl\naddl $4, %esp'
		super(Print, self).__init__(py_text, s_text)

class Input(Statement):
	def __init__(self, store):
		py_text = str(store) + " = input()"
		s_text = "call input\nmovl %eax, " + store.mapping()
		super(Input, self).__init__(py_text, s_text)

class flattened_ast ():
	def __init__(self, root):
		self.raw_ast = root
		self.vars = []
		self.statements = []
		self.process(self.raw_ast)

	def add_tmp_var(self):
		vn = "__tmp" + str(len(self.vars)) + "__"
		self.vars.append(Var(vn, len(self.vars)))
		return self.vars[-1]

	def add_stmt(self, stmt):
		self.statements.append(stmt)

	def process(self, n):
		# Certain Nodes should be Extracted into statements
		# Other nodes should be given variables instead of real nodes

		# First, Find Leaves
		if isinstance(n, Module):
			self.process(n.node)
		elif isinstance(n, Stmt):
			for i in n.nodes:
				self.process(i)
		elif isinstance(n, Printnl):
			self.add_stmt(Print(self.process(n.nodes[0])))
		elif isinstance(n, Assign):
			if not isinstance(n.nodes[0], AssName):
				raise Exception ("AssName not after Assign!")
			name = n.nodes[0].name;
			if not name in self.vars:
				self.vars.append(Var(name, len(self.vars)))
						
			self.add_stmt(Assignment(self.vars[, self.process(n.expr)))

			# Create new Var, assign process(expr) to it
		elif isinstance (n, AssName): # Leaf and vars
			return
		elif isinstance(n, Discard):
			self.process(n.expr)
		elif isinstance(n, Const): # Leaf
			return n.value
		elif isinstance(n, Name): # Leaf
			if not n.name in self.vars:
				raise Exception("Using Var Before Assignment!")
			return str(n.name)
		elif isinstance(n, Add):
			tmpv = self.add_tmp_var()
			self.add_stmt(Assignment(tmpv, self.process(n.left)))
			self.add_stmt(Addition(tmpv, self.process(n.right)))
			return tmpv
		elif isinstance(n, UnarySub):
			tmpv = self.add_tmp_var()
			self.add_stmt(Assignment(tmpv, self.process(n.expr)))
			self.add_stmt(Negate(tmpv))
			return tmpv
		elif isinstance(n, CallFunc): # Leaf
			if not n.node.name == 'input':
				raise Exception("Can only call input")
			else:
				tmpv = self.add_tmp_var()
				self.statements.append(Input(tmpv))
				return tmpv
		else:
			raise Exception('Unknown AST Node: ' + repr(n))



