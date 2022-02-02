import ast
import inspect
import networkx as nx

from typing import Callable, List


def fib(n: int) -> List[int]:
    nums = [0, 1]
    for i in range(1, n - 1):
        nums.append(nums[-1] + nums[-2])

    return nums


class GraphWalker(ast.NodeVisitor):
    def __init__(self):
        self.stack = []
        self.graph = nx.DiGraph()

    def __get_label(self, node):
        label = str(type(node)).split(".")[-1][:-2]

        if hasattr(node, "name"):
            label = label + ": " + node.name

        if hasattr(node, "id"):
            label = label + ": " + node.id

        return label

    def generic_visit(self, node):
        parent_name = self.stack[-1] if len(self.stack) > 0 else None

        if isinstance(node, ast.Load):
            ast.NodeVisitor.generic_visit(self, node)
            return

        self.stack.append(str(node))
        self.graph.add_node(str(node), label=self.__get_label(node))

        if parent_name is not None:
            self.graph.add_edge(parent_name, str(node))

        ast.NodeVisitor.generic_visit(self, node)
        self.stack.pop()


def build_ast(func: Callable, save_path: str):
    ast_struct = ast.parse(inspect.getsource(func)).body[0]

    ast_walker = GraphWalker()
    ast_walker.visit(ast_struct)

    G = ast_walker.graph

    pic = nx.drawing.nx_pydot.to_pydot(G)
    pic.write_png(save_path)


if __name__ == "__main__":
    build_ast(fib, "artifacts/ast.png")
