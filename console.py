from coder import coder
from save_to_file import save
from is_valid_input import is_valid_input


def main():
    text = ""
    while True:
        prompt = input("1 - Encode text, 2 - Decode text\n"
                       "Your choice: ")
        if prompt in ["1", "2"]:
            input_text = input("Enter the text: ").upper()
            if not is_valid_input(input_text):
                print("Wrong text format, please try again.")
                continue
            input_key = input("Enter the key: ").upper()
            if not is_valid_input(input_key):
                print("Wrong key format, please try again.")
                continue
            match prompt:
                case "1":
                    text = coder(input_text, input_key)
                    print("Encoded text: " + text)
                case "2":
                    text = coder(input_text, input_key, True)
                    print("Decoded text: " + text)
                case "3":
                    break
            save_input = input("Would you like to save the input? (y/n): ").upper()
            if save_input in ["Y", "YES"]:
                save(text)
        else:
            break