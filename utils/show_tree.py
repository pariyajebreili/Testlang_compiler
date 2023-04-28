from anytree import RenderTree
from utils.color_prints import Colorprints

def show_tree(tree):
    Colorprints.print_in_purple("Syntax Tree:")
    Colorprints.print_in_purple(RenderTree(tree).by_attr('name'))