class MaxNumber:
    def findMax(self, num1, num2, num3):
        """
        This function takes three numbers and returns the maximum of the three.
        :param num1: First number
        :param num2: Second number
        :param num3: Third number
        :return: The maximum of the three numbers
        """
        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3
        

# Example usage
# if __name__ == "__main__":
#     max_number = MaxNumber()
#     print(max_number.findMax(10, 20, 30))  # Output: 30
#     print(max_number.findMax(5, 3, 8))     # Output: 8
#     print(max_number.findMax(-1, -2, -3))  # Output: -1

max_number = MaxNumber()
print(max_number.findMax(10, 20, 30))  # Output: 30