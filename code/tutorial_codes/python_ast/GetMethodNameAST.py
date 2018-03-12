import ast
from collections import deque

class FunctionCallVisitor(ast.NodeVisitor):
    def __init__(self):
        self._name = deque()
    
    @property
    def name(self):
        return '.'.join(self._name)
    
    @name.deleter
    def name(self):
        self._name.clear()
    
    def visit_Name(self, node):
        self._name.appendleft(node.id)
    
    def visit_Attribute(self, node):
        try:
            self._name.appendleft(node.attr)
            self._name.appendleft(node.value.id)
        except AttributeError:
            self.generic_visit(node)
    
def get_func_calls(tree):
	func_calls = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                callvisitor = FunctionCallVisitor()
                callvisitor.visit(node.func)
                func_calls.append(callvisitor.name)
        return func_calls


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', help='Input .py file', required=True)
	args = parser.parse_args()
	tree = ast.parse(open(args.input).read())
	print get_func_calls(tree)


# Running:
## $ python function_calls_ast.py -i sample.py
