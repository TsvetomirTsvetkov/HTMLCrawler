# External imports
import copy

# Internal imports
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
    stack = Stack()

    testing_list = []

    for character in file_data:
        if character == '<' and not stack.is_empty():
            tag_entry = ''
            while not stack.is_empty():
                tag_entry = stack.pop() + tag_entry
            testing_list.append(tag_entry)
            stack.push(character)
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

    def __find_root(self, node):
        while node.parent is not None:
            node = node.parent
        return node

    # Protected method for recursively creating the tree
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

    # Public method for creating the tree
    def create_tree(self):
        print('Creating tree from data...')

        contents_list = html_parser(self.file_data)

        self.root = self._recursive_tree(Node(contents_list[0], None), contents_list[1:])
        print(self.root)

        print('The doc tree has been created!')

        input('\nPress any key to continue...\n')

    # Protected method for searching through the tree
    def search_nodes(self, relative_path):
        if len(relative_path) < 2 or relative_path[0:2] != '//':
            return 'Wrong input.\nTry again.\n'
        else:
            buffer = ''
            helper_list = []
            root_copy = copy.deepcopy(self.root)
            html_tag_found = False

            for character in relative_path[2:]:
                if character == '/':
                    if not html_tag_found and buffer == 'html':
                        html_tag_found = True
                        buffer = ''
                    elif not html_tag_found and buffer != 'html':
                        return 'Error while parsing.'
                    else:
                        helper_list = []
                        buffer = '<' + buffer
                        for child in root_copy.children:
                            if child.data.startswith(buffer, 0, len(buffer)):
                                helper_list.append(child)
                                root_copy = child
                        buffer = ''
                elif character == '[':
                    helper_list = []
                    buffer = '<' + buffer
                    for child in root_copy.children:
                        if child.data.startswith(buffer, 0, len(buffer)):
                            helper_list.append(child)
                    buffer = ''
                elif character == ']':
                    return helper_list[(int)(buffer)]
                    buffer = ''
                    helper_list = []
                else:
                    buffer += character

            if buffer != '':
                if buffer == 'html':
                    return self.root
                else:
                    helper_list = []
                    buffer = '<' + buffer
                    for child in root_copy.children:
                        if child.data.startswith(buffer, 0, len(buffer)):
                            helper_list.append(child)
                    return helper_list
            elif buffer == '' and len(relative_path) == 2:
                return root_copy

    # Public method for searching the relative path
    def search_relative_path(self):
        relative_path = input('PRINT ')

        print(self.search_nodes(relative_path))

        input('\nPress any key to continue...\n')

    # Public method for changing one of the nodes of the tree
    def change_node(self):
        input_text = input('SET ')
        relative_path = ''
        set_value = ''
        found_space = False
        for character in input_text:
            if character == ' ':
                found_space = True
                continue
            if not found_space:
                relative_path += character
            else:
                set_value += character

        nodes = self.search_nodes(relative_path)

        for node in nodes:
            for child in node.children:
                child.data = set_value

        new_root = self.__find_root(nodes[0])
        self.root = copy.deepcopy(new_root)

        input('\nPress any key to continue...\n')

    # Public method for copying one of the nodes of the tree
    def copy_node(self):
        print('Copying node...')
        input('\nPress any key to continue...\n')

    # Public method to save the tree to a file
    def save_to_file(self):
        filename = input('Please enter filename: ')

        if self.root is None:
            print('The doc tree is empty.\n Nothing to save.\n')
        else:
            with open(f'test_data/{filename}', 'w') as f:
                f.write(str(self.root))

        input('\nPress any key to continue...\n')

    # Public method to visualize the tree
    def visualize(self):
        print('Visualizing...')
        input('\nPress any key to continue...\n')
