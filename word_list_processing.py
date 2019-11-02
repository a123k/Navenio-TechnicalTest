from collections import Counter


def word_list_processing(list_of_list):
    """
    Identifies words that appear in more than one list,
    total number of unique words across all lists,
    top five frequent words in the all lists from single list consists of list of words
    :param list_of_list: single list consists of any number of lists (1..n),
    :return:
    """

    unique_words = set()
    all_words = []

    for individual_list in list_of_list:
        unique_words_in_list = set(individual_list)
        unique_words.update(unique_words_in_list)
        for word_in_list in unique_words_in_list:
            all_words.append(word_in_list)

    no_of_unique_words = len(unique_words)

    print("The total number of unique words across all lists", no_of_unique_words)

    #  Top five frequent words in the all lists
    counter = Counter(all_words)
    top_five_frequent_occurrence = counter.most_common(5)
    for word_count in top_five_frequent_occurrence:
        print(word_count[0], "-", word_count[1])

    # Words that appear in more than one list
    most_occurrence_of_all_words = counter.most_common(len(unique_words))
    words_in_more_than_one_list = []
    for word_count in most_occurrence_of_all_words:
        if word_count[1] > 1:
            words_in_more_than_one_list.append(word_count[0])
    print('Words appearing in more than one list', words_in_more_than_one_list)

    return words_in_more_than_one_list, no_of_unique_words, top_five_frequent_occurrence


if __name__ == "__main__":

    word_list = [
        ['Apple', 'Banana', 'Pineapple', 'Pineapple'],
        ['Apple', 'Cherry', 'Banana', 'Grapefruit'],
        ['Passion fruit', 'Apple', 'Apple', 'Guava'],
        ['Apricot', 'Blueberry', 'Eggfruit', 'Apple'],
        ['Grapefruit', 'Guava', 'Mango', 'Kiwi'],
    ]

    expected_words_in_more_than_one_list = ['Apple', 'Banana', 'Grapefruit', 'Guava']
    expected_no_of_unique_words = 12
    expected_top_five_frequent_occurrence = [('Apple', 4), ('Banana', 2), ('Grapefruit', 2), ('Guava', 2), ('Pineapple', 1)]
    actual_words_in_more_than_one_list, \
    actual_no_of_unique_words, \
    actual_top_five_frequent_occurrence = word_list_processing(word_list)

    assert (expected_words_in_more_than_one_list == actual_words_in_more_than_one_list), \
        'Expected list of word appeared in more than once is not matching with actual list'

    assert (expected_no_of_unique_words == actual_no_of_unique_words), \
        'Expected no of unique words is not matching with actual no of unique words'

    assert (expected_top_five_frequent_occurrence == actual_top_five_frequent_occurrence), \
        'Expected list of top five occurrence is not matching with actual list'

