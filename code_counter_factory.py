from typing import Type

from code_counter import CodeCounter
from code_counter_java import CodeCounterJava

_EXT_COUNTER_MAP = {
    "java": CodeCounterJava
}


def get_counter(filename: str) -> Type[CodeCounter]:
    file_extension = filename.split(".")[-1].lower()
    if file_extension not in _EXT_COUNTER_MAP:
        raise ValueError(f"Not Implemented or unsupported file extension: {file_extension}")
    return _EXT_COUNTER_MAP[file_extension]
