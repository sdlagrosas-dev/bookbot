import string

def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        
        return file_contents


def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count


def count_chars(text):
    lower_text = text.lower()
    char_record = {}
    
    for char in lower_text:
        if char not in string.ascii_lowercase:
            continue
        if char not in char_record:
            char_record[char] = 1
        else:
            char_record[char] += 1
    
    return char_record


def sort_on(dict):
    return dict["count"]


def sort_char_records(char_records):
    char_list = []
    for char, count in char_records.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    return char_list


def generate_report(filename, word_count, char_records):
    print(f"*** Start report of {filename} ***")
    print(f"{word_count} words found in the document\n")

    for char_rec in char_records:
        print(f"The '{char_rec['char']}' character was found {char_rec['count']} times")

    print("*** End report ***")


def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = read_file(path_to_file)

    word_count = count_words(file_contents)
    char_records = count_chars(file_contents)
    sorted_char_list = sort_char_records(char_records)

    generate_report(path_to_file, word_count, sorted_char_list)


if __name__ == '__main__':
    main()