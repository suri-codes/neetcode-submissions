class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        base = ""
        for string in strs:
            base += f"{len(string)},"
        base += "$"
        for string in strs:
            base += string
        print(base)
        return base
 
    def decode(self, s: str) -> List[str]:
        delim_idx = s.find("$")
        sizes_str = s[:delim_idx]
        sizes = sizes_str.split(",")
        print(sizes)
        word_start = delim_idx+1
        words = []
        for size in sizes[:-1]:
            size = int(size)
            words.append(s[word_start:word_start + size])
            word_start = word_start+size
        return words
            

        
        
