from Node import Node


class PriorityQueue:
    def __init__(self):
        self.count_of_nodes = 0
        self.queue = []

    def add_new_node(self, node):
        if self.count_of_nodes == 0:
            self.queue.append(node)
        else:
            i = 0
            while i < self.count_of_nodes and node.frequency > self.queue[i].frequency:
                i += 1
            if i == self.count_of_nodes - 1:
                i += 1
            self.queue.insert(i, node)
        self.count_of_nodes += 1

    def delete_and_return_node(self):
        self.count_of_nodes -= 1
        return self.queue.pop(0)

    def show_elements(self):
        for element in self.queue:
            print(f"{element.value} с частотой {element.frequency}")
