import unittest
from Binary_Search_Tree import *

class BST_Tester(unittest.TestCase):
    def setUp(self):
        self.__BST = Binary_Search_Tree()

# --> tree layout
#     
#
#                          1                          level 1
#                        /   \          
#                     /         \
#                  /               \
#               /                     \
#              2L                      2R             level 2           
#            /   \                    /   \
#           /     \                  /     \        
#          /       \                /       \       
#         /         \              /         \      
#       3LL        3LR           3RL         3RR      level 3 
#       / \         / \          / \         / \    
#      /   \       /   \        /   \       /   \   
#   4LLL  4LLR  4LRL  4LRR   4RLL  4RLR  4RRL  4RRR   level 4
#    / \   / \   / \   / \    / \   / \   / \   / \ 
#  5a  5b 5c 5d 5e 5f 5g 5h  5i 5j 5k 5l 5m 5n 5o 5p  level 5
# 

    def test_remove_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(1)
        self.assertEqual('[ ]', str(self.__BST))

    def test_remove_value_not_in_tree_w_1_item(self):
        with self.assertRaises(ValueError):
            self.__BST.insert_element(100) # el. 1  
            self.__BST.remove_element(10)  # number not in tree
        self.assertEqual('[ 100 ]', str(self.__BST))
    
    def test_insert_duplicate_value(self):
        with self.assertRaises(ValueError):
            self.__BST.insert_element(100) # el. 1
            self.__BST.insert_element(100) # el. 1 duplicate
        self.assertEqual('[ 100 ]', str(self.__BST))

# - - - - -     building to level 2 then emptying tree

    def test_insert_1_element(self):
        self.__BST.insert_element(100) # el. 1
        self.assertEqual('[ 100 ]', str(self.__BST))
        self.assertEqual([100], self.__BST.to_list())

    def test_insert_2L_element(self):
        self.__BST.insert_element(100) #el. 1
        self.__BST.insert_element(50) # el. 2L
        self.assertEqual('[ 50, 100 ]', str(self.__BST))
        self.assertEqual([50, 100], self.__BST.to_list())
        self.assertEqual('[ 50, 100 ]', self.__BST.in_order())
        self.assertEqual('[ 100, 50 ]', self.__BST.pre_order())
        self.assertEqual('[ 50, 100 ]', self.__BST.post_order())

    def test_insert_2R_element(self):
        self.__BST.insert_element(100)# el. 1
        self.__BST.insert_element(150) # el. 2R
        self.assertEqual('[ 100, 150 ]', str(self.__BST))
        self.assertEqual([100, 150], self.__BST.to_list())
        self.assertEqual('[ 100, 150 ]', self.__BST.in_order())
        self.assertEqual('[ 100, 150 ]', self.__BST.pre_order())
        self.assertEqual('[ 150, 100 ]', self.__BST.post_order())

    def test_remove_2_elements_from_2_level_tree(self):
        self.__BST.insert_element(100)# el. 1
        self.__BST.insert_element(150) # el. 2R
        self.__BST.insert_element(50) # el. 2L
        self.__BST.remove_element(100) #el. 1
        self.__BST.remove_element(150) #el . 2R
        self.assertEqual('[ 50 ]', str(self.__BST))
        self.assertEqual([50], self.__BST.to_list())
        self.assertEqual('[ 50 ]', self.__BST.in_order())
        self.assertEqual('[ 50 ]', self.__BST.pre_order())
        self.assertEqual('[ 50 ]', self.__BST.post_order())

    def test_remove_all_elements_from_2_level_tree(self):
        self.__BST.insert_element(100)# el. 1
        self.__BST.insert_element(150) # el. 2R
        self.__BST.insert_element(50) # el. 2L
        self.__BST.remove_element(100) #el. 1
        self.__BST.remove_element(150) #el . 2R
        self.__BST.remove_element(50) #el . 2L
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual([], self.__BST.to_list())
        self.assertEqual('[ ]', self.__BST.in_order())
        self.assertEqual('[ ]', self.__BST.pre_order())
        self.assertEqual('[ ]', self.__BST.post_order())

