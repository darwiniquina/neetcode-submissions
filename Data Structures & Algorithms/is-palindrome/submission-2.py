class Solution:
    def isPalindrome(self, s: str) -> bool:

        # cleaned_text = "".join(filter(str.isalnum, s))
        # reversed_text = cleaned_text[::-1]

        # return cleaned_text.lower() == reversed_text.lower()

        parsed_text = ''
        parsed_text_compare = ''
        
        left = 0
        right = len(s)

        for i in range(right):
            left_char_s = s[left]
            right_char_s = s[right - 1]

            if (left_char_s.isalnum()):
                parsed_text += left_char_s.lower()
            
            if (right_char_s.isalnum()):
                parsed_text_compare += right_char_s.lower()

            left+= 1
            right-= 1

        return parsed_text == parsed_text_compare