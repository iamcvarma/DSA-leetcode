class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res=0
        flag=0
        freq = Counter(words)
        for word in freq:
            if freq[word[::-1]]>0:
                if word[0]==word[1]:
                    res+=(freq[word]//2)*2
                    if flag==0:
                        flag = freq[word]%2
                else:
                    res+=min(freq[word],freq[word[::-1]])*2
                    freq[word]=0
        return (res+flag)*2