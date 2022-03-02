from cs50 import get_string


def main():
    # Ask user for text
    text = get_string("Text: ")

    # Store letter, words, sentences
    letters = 0
    words = 1
    sentences = 0

    # Loop through text to find letters, word, sentences
    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
        elif text[i] == " ":
            words += 1
        elif text[i] == "." or text[i] == "?" or text[i] == "!":
            sentences += 1

    # Coleman-Liau formula
    L = float(letters) / float(words) * 100
    S = float(sentences) / float(words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    grade_index = round(index)

    # Grade text input
    if grade_index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade_index}")


if __name__ == "__main__":
    main()
