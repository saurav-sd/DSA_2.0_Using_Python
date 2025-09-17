class NoteCount:
    def noteCount(self, amount):
        denominations = [500, 100, 50, 20, 10, 5, 2, 1]

        for note in denominations:
            count = amount // note
            if count > 0:
                print(f"Rs. {note} : {count}")
                amount = amount % note


# Example usage
if __name__ == "__main__":
    amount = int(input("Enter the amount: "))
    note_count = NoteCount()
    note_count.noteCount(amount)
