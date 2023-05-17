import re

def count_words(filename):
    # Read the file contents
    with open(filename, 'r') as file:
        text = file.read()

    # Split the text into words using the 're' library
    words = re.findall(r'\b\w+\b', text)

    # Count the number of words
    count = len(words)

    return count

# Example usage: count the number of words in 'example.txt'
filename = input("Enter File Path: ")
word_count = count_words(filename)
print(f'The file "{filename}" contains {word_count} words.')
