from Node import Node


class PriorityQueue:
    def __init__(self):
        self.count_of_nodes = 0
        self.queue = []

    def __str__(self):
        result = ''
        for n in self.queue:
            result += str(n) + ' '
        return result

    # add new node in priority queue
    def add_new_node(self, node):
        if self.count_of_nodes == 0:
            self.queue.append(node)
        else:
            i = 0
            while i < self.count_of_nodes and node.frequency > self.queue[i].frequency:
                i += 1
            while i < self.count_of_nodes and node.frequency == self.queue[i].frequency and node.height > self.queue[i].height:
                i += 1
            self.queue.insert(i, node)
        self.count_of_nodes += 1

    def delete_and_return_node(self):
        self.count_of_nodes -= 1
        return self.queue.pop(0)

    # print all elements in priority queue
    def show_elements(self):
        for element in self.queue:
            print(f"{element.value} с частотой {element.frequency}")
