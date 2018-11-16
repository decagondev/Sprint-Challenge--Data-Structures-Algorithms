class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  # implementation TODO: add pseudocode for this method
  def breadth_first_for_each(self, cb):
    # perform the call back on the root value

    # check the level of the node [ a nested function : lets get recursive ]

      # try to set left to the nodes left property

      # if it failes return an error or raise an exception
      # if there was no exception on the try do a semi redundant call to make sure it is set

      # try to set right to the nodes right property

      # if it failes return an error or raise an exception
      # if there was no exception on the try do a semi redundant call to make sure it is set

      # --- end of the trys ---

      # set a counter variable to 0

      # if left holds a value the invoke the call back on the left value and increment the counter by 1

      # if right holds a value the invoke the call back on the right value and increment the counter by 1

      # if the counter hits 2 then do a recursive call to check the level of the node to the left and one to the right

      # then deal with a fallout case where left or right are none and just return to the caller

    # do the seed call to the nested function
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
