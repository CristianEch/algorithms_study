
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    dic_1 = {chr(number): 0 for number in range(ord("a"), ord("z") + 1)}
    dic_2 = {chr(number): 0 for number in range(ord("a"), ord("z") + 1)}
    if len(s) != len (t):
        return False
    else:
            
        for n in range(len(s)):
            dic_1[s[n]] += 1
            dic_2[t[n]] += 1

        if dic_1 == dic_2:
            return True
        else:
            return False
        