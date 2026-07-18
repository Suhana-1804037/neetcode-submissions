class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes = []
        ans = []

        for string in strs:
            sizes.append(len(string))

        for size in sizes:
            ans.append(str(size))
            ans.append(",")

        ans.append("#")
        ans.extend(strs)

        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes = []
        ans = []
        i = 0

        while s[i] != "#":
            j = i

            while s[j] != ",":
                j += 1

            sizes.append(int(s[i:j]))
            i = j + 1

        i += 1  # Skip '#'

        for size in sizes:
            ans.append(s[i:i + size])
            i += size

        return ans