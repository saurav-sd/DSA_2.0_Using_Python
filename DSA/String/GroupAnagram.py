from collections import defaultdict

def groupAnagram(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        # option 1
        # key = "".join(sorted(word))

        # option 2
        key = [0]*26
        for c in word:
            key[ord(c) - ord('a')] += 1
        key = tuple(key)

        anagram_map[key].append(word)

    return list(anagram_map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(strs))