import json


def load_index(filename):
    """Loads the index from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def search_files(index, search_terms, extension=None):
    """Searches for files in the index that contain the specified search terms."""
    results = {}
    for term in search_terms:
        if term in index:
            for file_path in index[term]:
                if extension is None or file_path.endswith(f'.{extension}'):
                    if file_path not in results:
                        results[file_path] = []
                    with open(file_path, 'r') as file:
                        for line in file:
                            if term in line:
                                results[file_path].append(line.strip())
    return results


def parse_search_query(query):
    """Parses the search query for terms and potential meta-search options."""
    terms = query.split()
    search_terms = []
    extension = None
    for term in terms:
        if term.startswith("type:"):
            extension = term.split("type:")[1]
        else:
            search_terms.append(term)
    return search_terms, extension


if __name__ == "__main__":
    # Load the index
    index = load_index("dict_index.json")

    # User input for search
    query = input("Enter search terms (use 'type:<ext>' to filter by file extension): ")
    search_terms, extension = parse_search_query(query)

    # Perform the search
    results = search_files(index, search_terms, extension)

    # Display results
    for file_path, lines in results.items():
        print(f"\nFile: {file_path}")
        for line in lines:
            print(line)
