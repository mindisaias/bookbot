def count_words(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        num_words = len(file_contents.split())
    return num_words

def count_chars(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    file_contents = file_contents.lower()
    char_dict = {}
    for word in file_contents:
        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]

    char_list.sort(reverse = True, key = sort_on)

    return char_list
