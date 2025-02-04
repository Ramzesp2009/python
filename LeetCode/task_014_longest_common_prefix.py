# strs = ['start', 'stop', 'step', 'strange']
# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs = ["cir","car"]

# index = 0
# long = len(strs)
# res = []
# liste = [[i for i in word]for word in strs]
# new_liste = list(zip(*liste))
# for i in new_liste:
#     if len(set(i)) == 1:
#         res.append(set(i))
#     else:
#         break
# result = ''.join(item.pop() for item in res)
#
# print(result)



class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = []
        liste = [[i for i in word]for word in strs]
        new_liste = list(zip(*liste))
        for i in new_liste:
            if len(set(i)) == 1:
                res.append(set(i))
            else:
                break
        return ''.join(item.pop() for item in res)


