# List : Changeable / Ordered / Allows duplicates

skills  = ["React", "python", "Nextjs"]
skills.append("FastApi")
skills.append("React")
skills[1] = "ReactJs"
print(skills)

skills.remove("React")
print(skills)

skills.pop()
print(skills)

print(len(skills))