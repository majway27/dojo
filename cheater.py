# coding exercises, https://codingbat.com
import unittest

"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation.
Return True if we sleep in.
"""


def sleep_in(weekday, vacation):
    if vacation:
        return True
    elif not weekday:
        return True
    else:
        return False


"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
We are in trouble if they are both smiling or if neither of them is smiling. 
Return True if we are in trouble.
"""


def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False


"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
"""


def sum_double(a, b):
    val = a + b
    if a == b:
        return val*2
    return val


"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
"""


def diff21(n):
    val = abs(n - 21)
    if n > 21:
        val = val*2
    return val


"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
Return True if we are in trouble.
"""


def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking:
        return True
    else:
        return False


"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
"""


def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False


"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
"""


def near_hundred(n):
    if (90 <= n <= 110) or (190 <= n <= 210):
        return True
    else:
        return False


"""
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.
"""


def pos_neg(a, b, negative):
    if a < 0 or b < 0:
        if not negative and not (a < 0 and b < 0):
            return True
        # negative == True
        elif negative and (a < 0 and b < 0):
            return True
        else:
            return False
    return False


"""
Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.
"""


def not_string(my_str):
    if my_str[:3] == 'not':
        return my_str
    else:
        return 'not ' + my_str


"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string 
(i.e. n will be in the range 0..len(str)-1 inclusive).
"""


def missing_char(my_str, n):
    output = ""
    for i in range(len(my_str)):
        if i != n:
            output = output + my_str[i]
    return output


"""
Given a string, return a new string where the first and last chars have been exchanged.
"""


def front_back(my_str):
    if len(my_str) > 1:
        return my_str[-1:] + my_str[1:-1] + my_str[0:1]
    else:
        return my_str


"""
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.
"""


def front3(my_str):
    if len(my_str) < 3:
        front = my_str + my_str + my_str
    else:
        pre = my_str[0:3]
        front = pre + pre + pre
    return front


class TestCodingBatExercises(unittest.TestCase):

    # sleep_in
    def test_sleep_in_1(self):
        self.assertEqual(sleep_in(False, False), True)

    def test_sleep_in_2(self):
        self.assertEqual(sleep_in(True, False), False)

    def test_sleep_in_3(self):
        self.assertEqual(sleep_in(False, True), True)

    def test_sleep_in_4(self):
        self.assertEqual(sleep_in(True, True), True)

    # monkey_trouble
    def test_monkey_trouble_1(self):
        self.assertEqual(monkey_trouble(True, True), True)

    def test_monkey_trouble_2(self):
        self.assertEqual(monkey_trouble(False, False), True)

    def test_monkey_trouble_3(self):
        self.assertEqual(monkey_trouble(True, False), False)

    # sum_double
    def test_sum_double_1(self):
        self.assertEqual(sum_double(1, 2), 3)

    def test_sum_double_2(self):
        self.assertEqual(sum_double(3, 2), 5)

    def test_sum_double_3(self):
        self.assertEqual(sum_double(2, 2), 8)

    # diff21
    def test_diff21_1(self):
        self.assertEqual(diff21(19), 2)

    def test_diff21_2(self):
        self.assertEqual(diff21(10), 11)

    def test_diff21_3(self):
        self.assertEqual(diff21(21), 0)

    # parrot_trouble
    def test_parrot_trouble_1(self):
        self.assertEqual(parrot_trouble(True, 6), True)

    def test_parrot_trouble_2(self):
        self.assertEqual(parrot_trouble(True, 7), False)

    def test_parrot_trouble_3(self):
        self.assertEqual(parrot_trouble(False, 6), False)

    # makes10
    def test_makes10_1(self):
        self.assertEqual(makes10(9, 10), True)

    def test_makes10_2(self):
        self.assertEqual(makes10(9, 9), False)

    def test_makes10_3(self):
        self.assertEqual(makes10(1, 9), True)

    # near_hundred
    def test_near_hundred_1(self):
        self.assertEqual(near_hundred(93), True)

    def test_near_hundred_2(self):
        self.assertEqual(near_hundred(90), True)

    def test_near_hundred_3(self):
        self.assertEqual(near_hundred(89), False)

    # pos_neg
    def test_pos_neg_1(self):
        self.assertEqual(pos_neg(1, -1, False), True)

    def test_pos_neg_2(self):
        self.assertEqual(pos_neg(-1, 1, False), True)

    def test_pos_neg_3(self):
        self.assertEqual(pos_neg(-4, -5, True), True)

    # not_string
    def test_not_string_1(self):
        self.assertEqual(not_string('candy'), 'not candy')

    def test_not_string_2(self):
        self.assertEqual(not_string('x'), 'not x')

    def test_not_string_3(self):
        self.assertEqual(not_string('not bad'), 'not bad')

    # missing_char
    def test_missing_char_1(self):
        self.assertEqual(missing_char('kitten', 1), 'ktten')

    def test_missing_char_2(self):
        self.assertEqual(missing_char('kitten', 0), 'itten')

    def test_missing_char_3(self):
        self.assertEqual(missing_char('kitten', 4), 'kittn')

    # front_back
    def test_front_back_1(self):
        self.assertEqual(front_back('code'), 'eodc')

    def test_front_back_2(self):
        self.assertEqual(front_back('a'), 'a')

    def test_front_back_3(self):
        self.assertEqual(front_back('ab'), 'ba')

    # front3
    def test_front3_1(self):
        self.assertEqual(front3('Java'), 'JavJavJav')

    def test_front3_2(self):
        self.assertEqual(front3('Chocolate'), 'ChoChoCho')

    def test_front3_3(self):
        self.assertEqual(front3('abc'), 'abcabcabc')


if __name__ == "__main__":
    unittest.main()
