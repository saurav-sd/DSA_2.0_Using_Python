from collections import defaultdict

def charReplacement(str, k):
    count = defaultdict(int)
    left = 0
    max_freq = 0
    res = 0

    for right in range(len(str)):
        count[str[right]] += 1
        max_freq = max(max_freq, count[str[right]])

        while (right - left + 1) - max_freq > k:
            count[str[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res
# ----------------------------
# Time  = O(N)
# Space  = O(1) or O(K)

str = "AABABBA"
k = 1
output = charReplacement(str, k)

print("Output : ", output)
