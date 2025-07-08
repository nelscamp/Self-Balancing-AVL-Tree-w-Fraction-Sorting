class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      # TODO complete Node initialization
      self.left = None
      self.right = None
      self.height = 1
  
  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    if self.get_height() == 0:
      self.__root = self.__BST_Node(value)
    else:
      self.__root = self.__recursive_insertion(self.__root, value)
  
  def __recursive_insertion(self, node, value):
    if node is None:
      return self.__BST_Node(value)
    elif value == node.value:
      raise ValueError
    elif value < node.value:
      node.left = self.__recursive_insertion(node.left, value)
    elif value > node.value:
      node.right = self.__recursive_insertion(node.right, value)
    node.height = self.cur_node_height(node)
    return self.__balance(node)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    if self.__root == None:
      raise ValueError
    else:
      self.__root = self.__recursive_removal(self.__root, value)
    
  def __recursive_removal(self, node, value):
    if node is None:
      raise ValueError
    elif value < node.value:
      node.left = self.__recursive_removal(node.left, value)
    elif value > node.value:
      node.right = self.__recursive_removal(node.right, value)
    elif node.value == value:
      if node.left is None and node.right is None:
        return None
      elif node.left is not None and node.right is None:
        return node.left
      elif node.left is None and node.right is not None:
        return node.right
      elif node.left is not None and node.right is not None:
        smaller_node = self.__smaller_node(node.right)
        node.value = smaller_node.value
        node.right = self.__recursive_removal(node.right, smaller_node.value)
    node.height = self.cur_node_height(node)
    return self.__balance(node)

  def __smaller_node(self, root):
    if root.left is None:
      return root
    else:
      return self.__smaller_node(root.left)

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.get_height() == 0:
      return '[ ]'
    else:
      return '[ ' + str(self.__in_order_recursive(self.__root))[1: -1] + ' ]'

  def __in_order_recursive(self, node):
    list = []
    if node:
      list = self.__in_order_recursive(node.left)
      list.append(node.value)
      list += self.__in_order_recursive(node.right)
    return list

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.get_height() == 0:
      return '[ ]'
    else:
      return '[ ' + str(self.__pre_order_recursive(self.__root))[1: -1] + ' ]'

  def __pre_order_recursive(self, node):
    list = []
    if node:
      list.append(node.value)
      list += self.__pre_order_recursive(node.left)
      list += self.__pre_order_recursive(node.right)
    return list

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.get_height() == 0:
      return '[ ]'
    else:
      return '[ ' + str(self.__post_order_recursive(self.__root))[1: -1] + ' ]'

  def __post_order_recursive(self, node):
    list = []
    if node:
      list += self.__post_order_recursive(node.left)
      list += self.__post_order_recursive(node.right)
      list.append(node.value)
    return list

  def to_list(self):
    return self.__to_list_recursive(self.__root)

  def __to_list_recursive(self, node):
    list = []
    if node:
      list = self.__to_list_recursive(node.left)
      list.append(node.value)
      list += self.__to_list_recursive(node.right)
    return list

  def cur_node_height(self, node):
    if node is None:
      return 0
    elif node.left is None and node.right is None:
      return 1
    elif node.left is None and node.right is not None:
      return node.right.height+1
    elif node.left is not None and node.right is None:
      return node.left.height+1
    else:
      return max(node.left.height, node.right.height)+1

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation
    if self.__root is None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

  def __balance(self, root):
    balance_root = self.__balance_factor(root)
    balance_left = self.__balance_factor(root.left)
    balance_right = self.__balance_factor(root.right)
    if root is None:
      return None
    elif balance_root in [-1, 0, 1]:
      return root
    elif balance_root == -2:
      if balance_left <= 0:
        root = self.__r_rotate(root)
        return root
      elif balance_left > 0:
        root.left = self.__l_rotate(root.left)
        root = self.__r_rotate(root)
        return root
    elif balance_root == 2:
      if balance_right >= 0:
        root = self.__l_rotate(root)
        return root
      elif balance_right < 0:
        root.right = self.__r_rotate(root.right)
        root = self.__l_rotate(root)
        return root

  def __l_rotate(self, root):
    y = root.right
    temp = y.left
    y.left = root
    y.left.right = temp
    y.left.height = self.cur_node_height(y.left)
    y.height = self.cur_node_height(y)
    return y

  def __r_rotate(self, root):
    y = root.left
    temp = y.right
    y.right = root
    y.right.left = temp
    y.right.height = self.cur_node_height(y.right)
    y.height = self.cur_node_height(y)
    return y
    
  def __balance_factor(self, root):
    if root is None:
      return 0
    else:
      return self.cur_node_height(root.right) - self.cur_node_height(root.left)

if __name__ == '__main__':
   #unit tests make the main section unnecessary.
  # bst = Binary_Search_Tree()
  # #num = [5, 3, 7, 8, 1, 2, 10, 11, 4, 19, 21, 14, 15, 0]
  # num = [5, 4, 6, 8, 7, 1, 2, 9, 11, 13, 19]
  # for i in num:
  #   bst.insert_element(i)
  # print(bst.in_order())
  # print(bst.pre_order())
  # print(bst.post_order())
  # print(bst.to_list())
  pass
