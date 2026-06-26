import string

def clean_word(word):
    return word.lower().strip(string.punctuation)

def count_words(text):
    words = text.split()
    frequency = {}
    
    for word in words:
        word = clean_word(word)
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

def show_top_words(frequency, top=5):
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_words[:top]
    
    print("\nTop", top, "most frequent words:")
    print("-" * 30)
    
    for word, count in top_words:
        print(f"  {word:<20} {count}")

def main():
    print("Word Frequency Counter")
    print("=" * 30)
    print("Enter your passage below (press Enter twice when done):\n")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    text = " ".join(lines)
    
    if not text.strip():
        print("No text entered.")
        return
    
    frequency = count_words(text)
    total_words = sum(frequency.values())
    unique_words = len(frequency)
    
    print("\nTotal words typed:", total_words)
    print("Unique words found:", unique_words)
    
    show_top_words(frequency)

main()