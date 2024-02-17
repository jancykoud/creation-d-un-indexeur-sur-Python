import json
import os
import re


class TreeNode:
    def __init__(self):
        self.children = {}
        self.file_paths = []


def add_word_to_tree(root, word, file_path):
    """Adds a word and file path to the tree."""
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TreeNode()
        node = node.children[char]
    if file_path not in node.file_paths:
        node.file_paths.append(file_path)


def index_words_in_file_tree(file_path, root):
    """Indexes words in a given text file using a tree."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b[\w-]{4,8}\b', text)
        for word in words:
            add_word_to_tree(root, word, file_path)


def index_files_tree(start_path):
    """Indexes words in all text files in a directory using a tree."""
    root = TreeNode()
    for root_dir, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root_dir, file)
                index_words_in_file_tree(file_path, root)
    return root


def tree_to_dict(node):
    """Converts the tree into a dictionary for JSON saving."""
    result = {}
    for char, child in node.children.items():
        result[char] = {'files': child.file_paths, 'children': tree_to_dict(child)}
    return result


if __name__ == "__main__":
    # TODO change file path to test this script
    home_path = 'C:\\Users\\SCD UM\\Desktop\\projet systeme'
    tree_root = index_files_tree(home_path)

    # Save the tree index in JSON
    tree_index = tree_to_dict(tree_root)
    with open('tree_index.json', 'w', encoding='utf-8') as f:
        json.dump(tree_index, f, ensure_ascii=False, indent=4)
