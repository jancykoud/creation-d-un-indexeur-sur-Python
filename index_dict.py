import json
import os
import re


def index_words_in_file_dict(file_path, index):
    """Indexes words in a given text file using a dictionary."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b[\w-]{4,8}\b', text)
        for word in words:
            if word not in index:
                index[word] = []
            if file_path not in index[word]:
                index[word].append(file_path)


def index_files_dict(start_path):
    """Indexes words in all text files in a directory using a dictionary."""
    index = {}
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                index_words_in_file_dict(file_path, index)
    return index


if __name__ == "__main__":
    # TODO change file path to test this script
    home_path = 'C:\\Users\\SCD UM\\Desktop\\projet systeme'
    dict_index = index_files_dict(home_path)

    # Save the dictionary index in JSON
    with open('dict_index.json', 'w', encoding='utf-8') as f:
        json.dump(dict_index, f, ensure_ascii=False, indent=4)
