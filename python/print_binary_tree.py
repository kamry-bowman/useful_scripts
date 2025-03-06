def print_tree(node, last=True, header=''):
    """
    Print a binary tree  (a recursive class with a #left and #right and #val)
    recursively so that its structured can be quickly viewed.

    Based on https://stackoverflow.com/a/76691030/9865580

    """
    elbow = "└──"
    pipe = "│  "
    tee = "├──"
    blank = "   "
    print(header + (elbow if last else tee) + str(node.val))
    children = [n for n in [node.right, node.left] if n is not None]
    if children:
        for i, n in enumerate(children):
            print_tree(
                    n,
                    header=header + (blank if last else pipe),
                    last=i == len(children) - 1
            )
