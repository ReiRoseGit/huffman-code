from PriorityQueue import PriorityQueue
from Node import Node


class Compress:
    # create a compress object, name - name of file to compress
    def __init__(self, name="input.txt", output="output.bin"):
        self.name = name
        self.output = output

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
        for symbol in self.get_string_to_comress():
            for c in codes[symbol]:
                if c == '1':
                    sum |= bit
                if bit < 128:
                    bit <<= 1
                else:
                    bits.append(sum.to_bytes(1, byteorder="big"))
                    sum = 0
                    bit = 1
        if bit > 1:
            bits.append(sum.to_bytes(1, byteorder="big"))
        return bits

    # create header file: lenght, dictionary of compressed codes
    def create_header(self):
        header = []
        header.append(
            len(self.get_string_to_comress()).to_bytes(4, byteorder="big"))
        dic = self.get_compressed_codes()
        header.append(len(dic).to_bytes(1, byteorder="big"))
        for value, code in dic.items():
            header.append(value.encode())
            header.append(len(code).to_bytes(1, byteorder="big"))
            header.append(code.encode())
        return header

    # write message in output file
    def write_message(self):
        f = open(self.output, 'wb')
        res = self.create_header() + self.get_bits_array()
        for el in res:
            f.write(el)
        f.close()

    # return decoded message
    def decode_message(self):
        def get_correct_string(s):
            l = list(s)
            l.reverse()
            while len(l) < 8:
                l.append("0")
            return "".join(l)

        def get_key(d, value):
            for k, v in d.items():
                if v == value:
                    return k
        f = open(self.output, 'rb')
        size_of_input_string = int.from_bytes(
            f.read(4), "big")
        size_of_dic = int.from_bytes(f.read(1), "big")
        d = dict()
        for _ in range(size_of_dic):
            k = f.read(1)
            s = int.from_bytes(f.read(1), "big")
            v = f.read(s)
            d[k.decode()] = v.decode()
        result = ""
        coded_string = f.readline()
        code = ""
        for bt in coded_string:
            for i in get_correct_string("{0:b}".format(bt)):
                code += i
                if code in d.values():
                    result += get_key(d, code)
                    code = ""
                    size_of_input_string -= 1
                    if size_of_input_string <= 0:
                        break
        f.close()
        return result

    def write_decoded_result(self):
        result = self.decode_message()
        with open(self.name, "w") as f:
            f.write(result)
