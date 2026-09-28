import string
import secrets


def show_menu():
    print("\n=== Password Generator ===")
    print("1. Random characters      (unmemorable, works everywhere)")
    print("2. Random word passphrase (memorable, no personal info)")
    print("3. Use my words           (personal, I'll strengthen it)")
    print("4. Quit")
    print()


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


def main():
    while True:
        show_menu()
        choice = input("Choose a mode: ")

        if choice == "1":
            mode_random_characters()
        elif choice == "2":
            print("→ [Mode 2 not built yet]")
        elif choice == "3":
            print("→ [Mode 3 not built yet]")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()