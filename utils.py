import operator
import logging

'''
The Utils class maintains helper functions
and validation functions for the Tree class.
This was written using the Python 2.7.8 compiler
''' 
class Utils:
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    # returns the participating operators
    def get_operators(self):
        return ["/", "*", "+", "-"]
    
    # returns the minimum allowed number of nodes
    def get_node_minimum(self):
        return 2
    
    # takes a list and an operator and performs
    # the calculation starting from left to right
    def calculate_expression(self, op, my_list):
        try:
            operators = { 
                "/": operator.div, 
                "*": operator.mul, 
                "+": operator.add, 
                "-": operator.sub 
            }
            base = my_list[0]
            while len(my_list) >= 2:
                base = operators[op] (base, my_list[1])
                my_list.pop(0)
            return base
        except Exception as e:
            self.logger.error(str(e))
    
    # returns the root operator
    def get_root_operator(self, list):
        try:
            return list[0]
        except Exception as e:
            self.logger.error(str(e))
    
    # validates whether all elements in a list are numbers
    def is_joined_list_int(self, my_list):
        try:
            joined_str = ''.join([str(i) for i in my_list])
            if joined_str.isdigit() == False:
                return False
            return True
        except Exception as e:
            self.logger.error(str(e))    
    
    # validates the length of the list meets the minimum requirements
    def does_len_qualify(self, my_list):
        try:
            if len(my_list) < 2:
                self.logger.error(
                    " %s does not meet the minimum node requirement" % str(my_list)
                    )
                exit()
        except Exception as e:
            self.logger.error(str(e))        
    
    # validates the operator
    def is_operator_valid(self, my_list):
        try:
            if my_list[0] not in self.get_operators():
                self.logger.error(
                    " %s is not an operator" % str(my_list)
                    )
                exit()
        except Exception as e:
            self.logger.error(str(e))
    