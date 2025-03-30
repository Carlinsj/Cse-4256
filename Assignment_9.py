def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root, " ")
