class Node:
    # left - ссылка на левого ребенка
    # right - ссылка на правого ребенка
    # value - символ, по умолчанию ничего
    # frequency - частота появления символа
    def __init__(self, left=None, right=None, value=None, frequency=0, height=0):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency
        self.height = height

    def __str__(self):
        return(f"{self.value} - {self.frequency}")

    # print all byte codes
    def order_to_show(node, str=""):
        if node.value is None:
            Node.order_to_show(node.left, str + "0")
            Node.order_to_show(node.right, str + "1")
        else:
            print(f"{node.value} - {str}")

    # return dictionary with key - symbol, value - byte code
    def order_to_get_codes(node):
        def get_codes(node, str):
            if node.left is not None:
                get_codes(node.left, str + '0')
                get_codes(node.right, str + '1')
            else:
                result[node.value] = str
        result = {}
        get_codes(node, "")
        return result
