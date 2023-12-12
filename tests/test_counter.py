import os
import unittest

from code_counter_factory import get_counter

_TEST_JAVA = '''import java.util.*;

// file created on 1st Jan 2020
// author: @openenvoy

public class Main {

// This is another comment line
public static void main(String[] args) {
System.out.println("Hello world!"); // code, not comment 11
}
}
'''


class TestCounter(unittest.TestCase):

    def test_count(self):
        with open("code_files/java/test.java", 'w') as f:
            f.write(_TEST_JAVA)
        total_lines, blank_lines, comment_lines, code_lines = get_counter(filename="code_files/java/test.java")().count_lines(
            file_path="code_files/java/test.java")
        self.assertEqual(total_lines, 12)
        self.assertEqual(blank_lines, 3)
        self.assertEqual(comment_lines, 3)
        self.assertEqual(code_lines, 6)

    def tearDown(self):
        os.remove("code_files/java/test.java")
