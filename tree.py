from utils import Utils
import re
import ast
import logging

__author__ = "sosborne"          
'''          
The input is an expression tree in the form of a 
multi-dimensional list. The number of children extending 
from any node should be greater than or equal to 2.
Each node could either be a mathematical operator or a real number.
Each of the leaf nodes should be a real number 
The mathematical operators come from the set (-, +, /, *)
''' 
          
def main():
    
    tree = ['+',
            ['+',
                 ['+', 
                    ['-', [7, 8, ['*', 
                                  [3, 4]]]], 
                    ['+', [5, 6]]
                  ], 
                 ['+', [5, 6]]
             ],
            ['-', 
                 ['+', [5, 6]], 
                 ['-', [3, 4, 7, 11]], 
                 ['/', [1, 2]]
            ],
            ['+',
                 ['-', [7, 3]], 
                 ['+', [5, 6, 
                        ['+', 
                               [12, 37]]]], 
                 ['*', [3, 4]], 
                 ['/', [1, 2, 3, 4, 5]]
            ]
           ]
    
    # the entry point for evaluation is the calculate() function
    Tree().calculate(tree)   
           
class Tree(Utils):
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.tree_list_post = []
        
    def calculate(self, tree):
        '''
        This method converts the x-dimensional list into a string
        for pattern matching for leaf node indicators. Then performs
        calculations on those leaf nodes and replaces the leaf node 
        string indicators. Recursion is used until the tree is 
        reduced to a number which is the final calculation of the tree
        '''
        try:
            while isinstance(self.tree_list_post, list) == True:
                # finding the leaf nodes and replacing with the calculation
                tree_str_pre = str(tree)
                tree_str_post = tree_str_pre
                pattern = re.compile("\[\'[\+\-\*\/]\'\,\s\[[-|\d|,|\s]*\]\]")
                leaf_matches = pattern.findall(tree_str_pre)
                for i in leaf_matches:
                    match = str(i)
                    leaf_list = ast.literal_eval(i)
                    operator = leaf_list[0]
                    leafs = str(leaf_list[1:]).lstrip("[").rstrip("]").split(", ")
                    leafs = [int(i) for i in leafs]
                    calculation = self.calculate_expression(operator, leafs)
                    tree_str_post = tree_str_post.replace(match, str(calculation))
                
                # converting the stray numbers back to list for recalculation
                pattern = re.compile("\[\'[\+\-\*\/]\'\,\s[-|\d|,|\s]*\]")
                leaf_matches = pattern.findall(tree_str_post)
                for i in leaf_matches:
                    update_str = i
                    update_str = update_str.replace("', ", "', [")
                    update_str = update_str.replace("]", "]]")
                    tree_str_post = tree_str_post.replace(i, update_str)
                self.tree_list_post = ast.literal_eval(tree_str_post)
                
                # info logs to follow the calculations
                if tree_str_post.isdigit() == True:
                    self.logger.info(" This tree equals " + str(self.tree_list_post))
                else:
                    self.logger.info(self.tree_list_post)
                
                # recursion to continue reducing the branches
                self.calculate(self.tree_list_post)

        except Exception as e:
            self.logger.error(str(e))
        

if __name__ == '__main__':
    main()