def calculate_letter_ratio(word_list, pos1, pos2):
    # Initialize dictionaries to keep track of letter counts
    letter_counts_pos1 = {}
    letter_counts_pos2 = {}
    
    # Iterate through the list of words
    for word in word_list:
        # Check if the word has the specified positions (1-indexed)
        if len(word) >= max(pos1, pos2):
            # Increment letter counts
            letter_counts_pos1[word[pos1 - 1]] = letter_counts_pos1.get(word[pos1 - 1], 0) + 1
            letter_counts_pos2[word[pos2 - 1]] = letter_counts_pos2.get(word[pos2 - 1], 0) + 1
    
    # Create a dictionary for the ratios
    ratio_dict = {}
    
    # Iterate through the letters found in the first specified position
    for letter, count_pos1 in letter_counts_pos1.items():
        # Check if the letter was also found in the second specified position
        count_pos2 = letter_counts_pos2.get(letter, 0)
        if count_pos2 > 0:
            # Calculate the ratio and add it to the ratio dictionary
            ratio_dict[letter] = round(count_pos1 / count_pos2, 2)
    
    return ratio_dict

# Load the word list from the provided file
with open('google-10000-english-usa-no-swears.txt', 'r') as file:
    word_list = [line.strip() for line in file]

    # Call the function with the first and third positions (1-indexed)
    letter_ratios = calculate_letter_ratio(word_list, 1, 3)
    print(letter_ratios['a'])
