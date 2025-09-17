class LargestElement:
    def find_largest(self, array):
        if not array:
            return None
        largest = array[0]
        for num in array:
            if num > largest:
                largest = num
        return largest
    

class SmallestElement:
    def find_smallest(self , array):
        smallest = array[0]
        for num in array:
            if num < smallest:
                smallest = num
        return smallest
    
# Example usage:
# if __name__ == "__main__":
#     le = LargestElement()
#     sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
#     print("The largest element is:", le.find_largest(sample_array))


if __name__ == "__main__":
    le = SmallestElement()
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("The smallest element is:", le.find_smallest(sample_array))