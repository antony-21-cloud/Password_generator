import string
import secrets


def show_menu():
    print("\n=== Password Generator ===")
    print("1. Random characters      (unmemorable, works everywhere)")
    print("2. Random word passphrase (memorable, no personal info)")
    print("3. Use my words           (personal, I'll strengthen it)")
    print("4. Quit")
    print()


def load_words(filename):
    """Read a diceware-style wordlist and return a list of just the words."""
    words = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                words.append(parts[1])
    return words


def mode_random_characters():
    print("\n--- Random Character Password ---")

    length = int(input("Length (recommended 16+): "))

    include_letters = input("Include letters? (y/n): ").lower() == "y"
    include_numbers = input("Include numbers? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"

    pool = ""
    if include_letters:
        pool += string.ascii_letters
    if include_numbers:
        pool += string.digits
    if include_symbols:
        pool += string.punctuation

    if not pool:
        print("You must include at least one character type.")
        return

    password = "".join(secrets.choice(pool) for _ in range(length))
    print(f"\nGenerated password: {password}")


def mode_word_passphrase():
    print("\n--- Random Word Passphrase ---")

    try:
        words = load_words("wordlist.txt")
    except FileNotFoundError:
        print("Error: wordlist.txt not found in this folder.")
        return

    count = int(input("How many words? (recommended 4-6): "))
    print("Separator:")
    print("  1. Dash  -")
    print("  2. Space")
    print("  3. Dot   .")
    print("  4. None")
    sep_choice = input("Choose [1]: ") or "1"
    separator = {"1": "-", "2": " ", "3": ".", "4": ""}.get(sep_choice, "-")
    add_number = input("Add a random number at the end? (y/n): ").lower() == "y"

    chosen = [secrets.choice(words) for _ in range(count)]
    password = separator.join(chosen)

    if add_number:
        password += separator + str(secrets.randbelow(100))

    print(f"\nGenerated passphrase: {password}")


def mode_use_my_words():
    print("\n--- Use My Words ---")
    print("⚠️  Note: Personal words are easier to guess if someone knows you.")
    print("    For maximum security, use modes 1 or 2.")
    print("    This mode is for passwords you want to remember.\n")

    try:
        words = load_words("wordlist.txt")
    except FileNotFoundError:
        print("Error: wordlist.txt not found in this folder.")
        return

    user_input = input("Enter your word(s), space-separated: ").strip()
    if not user_input:
        print("You must enter at least one word.")
        return
    user_words = user_input.split()

    count = int(input("How many random words to add? (recommended 3-5): "))
    print("Separator:")
    print("  1. Dash  -")
    print("  2. Space")
    print("  3. Dot   .")
    print("  4. None")
    sep_choice = input("Choose [1]: ") or "1"
    separator = {"1": "-", "2": " ", "3": ".", "4": ""}.get(sep_choice, "-")
    add_number = input("Add a random number at the end? (y/n): ").lower() == "y"

    random_words = [secrets.choice(words) for _ in range(count)]
    all_words = user_words + random_words

    # Secure shuffle so user words aren't always first
    secrets.SystemRandom().shuffle(all_words)

    password = separator.join(all_words)

    if add_number:
        password += separator + str(secrets.randbelow(100))

    print(f"\nGenerated password: {password}")


def main():
    while True:
        show_menu()
        choice = input("Choose a mode: ")

        if choice == "1":
            mode_random_characters()
        elif choice == "2":
            mode_word_passphrase()
        elif choice == "3":
            mode_use_my_words()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()