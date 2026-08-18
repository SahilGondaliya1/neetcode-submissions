class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input constraints:
        # string length = 10^4
        # create two tupples and then compare it
        tuple1= tuple(sorted(list(s)))
        tuple2= tuple(sorted(list(t)))
        if tuple1 == tuple2:
            return True
        return False