import re

from code_counter import CodeCounter


class CodeCounterJava(CodeCounter):

    def _get_comment_pattern(self) -> re.Pattern:
        return re.compile(r"^\s*//|^\s*/\*|^\s*\*|^\s*\*/")

    def _get_multiline_comment_start(self) -> str:
        return "/*"

    def _get_multiline_comment_end(self) -> str:
        return "*/"
