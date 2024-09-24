class File:
    @staticmethod
    def read_lines(file):
        with open(file, "r") as fin:
            lines = fin.readlines()
        return lines

    @staticmethod
    def read(file):
        with open(file, "r") as fin:
            line = fin.read()
        return line

    @staticmethod
    def write(file, output):
        with open(file, "w") as fout:
            fout.write(output)
        return
