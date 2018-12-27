

class CustomerCase:
    """ A service record for a customer """
    def __init__(self,
                 cust_id,
                 c_id,  # TODO function to find next unique id
                 c_description
                 ):
        self.customer_id = cust_id
        self._case_id = c_id
        self.case_description = c_description

    @property
    def customer_id(self):
        print("Getting Customer ID for Case")
        return self.customer_id

