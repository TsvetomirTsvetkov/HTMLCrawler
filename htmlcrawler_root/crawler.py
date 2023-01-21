# TESTING
from utils import load_file


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(Node(child))

    # def remove_child(self, child):
    #     try:
    #         self.children.remove(child)
    #     except Exception:
    #         print(f"{child} couldn't be removed as it wasn't found.")


# class Tree:
#     def __init__(self):
#         pass


class Stack:
    def __init__(self):
        self.elements = []
        self.size = 0

    def push(self, element):
        self.elements.append(element)
        self.size += 1

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            self.size -= 1
            return self.elements.pop()

    def top(self):
        return self.elements[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        return str(self.elements)


class Crawler:
    def __init__(self, file_data):
        self.file_data = file_data

    def create_tree(self):
        print('Creating tree from data...')
        input()

    def search_relative_path(self):
        print('Searching by relative path...')
        input()

    def change_node(self):
        print('Changing node...')
        input()

    def copy_node(self):
        print('Copying node...')
        input()

    def save_to_file(self):
        print('Saving to file...')
        input()

    def visualize(self):
        print('Visualizing...')
        input()


# test = Node('1')
# test.add_child('2')
# test.add_child('3')

# print(test.children)

def html_parser(file):
    level = 0
    stack = Stack()
    file_data = load_file(file)

    testing_list = []

    for character in file_data:
        if character == '<' and not stack.is_empty():
            tag_entry = ''
            while not stack.is_empty():
                tag_entry = stack.pop() + tag_entry
            testing_list.append(tag_entry)
            stack.push(character)
        elif character == '>' and stack.top() == '\\':
            level -= 1
        elif character == '>' and not stack.is_empty():
            tag_entry = ''
            while not stack.is_empty():
                tag_entry = stack.pop() + tag_entry
            tag_entry += character
            testing_list.append(tag_entry)
        else:
            stack.push(character)

    if not stack.is_empty():
        raise Exception('Error with parsing the document.')

    # Cleanup the whitespaces
    testing_list_new = []
    for element in testing_list:
        if '\n' not in element:
            testing_list_new.append(element)
    print(testing_list_new)


html_parser('/home/sktuan/Documents/HTMLCrawler/test_data/test.html')
