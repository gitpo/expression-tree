import logging
import random
from utils import Utils
from tree import Tree

def main():
    instance = Test()
    instance.validate_number_requirement()

'''
Testing the utility functions that do the critical tasks
Inherits the Utils & Tree class
'''
class Test(Utils):
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)      
    
    '''
    Tests the operator validation function to make sure the
    function is throwing an error on unacceptable objects
    '''
    def testing_acceptable_operators(self):
        test_list = ["$", "+", "#", 1, "3", "a", ".", "*"]
        self.logger.info(test_list)
        try:
            for i in test_list:
                self.is_operator_valid(random.choice(test_list))
                
        except Exception as e:
            self.logger.error(str(e))
            
    '''
    Tests if a list passed into the expression calculator is
    calculating from left to right
    '''
    def testing_expression_calculation(self):
        try:
            test_list = [1, 2, 3, 4, 5]
            self.logger.info(test_list)
            print self.get_random_operator_testing()
            calculation = self.calculate_expression(
                "+",                           
                test_list)
            self.logger.info(calculation)
        except Exception as e:
            self.logger.error(str(e))
    
    '''
    Picks a random operator from the list of 
    acceptable operators
    '''
    def get_random_operator_testing(self):
        try:
            ops = self.get_operators()
            ops_length = len(ops) - 1
            ops_random_index = random.randint(0, ops_length)
            random_op = random.choice(ops[ops_random_index])
            return random_op
        except Exception as e:
            self.logger.error(str(e))
    
    '''
    Testing a validation message is thrown when there are
    less than 2 nodes
    An exception is expected
    '''
    def validate_node_length_requirement(self):
        try:
            invalid_tree = ["+",
                ["+",
                     ["+", [7]], # invalid leaf
                     ["+", [5, 6]], 
                     ["+", [3, 4, 5, 3]]
                 ],
                ["-", 
                     ["+", [5, 6]], 
                     ["-", [3, 4, 7, 11]], 
                     ["/", [1]] # invalid leaf
                ]
           ]
            self.logger.info(
                Tree().check_children(invalid_tree)
            )
        except Exception as e:
            self.logger.error(str(e))
    
    '''
    Testing a validation message is thrown when a non-number is 
    in a leaf node
    An exception is expected
    '''
    def validate_number_requirement(self):
        try:
            invalid_tree = ["+",
                ["+",
                     ["+", [7, "@"]], # invalid leaf
                     ["+", [5, 6]], 
                     ["+", [3, 4, 5, 3]]
                 ],
                ["-", 
                     ["+", [5, 6]], 
                     ["-", [3, 4, "&", 11]], # invalid leaf
                     ["/", [1]]
                ]
           ]
            self.logger.info(
                Tree().check_children(invalid_tree)
            )
        except Exception as e:
            self.logger.error(str(e))
    

if __name__ == '__main__':
    main()