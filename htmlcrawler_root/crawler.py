# TESTING
from htmlcrawler_root.utils import get_html_element_type, Tag


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(Node(child))

    def __repr__(self):
        return f'{self.data} : {self.children}'

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

    def create_tree(self):
        print('Creating tree from data...')

        contents_list = html_parser(self.file_data)

        self.root = Node(contents_list[0])
        level = 0
        child_index = 0

        for element in contents_list[1:]:
            if get_html_element_type(element) == Tag.ENTRY_TAG:
                self.root.add_child(element)
                level += 1
                child_index += 1
            elif get_html_element_type(element) == Tag.EXIT_TAG:
                pass
            else:
                pass

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
