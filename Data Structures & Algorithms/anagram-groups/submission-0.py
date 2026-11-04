class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to List of Anagrams

        for n in strs:
            count = [0] * 26 #a ... z

            for c in n:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(n)

        return list(res.values())

            
        