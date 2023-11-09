class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        t = 0
        for l in s:
            i = l
            for ind, l in enumerate(s):
                if l == i:
                    t += 1


examples = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
]


for e in examples:
    print(i:=e[0]) 
    print(Solution.firstUniqChar(i))

