from collections import Counter

#Reading the File
def read_file(filename):     #Opens and reads the content of a specified file.
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return ""

#Counting Lines
def count_lines(content):    
    return len(content.split('\n'))  #Counts the number of lines in the text by splitting the content at newline characters (\n).

#Counting Words
def count_words(content):   #Counts the total number of words by splitting the content into words (default split by whitespace).
    return len(content.split())

#Counting Unique Words
def count_unique_words(content):   #Counts unique words by converting the list of words to a set (which automatically removes duplicates).     
    words = content.lower().split()   ##It uses lower() to ensure case insensitivity.
    return len(set(words))

#Finding the Longest Word
def longest_word(content):     #Finds the longest word in the text using max() with the key argument set to len, 
    words = content.split()    #which checks the length of each word. If there are no words, it returns an empty string.
    return max(words, key=len) if words else ""

#Counting Specific Word Occurrences
def count_specific_word(content, word):   #Counts how many times a specific word appears in the text, 
    words = content.lower().split()       #ignoring case by converting both the content and the target word to lowercase.
    return words.count(word.lower())

#Calculating Average Word Length
def average_word_length(content):    #Calculates the average length of words. 
    words = content.split()          #It sums the lengths of all words and divides by the number of words. If there are no words, it returns 0 to avoid division by zero.
    return sum(len(word) for word in words) / len(words) if words else 0

#Calculating Percentage of Long Words
def percentage_long_words(content):         #Calculates the percentage of words that are longer than the average word length. 
    avg_length = average_word_length(content)    #It counts how many words exceed the average length and divides that count by the total number of words.
    words = content.split()
    long_words_count = sum(1 for word in words if len(word) > avg_length)
    return (long_words_count / len(words) * 100) if words else 0

#Finding the Most Common Word
def most_common_word(content):     #Uses Counter from the collections module to find the most frequently occurring word in the text, returning the most common word and its count.    
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

#Analyzing Text
def analyze_text(filename, specific_word):   #This is the main function that orchestrates the analysis. 
    content = read_file(filename)            #It reads the file, calls all the other functions to gather statistics, and prints the results.
    
    if not content:
        return
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    num_unique_words = count_unique_words(content)
    common_word, common_count = most_common_word(content)
    longest = longest_word(content)
    specific_count = count_specific_word(content, specific_word)
    avg_length = average_word_length(content)
    long_word_percentage = percentage_long_words(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Most common word: '{common_word}' (appears {common_count} times)")
    print(f"Longest word: '{longest}'")
    print(f"Occurrences of '{specific_word}': {specific_count}")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Percentage of words longer than average: {long_word_percentage:.2f}%")

# Example of how to run the analysis
specific_word = 'your_word_here'  # Change this to the word you want to count
analyze_text('sample.txt', specific_word)
