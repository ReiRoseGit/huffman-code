class Node:
    # left - ссылка на левого ребенка
    # right - ссылка на правого ребенка
    # value - символ, по умолчанию ничего
    # frequency - частота появления символа
    def __init__(self, left=None, right=None, value=None, frequency=0):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency

    def order_to_show(node, str=""):
        if node.value is None:
            Node.order_to_show(node.left, str + "0")
            Node.order_to_show(node.right, str + "1")
        else:
            print(f"{node.value} - {str}")
