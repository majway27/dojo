import unittest

# Returns the first character of the string str
def first_character(my_str):
    return my_str[:1]

# Returns the last character of a string str
def last_character(my_str):
    return my_str[-1:]

# Returns the string that results from removing the first
# and last characters from str
def middle_characters(my_str):
    return my_str[1:-1]


def is_palindrome(my_str):
    # base case #1
    if len(my_str) <= 1:
        return True
    # base case #2
    if first_character(my_str) != last_character(my_str):
        return False
    # recursive case
    input = middle_characters(my_str)
    print('Testing input: ' + input + ' this round.')
    return is_palindrome(input)


def check_palindrome(my_str):
    print("Is this word a palindrome? " + my_str)
    return is_palindrome(my_str)


class PalindromeTestCases(unittest.TestCase):

    def test_check_palindrome_1(self):
        self.assertEqual(check_palindrome("a"), True)

    def test_check_palindrome_2(self):
        self.assertEqual(check_palindrome("motor"), False)

    def test_check_palindrome_3(self):
        self.assertEqual(check_palindrome("rotor"), True)

    def test_check_palindrome_4(self):
        self.assertEqual(check_palindrome("poolloop"), True)

    def test_check_palindrome_5(self):
        self.assertEqual(check_palindrome("pooeloop"), False)


if __name__ == "__main__":
    unittest.main()
