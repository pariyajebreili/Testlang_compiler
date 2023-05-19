from anytree import RenderTree
from my_utils.colorprints import ColorPrints

def show_tree(tree):
    ColorPrints.print_in_purple("Syntax Tree:")
    ColorPrints.print_in_purple(RenderTree(tree).by_attr('name'))