import re
from typing import List

###Classes Review:

class BankCustomer:
    '''
    This class creates a BankCustomer object. A BankCustomer has a name,
    personal identification number, transaction log and total balance ($).
    '''

    def __init__(self, name, id_num):
        '''
        TODO:
            This method takes in a string (name) that represents the bank
            customer's name and an integer (id_num) that represents the customer's
            identification number.

            !IMPORTANT: Your task is to initialize FOUR instance variables: name, id,
            transaction_history and total.

            Store the name parameter in the name instance variable and the id_num
            parameter in the id instance variable.
            Your transaction_history instance variable should be a dictionary. In
            your dictionary map the string, "Deposits", to an empty list and map
            another string, "Withdrawals", to an empty list. Again, you create these
            mappings in the dictionary!
            Your total instance variable should be initialized to 0.
        '''


    def __repr__(self):
        '''
        TODO:
            This method never takes in a parameter!
            Your task is to create and return a string.
            You will first greet the Customer by saying Hello followed by there name.
            Then, you will include the following string:
            "Your bank history is as follows: ".
            After that, iterate through your transaction_history dictionary. The
            idea here is to use nested for loops. First iterate through the keys in
            the dictionary for each key print the key followed "Log: ". Then in the
            inner loop iterate through the list that is mapped to the current key
            and print out each item in the list on separate lines. DO NOT hard code
            the strings "Withdrawals" or "Deposits" in your repr code.
            Finally, include the string "Your current Balance: " followed by
            the customer's current total.
                Example only:
                    Hello Henry Smith! #Don't hard code the name "Henry Smith"
                    Your bank history is as follows:
                    Withdrawals Log:
                    100
                    50              # NOTE: Withdrawals and Deposits can show up in
                                    #       any order do not hard code the event!!
                    Deposits Log:
                    200
                    Your current Balance: $50
        '''
        withdrawals_log = ""
        deposits_log = ""

        # Your code starts here:

        # Your code ends here.

        return (f"Hello {self.name}! \n"
                f"Your bank history is as follows:\n\n"
                f"Withdrawals Log:"
                f"{withdrawals_log}"
                f"\n\nDeposits Log:"
                f"{deposits_log}"
                f"\n\nYour current Balance: ${self.balance}"
                )

    def get_id_num(self):
        '''
        TODO:
         This method takes no parameters.
         Your task is to return the customer's identification number.
        '''


    def deposit(self, amount):
        '''
        TODO:
         This method takes one integer parameter, amount, which represents a
         monetary amount.
         Your task is to append to the list that is mapped to the key "Deposits"
         and adjust the total instance variable accordingly.
        '''



    def withdrawal(self, amount):
        '''
        TODO:
            This method takes one integer parameter, amount, which represents a
            monetary amount.
            Your task is to append to the list that is mapped to the key
            "Withdrawals" and adjust the total instance variable accordingly.
        '''


###RegEx:

def get_numbers(file: str) -> List[str]:
    '''
    THIS IS A FINISHED FUNCTION
    Given the text file and using regular expressions, extract all of the valid phone numbers
    from the text file and return them in a list. Account for the below phone number formats:
    (888)-888-8888
    888-888-8888
    (888) 888-8888
    Parameters:
    :file: filename - file contains phone numbers and email addresses
    Returns:
    A list containing the phone numbers
    '''
    text = open(file).read()
    p = re.compile(r'((\(\d{3}\)[.-]?|\d{3}-)\d{3}-\d{4})')
    return p.findall(text)


def get_emails(file: str) -> List[str]:
    '''
    THIS IS A FINISHED FUNCTION
    Given the text file and using regular expressions, extract all of the valid email addresses
    from the text file and return them in a list.
    Parameters:
    :file: filename - file contains email addresses and phone numbers
    Returns:
    A list containing the email addresses
    '''
    text = open(file).read()
    p = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')
    return p.findall(text)


def main():
    '''
    TODO:
        Create a BankCustomer instance. Give them a name and personal identification
        number. Make use of the methods in your BankCustomer (make your customer
        wealthy or broke). Once you have finished depositing and withdrawing
        virtual and insignificant money, print a complete summary of your
        BankCustomer's transaction history and current balance.
    '''
    filename = "iwalktheline3.text"

    # Your code starts here:

    '''
    EXAMPLE CODE: 
    
    customer = BankCustomer("Shiyu", 1)
    customer.deposit(500)
    customer.deposit(200)
    customer.withdrawal(150)
    customer.deposit(40)
    customer.withdrawal(56)
    print(customer)
    
    OUTPUT:
    
    Hello Shiyu! 
    Your bank history is as follows:
    
    Withdrawals Log:
    150
    56
    
    Deposits Log:
    500
    200
    40
    
    Your current Balance: $946
    
    '''



if __name__ == '__main__':
    main()