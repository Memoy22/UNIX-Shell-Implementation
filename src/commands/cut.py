from commands.command import Command
from exceptions import FlagError
from exceptions import InvalidFormatError
from utils import File
from utils import Validator


class Cut(Command):

    def pre_process_ranges(self, option_ranges, line_len):
        """ Pre-process the ranges given in the cut options.
        Args:
            option_ranges (list): List of strings containing the ranges.
            line_len (int): Length of the line.
        Returns:
            list: List containing the processed ranges.
        Raises:
            InvalidFormatError: If the range is not in the correct format.
        """
        option_range = []
        for option in option_ranges:
            if '-' in option:
                range_split = option.split('-')
                self.check_range_format(range_split)
                left = int(range_split[0]) if range_split[0] else 0
                right = int(range_split[1]) if range_split[1] else line_len
                option_range.append((left, right))
            else:
                if not option.isdigit():
                    raise InvalidFormatError("Error: Invalid cut option "
                                             "format")
                num = int(option)
                option_range.append((num, num))
        return option_range

    def execute(self, args, stdin=None):
        cut_options, lines = self.validate_flags(args, stdin)

        lines = [line.rstrip('\n') for line in lines]
        output = []

        for line in lines:
            option_ranges = cut_options.split(',')

            # Pre-process ranges and put them in option_range: list[tuple]
            option_range = self.pre_process_ranges(option_ranges, len(line))

            # Merge for overlapping intervals
            resultant_range = self.merge_intervals(option_range)

            # slice the line as per merged cut-intervals
            output.append(''.join(self.slice_line(resultant_range, line)))

        # print(output)
        return '\n'.join(output)

    @staticmethod
    def validate_flags(args, stdin):
        """ Validate the flags given in the command line.
        Args:
            args (list): List of arguments given in the command line.
            stdin (list): List of lines from standard input.
        Returns:
            tuple: Tuple containing the cut options and lines
        Raises:
            FlagError: If the flag given is not -b.
            FlagError: If the file does not exist.
            FlagError: If the number of flags given is not 1 or 2.
        """
        num_args = len(args)
        if num_args == 2:
            Validator.check_flag(args[0], "-b")
            cut_options = args[1]
            lines = stdin
        elif num_args == 3:
            Validator.check_flag(args[0], "-b")
            cut_options = args[1]
            Validator.check_path_exists(args[2])
            lines = File(args[2]).read_lines()
        else:
            raise FlagError("Error: Wrong number of flags given")
        return cut_options, lines

    @staticmethod
    def check_range_format(range_split):
        """ Check if the given range is valid.
        Args:
            range_split (list): List of strings containing the range.
        Raises:
            InvalidFormatError: If the range is not in the correct format.
        """
        if len(range_split) != 2:
            raise InvalidFormatError("Error: Invalid cut option format")
        if range_split[0]:
            Validator.check_string_isdigit(range_split[0])
        if range_split[1]:
            Validator.check_string_isdigit(range_split[1])

    @staticmethod
    def merge_intervals(option_range):
        """ Merge the overlapping intervals.
        Args:
            option_range (list): List containing the processed ranges.
        Returns:
            list: List containing the merged ranges.
        """
        option_range.sort()
        start, end = option_range[0]
        resultant_range = []
        for curr_start, curr_end in option_range[1:]:
            if end < curr_start:
                resultant_range.append((start, end))
                start = curr_start
            end = max(curr_end, end)
        resultant_range.append((start, end))
        return resultant_range

    @staticmethod
    def slice_line(resultant_range, line):
        """ Slice the line as per the merged cut-intervals.
        Args:
            resultant_range (list): List containing the merged ranges.
            line (str): Line to be sliced.
        Returns:
            list: List containing the sliced line.
        """
        result_line = []
        for cur_range in resultant_range:
            cut_left = cur_range[0] - 1 if cur_range[0] != 0 else 0
            cut_right = cur_range[1]
            result_line.append(line[cut_left:cut_right])
        return result_line
