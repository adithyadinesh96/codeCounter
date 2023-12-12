import os

from code_counter_factory import get_counter


def process_files(directory_path: str) -> None:
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"\nProcessing: {file_path}")
            total_lines, blank_lines, comment_lines, code_lines = get_counter(
                filename=file_path.split('/')[-1])().count_lines(
                file_path=file_path)
            print(f"Total lines: {total_lines}")
            print(f"Blank lines: {blank_lines}")
            print(f"Comment lines: {comment_lines}")
            print(f"Code lines: {code_lines}")


if __name__ == '__main__':
    process_files("./tests/code_files")
