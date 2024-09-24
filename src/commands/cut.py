from typing import Optional
from commands.command import Command
from exceptions import FlagError
from exceptions import FlagValueError
from utils.file import File
from utils.validator import Validator


class Cut(Command):

    def execute(self, args: list[str], stdin: Optional[list[str]] = None):
        cut_options, lines = self.validate_flags(args, stdin)
        output = []

        for line in lines:
            # split 2-3,5,-2 to [2-3, 5,-2]
            options = cut_options.split(',')

            # process [2-3, 5, -2] to [(2,3), (5,5), (0,2)]
            option_ranges = self.pre_process_ranges(options, len(line))

            # Merge [(2,3), (5,5), (0,2)] to [(0,3), (5,5)]
            merged_ranges = self.merge_intervals(option_ranges)

            # slice the line as per merged cut-intervals
            output.append(''.join(self.slice_line(merged_ranges, line)))

        return '\n'.join(output)

    @staticmethod
    def validate_flags(args, stdin) -> tuple[str, list[str]]:
        """
        Validate the flags given in the command line.
        Raises:
            FlagError: If the flag given is not -b.
            FlagError: If the file does not exist.
            FlagError: If the number of flags given is not 1 or 2.
        """
        num_args = len(args)
        if num_args == 2:
            Validator.check_flag(args[0], "-b")
            cut_options = args[1]
            lines = [
                item for line in stdin for item in line.split("\n") if item
            ]
        elif num_args == 3:
            Validator.check_flag(args[0], "-b")
            cut_options = args[1]
            Validator.check_path_exists(args[2])
            lines = File.read_lines(args[2])
            lines = [line.rstrip('\n') for line in lines]
        else:
            raise FlagError("Error: Wrong number of flags given")
        return cut_options, lines

    def pre_process_ranges(self, option_ranges: list[str],
                           line_len: int) -> list[tuple[int, int]]:
        """
        Changes cut bytes option_ranges into indices for slicing
        Raises:
            FlagValueError: If the range is not in the correct format.
        """
        option_range = []
        for option in option_ranges:
            if '-' in option:
                range_split = option.split('-')
                self.is_range_format_valid(range_split)
                left = int(range_split[0]) if range_split[0] else 0
                right = int(range_split[1]) if range_split[1] else line_len
                option_range.append((left, right))
            else:
                if not option.isdigit():
                    raise FlagValueError(
                        "Error: Invalid cut option format"
                    )
                num = int(option)
                option_range.append((num, num))
        return option_range

    @staticmethod
    def is_range_format_valid(range_split: list[str]) -> None:
        if len(range_split) != 2:
            raise FlagValueError("Error: Invalid cut option format")
        if range_split[0]:
            Validator.check_string_isdigit(range_split[0])
        if range_split[1]:
            Validator.check_string_isdigit(range_split[1])

    @staticmethod
    def merge_intervals(option_ranges: list[tuple[int, int]])\
            -> list[tuple[int, int]]:
        """
        Merge the overlapping cut option ranges to get distinct cut bytes
        """
        option_ranges.sort()
        start, end = option_ranges[0]
        resultant_range = []
        for curr_start, curr_end in option_ranges[1:]:
            if end < curr_start:
                resultant_range.append((start, end))
                start = curr_start
            end = max(curr_end, end)
        resultant_range.append((start, end))
        return resultant_range

    @staticmethod
    def slice_line(resultant_range: list[tuple[int, int]], line: str)\
            -> list[str]:
        result_line = []
        for cur_range in resultant_range:
            cut_left = cur_range[0] - 1 if cur_range[0] != 0 else 0
            cut_right = cur_range[1]
            result_line.append(line[cut_left:cut_right])
        return result_line
