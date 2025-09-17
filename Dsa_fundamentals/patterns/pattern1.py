class Pattern1:
    # def __init__(self, name):
    #     self.name = name

    def display(self):
        for i in range(0,4):
            for j in range(0,4):
                print("* ", end="")
            print()

pattern = Pattern1()
pattern.display()