def rearrangeArray(nums):
        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res

if __name__ == "__main__":
     nums = [3,1,-2,-5,2,-4]
     print("rearrange array : ", rearrangeArray(nums))