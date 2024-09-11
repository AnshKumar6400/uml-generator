import ast

class PythonUMLVisitor(ast.NodeVisitor):
    def __init__(self):
        self.classes = {}

    def visit_ClassDef(self, node):
        base_classes = [base.id for base in node.bases if isinstance(base, ast.Name)]
        class_info = {
            'name': node.name,
            'methods': [],
            'attributes': [],
            'inherits': base_classes
        }
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                class_info['methods'].append(item.name)
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        class_info['attributes'].append(target.id)
        self.classes[node.name] = class_info
        self.generic_visit(node)

def parse_code(code):
    tree = ast.parse(code)
    visitor = PythonUMLVisitor()
    visitor.visit(tree)
    return visitor.classes
