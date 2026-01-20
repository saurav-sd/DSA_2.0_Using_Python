class FindDatatypeofCharactor:
    def find_datatype(ch):
        if len(ch) != 1:
            return "Invalid input. Please enter a single character."
        if ch.isalpha():
            return "Alphabet"
        elif ch.isdigit():
            return "Digit"
        elif ch in ['+', '-', '*', '/', '%', '=', '!', '@', '#', '$', '^', '&', '(', ')', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?']:
            return "Special Character"
        else:
            return "Unknown character type"
        

# Example usage 
if __name__ == "__main__":
    ch = input("Enter a character: ")
    result = FindDatatypeofCharactor.find_datatype(ch)
    print(f"The character '{ch}' is of type: {result}")