# - - - - - building tree to 3 levels then empty tree (involves rotations)

    def test_insert_to_3_level_tree(self):
        self.__BST.insert_element(100) #el. 1
        self.__BST.insert_element(50) # el. 2L
        self.__BST.insert_element(150) # el. 2R
        self.__BST.insert_element(25) # el. 3LL
        self.__BST.insert_element(75) # el. 3LR
        self.__BST.insert_element(125) # el. 3RL
        self.__BST.insert_element(175) # el. 3RR
        self.assertEqual('[ 25, 50, 75, 100, 125, 150, 175 ]', str(self.__BST))
        self.assertEqual([25, 50, 75, 100, 125, 150, 175], self.__BST.to_list())
        self.assertEqual('[ 25, 50, 75, 100, 125, 150, 175 ]', self.__BST.in_order())
        self.assertEqual('[ 100, 50, 25, 75, 150, 125, 175 ]', self.__BST.pre_order())
        self.assertEqual('[ 25, 75, 50, 125, 175, 150, 100 ]', self.__BST.post_order())

    def test_remove_entire_left_subtree_of_level_3_tree(self): #involves rotation
        self.__BST.insert_element(100) #el. 1
        self.__BST.insert_element(50) # el. 2L
        self.__BST.insert_element(150) # el. 2R
        self.__BST.insert_element(25) # el. 3LL
        self.__BST.insert_element(75) # el. 3LR
        self.__BST.insert_element(125) # el. 3RL
        self.__BST.insert_element(175) # el. 3RR
        self.__BST.remove_element(50)
        self.__BST.remove_element(75)
        self.__BST.remove_element(25)
        self.assertEqual('[ 100, 125, 150, 175 ]', str(self.__BST))
        self.assertEqual([100, 125, 150, 175], self.__BST.to_list())
        self.assertEqual('[ 100, 125, 150, 175 ]', self.__BST.in_order())
        self.assertEqual('[ 150, 100, 125, 175 ]', self.__BST.pre_order())
        self.assertEqual('[ 125, 100, 175, 150 ]', self.__BST.post_order())

    def test_remove_entire_left_subtree_and_right_left_subtree_of_level_3_tree(self): #involves rotation
        self.__BST.insert_element(100) #el. 1
        self.__BST.insert_element(50) # el. 2L
        self.__BST.insert_element(150) # el. 2R
        self.__BST.insert_element(25) # el. 3LL
        self.__BST.insert_element(75) # el. 3LR
        self.__BST.insert_element(125) # el. 3RL
        self.__BST.insert_element(175) # el. 3RR
        self.__BST.remove_element(125)
        self.__BST.remove_element(75)
        self.__BST.remove_element(25)
        self.__BST.remove_element(50)
        self.assertEqual('[ 100, 150, 175 ]', str(self.__BST))
        self.assertEqual([100, 150, 175], self.__BST.to_list())
        self.assertEqual('[ 100, 150, 175 ]', self.__BST.in_order())
        self.assertEqual('[ 150, 100, 175 ]', self.__BST.pre_order())
        self.assertEqual('[ 100, 175, 150 ]', self.__BST.post_order())
    
    def test_remove_entire_right_subtree_of_level_3_tree(self): #involves rotation
        self.__BST.insert_element(100) #el. 1
        self.__BST.insert_element(50) # el. 2L
        self.__BST.insert_element(150) # el. 2R
        self.__BST.insert_element(25) # el. 3LL
        self.__BST.insert_element(75) # el. 3LR
        self.__BST.insert_element(125) # el. 3RL
        self.__BST.insert_element(175) # el. 3RR
        self.__BST.remove_element(150)
        self.__BST.remove_element(125)
        self.__BST.remove_element(175)
        self.assertEqual('[ 25, 50, 75, 100 ]', str(self.__BST))
        self.assertEqual([25, 50, 75, 100], self.__BST.to_list())
        self.assertEqual('[ 25, 50, 75, 100 ]', self.__BST.in_order())
        self.assertEqual('[ 50, 25, 100, 75 ]', self.__BST.pre_order())
        self.assertEqual('[ 25, 75, 100, 50 ]', self.__BST.post_order())
    
