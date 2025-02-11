import random
import argparse  # Import argparse to handle command-line arguments

def read_words(file_path):
    """Read words from a file and filter them based on length."""
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file if 4 <= len(line.strip()) <= 8]
    return words

def select_random_words(words, count=5):
    """Select a specified number of random words from a list."""
    return random.sample(words, count)

def change_words_to_uppercase(words, count):
    """Change a specified number of words to uppercase."""
    indices = random.sample(range(len(words)), count)
    for index in indices:
        words[index] = words[index].upper()
    return words

def generate_random_hex():
    """Generate a random hexadecimal number with 4 digits."""
    return f"{random.randint(1, 0xFFFF):04X}"

def generate_password(file_path):
    """Generate a password based on the specifications."""
    words = read_words(file_path)
    selected_words = select_random_words(words)
    x = random.randint(1, 4)
    modified_words = change_words_to_uppercase(selected_words, x)
    hex_number = generate_random_hex()
    password = '-'.join(modified_words + [hex_number])
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random passwords.")
    parser.add_argument('count', nargs='?', type=int, default=5, help='Number of passwords to generate')
    args = parser.parse_args()

    file_path = 'words_alpha.txt'
    for _ in range(args.count):
        password = generate_password(file_path)
        print(password)
