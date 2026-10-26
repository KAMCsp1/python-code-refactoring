"""Process a list of numbers and a list of words, then print the results.

Even numbers are doubled and odd numbers are tripled. Words with six or
more letters are made uppercase and shorter words are made lowercase.
"""

# The rules are stored here so they can be changed in one place.
EVEN_MULTIPLIER = 2
ODD_MULTIPLIER = 3
LONG_WORD_MIN_LENGTH = 6  # Minimum length for a word to be uppercased.


def process_numbers(numbers):
    """Double even numbers and triple odd numbers.

    Args:
        numbers: An iterable of integers.

    Returns:
        A new list with the processed numbers, in the same order.
    """
    return [
        number * (EVEN_MULTIPLIER if number % 2 == 0 else ODD_MULTIPLIER)
        for number in numbers
    ]


def format_words_by_length(words):
    """Uppercase long words, lowercase short ones, and join them with spaces.

    Args:
        words: An iterable of strings.

    Returns:
        One string with the words separated by spaces.
    """
    return " ".join(
        word.upper() if len(word) >= LONG_WORD_MIN_LENGTH else word.lower()
        for word in words
    )


def main():
    """Process the sample lists and print the results."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    fruits = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    print("Processed Numbers:", process_numbers(numbers))
    print("Processed Strings:", format_words_by_length(fruits))


if __name__ == "__main__":
    main()
