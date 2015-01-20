import compiler
import os.path
class dj_ast():
	def __init__(self, src_file):
		self.filename = os.path.basename(src_file)
		f = open(src_file)
		self.raw_tree = compiler.parse("")
		f.close()



