def isIsomorphic(s,t):
    mapST = {}
    mapTS = {}

    for c1, c2 in zip(s, t):
        if c1 in mapST and mapST[c1] != c2:
            return False
        if c2 in mapTS and mapTS[c2] != c1:
            return False

        mapST[c1] = c2
        mapTS[c2] = c1

    return True


def isIsomorphic_2(s,t):
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

s = "egg"
t = "att"
output = isIsomorphic(s, t)
print("Output : ", output)
