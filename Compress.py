from email.mime import message
from PriorityQueue import PriorityQueue
from Node import Node


class Compress:
    # create a compress object, name - name of file to compress
    def __init__(self, name="input.txt", output="output.txt"):
        self.name = name
        self.output = output
        self.string_to_compress = self.get_string_to_comress()

    # return string to compress
    def get_string_to_comress(self):
        f = open(self.name, 'r')
        s = f.read()
        f.close()
        return s

    # return huffman tree
    def get_huffman_tree(self):
        pq = PriorityQueue()
        l = list(self.get_string_to_comress())
        dic = {}
        for el in l:
            if el in dic:
                dic[el] += 1
            else:
                dic[el] = 1
        for key, value in dic.items():  # key - symbol, value - frequency
            node = Node(value=key, frequency=value)
            pq.add_new_node(node)
        while pq.count_of_nodes > 1:
            first = pq.delete_and_return_node()
            second = pq.delete_and_return_node()
            new_node = Node(frequency=first.frequency +
                            second.frequency, left=first, right=second, height=max(first.height, second.height) + 1)
            pq.add_new_node(new_node)
        return pq.delete_and_return_node()

    # return codes in dictionary: key - symbol, value - code
    def get_compressed_codes(self):
        return Node.order_to_get_codes(self.get_huffman_tree())

    # return bits array
    def get_bits_array(self):
        codes = self.get_compressed_codes()
        bits = []
        sum = 0
        bit = 1
        for symbol in self.string_to_compress:
            for c in codes[symbol]:
                if c == '1':
                    sum |= bit
                if bit < 128:
                    bit <<= 1
                else:
                    bits.append(sum)
                    sum = 0
                    bit = 1
        if bit > 1:
            bits.append(sum)
        return bits

    # write message in output file
    def write_message(self):
        f = open(self.output, 'wb')
        compressed_string = ""
        f.close()

    # function to test
    def decode_message(self):
        def get_key(d, value):
            for k, v in d.items():
                if v == value:
                    return k
        self.write_message()
        codes = self.get_compressed_codes()
        f = open(self.output, 'r')
        compressed_string = f.read()
        n = int(compressed_string, 2)
        n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        result = ""
        cur_str = ""
        for letter in compressed_string:
            cur_str += letter
            if cur_str in codes.values():
                result += get_key(d=codes, value=cur_str)
                cur_str = ""
        return result
