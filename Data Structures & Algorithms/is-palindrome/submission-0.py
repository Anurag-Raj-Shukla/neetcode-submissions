class Solution:

    def isPalindrome(self, s: str) -> bool:
        # Keep only letters and numbers, then make them lowercase
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())

        # Check if the clean string equals its reverse
        return cleaned == cleaned[::-1]
