from coder import coder
from is_valid_input import is_valid_input


def main():
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
                    encoded_text = coder(input_text, input_key)
                    print("Encoded text: " + encoded_text)
                case "2":
                    decoded_text = coder(input_text, input_key, True)
                    print("Decoded text: " + decoded_text)
                case "3":
                    break
        else:
            break