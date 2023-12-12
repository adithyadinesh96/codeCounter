import re
from abc import abstractmethod


class CodeCounter:
    def __init__(self):
        self._in_multiline_comment = False
        self._total_lines = 0
        self._blank_lines = 0
        self._comment_lines = 0
        self._code_lines = 0

    @abstractmethod
    def _get_comment_pattern(self) -> re.Pattern:
        pass

    @abstractmethod
    def _get_multiline_comment_start(self) -> str:
        pass

    @abstractmethod
    def _get_multiline_comment_end(self) -> str:
        pass

    @staticmethod
    def _get_blank_line_pattern() -> re.Pattern:
        return re.compile(r"^\s*$")

    def _process_line(self, line) -> None:

        self._total_lines += 1

        if self._get_blank_line_pattern().match(line):
            self._blank_lines += 1
        elif self._in_multiline_comment:
            self._comment_lines += 1
            if self._get_multiline_comment_end() in line:
                self._in_multiline_comment = False

        elif self._get_comment_pattern().match(line):
            self._comment_lines += 1
            if self._get_multiline_comment_start() in line and self._get_multiline_comment_end() not in line:
                self._in_multiline_comment = True
        else:
            self._code_lines += 1
            #Can Extend to detect imports, variable, declarations later

    def count_lines(self, file_path: str):
        # Open the file and process each line
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                self._process_line(line)
        return self._total_lines, self._blank_lines, self._comment_lines, self._code_lines

