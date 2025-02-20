import argparse
import itertools

def generate_passwords(words, repeat, output_file):
    temp = itertools.product(words, repeat=repeat)

    with open(output_file, "a") as passwords:
        for i in temp:
            passwords.write("".join(i))  
            passwords.write("\n")

def main():
    parser = argparse.ArgumentParser(description="Generate password dictionaries based on specified parameters.")
    
    parser.add_argument(
        "-w", "--words", 
        type=str, 
        required=True, 
        help="The characters to use for password generation (e.g., '01234' or 'abcdefg')."
    )
    parser.add_argument(
        "-r", "--repeat", 
        type=int, 
        required=True, 
        help="Length of the generated password (e.g., 2 for two-digit passwords)."
    )
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        required=True, 
        help="Output file to save the generated passwords (e.g., '1.txt')."
    )
    
    args = parser.parse_args()

    generate_passwords(args.words, args.repeat, args.output)

if __name__ == '__main__':
    main()
