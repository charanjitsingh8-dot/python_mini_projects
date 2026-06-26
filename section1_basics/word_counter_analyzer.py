def analyze_text(paragraph):
    words = paragraph.split()
    word_count = len(words)

    longest_word = ""
    for word in words:
        clean_word = word.strip(".,!?;:\"'")
        if len(clean_word) > len(longest_word):
            longest_word = clean_word

    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in paragraph:
        if char in vowels:
            vowel_count += 1

    total_length = 0
    for word in words:
        clean_word = word.strip(".,!?;:\"'")
        total_length += len(clean_word)

    if word_count > 0:
        avg_length = total_length / word_count
    else:
        avg_length = 0

    letter_count = {}
    for word in words:
        if word:
            first_letter = word[0].lower()
            if first_letter.isalpha():
                if first_letter in letter_count:
                    letter_count[first_letter] += 1
                else:
                    letter_count[first_letter] = 1

    most_common_letter = ""
    max_count = 0
    for letter in letter_count:
        if letter_count[letter] > max_count:
            max_count = letter_count[letter]
            most_common_letter = letter

    return word_count, longest_word, vowel_count, avg_length, most_common_letter, max_count


def main():
    print("=" * 45)
    print("       Word Counter & Analyzer")
    print("=" * 45)

    while True:
        print("\nEnter a paragraph to analyze")
        print("(or type 'exit' to quit)")
        print("-" * 45)

        paragraph = input("Your text: ").strip()

        if paragraph.lower() == "exit":
            print("\nGoodbye!")
            break

        if len(paragraph) == 0:
            print("Please enter some text!\n")
            continue

        word_count, longest_word, vowel_count, avg_length, common_letter, letter_freq = analyze_text(paragraph)

        print("\n" + "=" * 45)
        print("           ANALYSIS REPORT")
        print("=" * 45)
        print(f"  Total Words        : {word_count}")
        print(f"  Total Characters   : {len(paragraph)}")
        print(f"  Total Vowels       : {vowel_count}")
        print(f"  Longest Word       : '{longest_word}' ({len(longest_word)} letters)")
        print(f"  Avg Word Length    : {avg_length:.2f} letters")
        print(f"  Most Common Start  : '{common_letter.upper()}' ({letter_freq} words)")
        print("=" * 45)

        again = input("\nAnalyze another paragraph? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThank you for using Word Analyzer. Goodbye!")
            break


main()