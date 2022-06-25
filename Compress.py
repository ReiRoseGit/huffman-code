from PriorityQueue import PriorityQueue
from Node import Node


def get_string_to_comress(name):
    f = open(name, 'r')
    return f.read()


def get_huffman_tree(name):
    pq = PriorityQueue()
    l = list(get_string_to_comress(name))
    dic = {}
    for el in l:
        if el in dic:
            dic[el] += 1
        else:
            dic[el] = 1
    for key, value in dic.items():
        node = Node(value=key, frequency=value)
        pq.add_new_node(node)
    while pq.count_of_nodes > 1:
        first = pq.delete_and_return_node()
        second = pq.delete_and_return_node()
        new_node = Node(frequency=first.frequency +
                        second.frequency, left=first, right=second)
        pq.add_new_node(new_node)
    return pq.delete_and_return_node()
