class BinaryTree:
    """
    class describes a binary tree.
    Attributes:
    -----------
    left : BinaryTree
        left node
    right : BinaryTree
        right node
    code : int
        code of the product
    price : int
        price of the product
    Methods:
    -------
    insert(self, code, price):
        inserts new node of the binary tree
    find_cost(self, code, count):
        finds cost of customer's order
    """
    def __init__(self, code, price):
        """
        Sets all required attributes for the student object.
        Options
        ---------
        code : int
            code of the product
        price : int
            price of the product
        """
        if not isinstance(price, int):
            raise TypeError("Wrong type of price!")
        if price <= 0:
            raise ValueError("Wrong value of price!")
        if not isinstance(code, int):
            raise TypeError("Wrong type of code!")
        if code <= 0:
            raise ValueError("Wrong value of code!")
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
        """inserts new node of the binary tree:
        if code il less than existing insert left, if more insert right"""
        if self.code and self.price:
            if code < self.code:
                if self.left is None:
                    self.left = BinaryTree(code, price)
                else:
                    self.left.insert(code, price)
            elif code > self.code:
                if self.right is None:
                    self.right = BinaryTree(code, price)
                else:
                    self.right.insert(code, price)
            else:
                raise ValueError("This code is already exist!")
        else:
            self.code = code
            self.price = price

    def find_cost(self, code, count):
        """
        finds cost of customer's order by multiplying price by count of product
        returns cost of order
        """
        if code < self.code:
            if self.left is None:
                return "Product with code " + str(code) + " doesn't exist"
            return self.left.find_cost(code, count)
        elif code > self.code:
            if self.right is None:
                return "Product with code " + str(code) + " doesn't exist"
            return self.right.find_cost(code, count)
        return "Cost of your order is " + str(self.price*count)


root = BinaryTree(1, 500)
root.insert(2, 300)
root.insert(3, 200)
root.insert(4, 400)
root.insert(5, 700)
codeOfProd = int(input("Enter code of product: "))
number = int(input("Enter number of products: "))
if number <= 0:
    raise ValueError("Wrong value of number!")
print(root.find_cost(codeOfProd, number))