# - - - - - building to 4 level tree 

#heavily right sided insertion

    def test_build_4_level_tree(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(4)
        self.__BST.insert_element(6)
        self.__BST.insert_element(8)
        self.__BST.insert_element(10)
        self.__BST.insert_element(12)
        self.__BST.insert_element(14)
        self.__BST.insert_element(11)
        self.__BST.insert_element(13)
        self.__BST.insert_element(15)
        self.__BST.insert_element(16)
        self.assertEqual('[ 2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16 ]', str(self.__BST))
        self.assertEqual([2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16], self.__BST.to_list())
        self.assertEqual('[ 2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16 ]', self.__BST.in_order())
        self.assertEqual('[ 12, 8, 4, 2, 6, 10, 11, 14, 13, 15, 16 ]', self.__BST.pre_order())
        self.assertEqual('[ 2, 6, 4, 11, 10, 8, 13, 16, 15, 14, 12 ]', self.__BST.post_order())

#heavily left sided deletions

    def test_empty_out_4_level_tree_stage_1(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(4)
        self.__BST.insert_element(6)
        self.__BST.insert_element(8)
        self.__BST.insert_element(10)
        self.__BST.insert_element(12)
        self.__BST.insert_element(14)
        self.__BST.insert_element(11)
        self.__BST.insert_element(13)
        self.__BST.insert_element(15)
        self.__BST.insert_element(16)
        self.__BST.remove_element(2)
        self.__BST.remove_element(4)
        self.__BST.remove_element(6)
        self.__BST.remove_element(11)
        self.__BST.remove_element(12)
        self.assertEqual('[ 8, 10, 13, 14, 15, 16 ]', str(self.__BST))
        self.assertEqual([8, 10, 13, 14, 15, 16], self.__BST.to_list())
        self.assertEqual('[ 8, 10, 13, 14, 15, 16 ]', self.__BST.in_order())
        self.assertEqual('[ 13, 10, 8, 15, 14, 16 ]', self.__BST.pre_order())
        self.assertEqual('[ 8, 10, 14, 16, 15, 13 ]', self.__BST.post_order())
    
    def test_empty_out_4_level_tree_stage_2(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(4)
        self.__BST.insert_element(6)
        self.__BST.insert_element(8)
        self.__BST.insert_element(10)
        self.__BST.insert_element(12)
        self.__BST.insert_element(14)
        self.__BST.insert_element(11)
        self.__BST.insert_element(13)
        self.__BST.insert_element(15)
        self.__BST.insert_element(16)
        self.__BST.remove_element(2)
        self.__BST.remove_element(4)
        self.__BST.remove_element(6)
        self.__BST.remove_element(11)
        self.__BST.remove_element(12)
        self.__BST.remove_element(8)
        self.__BST.remove_element(10)
        self.assertEqual('[ 13, 14, 15, 16 ]', str(self.__BST))
        self.assertEqual([13, 14, 15, 16], self.__BST.to_list())
        self.assertEqual('[ 13, 14, 15, 16 ]', self.__BST.in_order())
        self.assertEqual('[ 15, 13, 14, 16 ]', self.__BST.pre_order())
        self.assertEqual('[ 14, 13, 16, 15 ]', self.__BST.post_order())

    def test_empty_out_4_level_tree_stage_3(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(4)
        self.__BST.insert_element(6)
        self.__BST.insert_element(8)
        self.__BST.insert_element(10)
        self.__BST.insert_element(12)
        self.__BST.insert_element(14)
        self.__BST.insert_element(11)
        self.__BST.insert_element(13)
        self.__BST.insert_element(15)
        self.__BST.insert_element(16)
        self.__BST.remove_element(2)
        self.__BST.remove_element(4)
        self.__BST.remove_element(6)
        self.__BST.remove_element(11)
        self.__BST.remove_element(12)
        self.__BST.remove_element(8)
        self.__BST.remove_element(10)
        self.__BST.remove_element(15)
        self.assertEqual('[ 13, 14, 16 ]', str(self.__BST))
        self.assertEqual([13, 14, 16], self.__BST.to_list())
        self.assertEqual('[ 13, 14, 16 ]', self.__BST.in_order())
        self.assertEqual('[ 14, 13, 16 ]', self.__BST.pre_order())
        self.assertEqual('[ 13, 16, 14 ]', self.__BST.post_order())

    def test_empty_out_4_level_tree_stage_4(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(4)
        self.__BST.insert_element(6)
        self.__BST.insert_element(8)
        self.__BST.insert_element(10)
        self.__BST.insert_element(12)
        self.__BST.insert_element(14)
        self.__BST.insert_element(11)
        self.__BST.insert_element(13)
        self.__BST.insert_element(15)
        self.__BST.insert_element(16)
        self.__BST.remove_element(2)
        self.__BST.remove_element(4)
        self.__BST.remove_element(6)
        self.__BST.remove_element(11)
        self.__BST.remove_element(12)
        self.__BST.remove_element(8)
        self.__BST.remove_element(10)
        self.__BST.remove_element(15)
        self.__BST.remove_element(14)
        self.assertEqual('[ 13, 16 ]', str(self.__BST))
        self.assertEqual([13, 16], self.__BST.to_list())
        self.assertEqual('[ 13, 16 ]', self.__BST.in_order())
        self.assertEqual('[ 16, 13 ]', self.__BST.pre_order())
        self.assertEqual('[ 13, 16 ]', self.__BST.post_order())

    def test_empty_out_4_level_tree_stage_5(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(4)
        self.__BST.insert_element(6)
        self.__BST.insert_element(8)
        self.__BST.insert_element(10)
        self.__BST.insert_element(12)
        self.__BST.insert_element(14)
        self.__BST.insert_element(11)
        self.__BST.insert_element(13)
        self.__BST.insert_element(15)
        self.__BST.insert_element(16)
        self.__BST.remove_element(2)
        self.__BST.remove_element(4)
        self.__BST.remove_element(6)
        self.__BST.remove_element(11)
        self.__BST.remove_element(12)
        self.__BST.remove_element(8)
        self.__BST.remove_element(10)
        self.__BST.remove_element(15)
        self.__BST.remove_element(14)
        self.__BST.remove_element(16)
        self.assertEqual('[ 13 ]', str(self.__BST))
        self.assertEqual([13], self.__BST.to_list())
        self.assertEqual('[ 13 ]', self.__BST.in_order())
        self.assertEqual('[ 13 ]', self.__BST.pre_order())
        self.assertEqual('[ 13 ]', self.__BST.post_order())

    def test_empty_out_4_level_tree_stage_6(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(4)
        self.__BST.insert_element(6)
        self.__BST.insert_element(8)
        self.__BST.insert_element(10)
        self.__BST.insert_element(12)
        self.__BST.insert_element(14)
        self.__BST.insert_element(11)
        self.__BST.insert_element(13)
        self.__BST.insert_element(15)
        self.__BST.insert_element(16)
        self.__BST.remove_element(2)
        self.__BST.remove_element(4)
        self.__BST.remove_element(6)
        self.__BST.remove_element(11)
        self.__BST.remove_element(12)
        self.__BST.remove_element(8)
        self.__BST.remove_element(10)
        self.__BST.remove_element(15)
        self.__BST.remove_element(14)
        self.__BST.remove_element(16)
        self.__BST.remove_element(13)
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual([], self.__BST.to_list())
        self.assertEqual('[ ]', self.__BST.in_order())
        self.assertEqual('[ ]', self.__BST.pre_order())
        self.assertEqual('[ ]', self.__BST.post_order())


if __name__== '__main__':
    unittest.main()