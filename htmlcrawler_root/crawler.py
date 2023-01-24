# TESTING
from htmlcrawler_root.utils import get_html_element_type, Tag


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(Node(child, self))

    def __repr__(self):
        return f'{self.data} : {self.children}'


# class Tree:
#     def __init__(self):
#         pass


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.elements.pop()

    def top(self):
        return self.elements[-1]

    def is_empty(self):
        return self.elements == []

    def __repr__(self):
        return str(self.elements)


def html_parser(file_data):
    level = 0
    stack = Stack()

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

    # Cleanup the whitespaces
    testing_list_new = []
    for element in testing_list:
        if '\n' not in element:
            testing_list_new.append(element)
    return testing_list_new


class Crawler:
    def __init__(self, file_data):
        self.file_data = file_data
        self.root = None

    def _recursive_tree(self, root, contents_list):
        if len(contents_list) == 0:
            return root
        elif get_html_element_type(contents_list[0]) == Tag.ENTRY_TAG:
            root.add_child(contents_list[0])
            return self._recursive_tree(root.children[-1], contents_list[1:])
        elif get_html_element_type(contents_list[0]) == Tag.NOT_TAG:
            root.add_child(contents_list[0])
            return self._recursive_tree(root, contents_list[1:])
        elif get_html_element_type(contents_list[0]) == Tag.EXIT_TAG:
            if root.parent is not None:
                return self._recursive_tree(root.parent, contents_list[1:])
            else:
                return self._recursive_tree(root, contents_list[1:])

    def create_tree(self):
        print('Creating tree from data...')

        contents_list = html_parser(self.file_data)

        self.root = self._recursive_tree(Node(contents_list[0], None), contents_list[1:])

        print(self.root)

        input('\nPress any key to continue...\n')

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


print(html_parser('/home/sktuan/Documents/HTMLCrawler/test_data/test.html'))
