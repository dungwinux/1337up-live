import dis
import marshal
import re

# Before this, you must have AES-decrypted the message and know what to look for

# Load the bytecode along with its debug symbols
with open('funny.pyc', 'rb') as f:
    f.seek(16)
    a = (marshal.load(f))


class VT:
    """Virual text file

    Simulate source file to reconstruct the symbol location.
    """
    _table: list[list[str]] = []
    _regex = re.compile(r"(\w) ", re.IGNORECASE)
    def write(self, coord, data):
        line_n, col_n = coord
        # Dynamically allocate lines and columns
        if len(self._table) <= line_n:
            z1 = line_n - len(self._table) + 1
            self._table.extend([[] for _ in range(z1)])
        if len(self._table[line_n]) <= col_n:
            z2 = col_n - len(self._table[line_n]) + 1
            self._table[line_n].extend([' ' for _ in range(z2)])
        assert len(data) == 1, "{} is too long".format(data)
        self._table[line_n][col_n] = data

    def get(self, coord):
        line_n, col_n = coord
        return self._table[line_n][col_n]

    def __str__(self) -> str:
        res = ''
        for raw_line in self._table:
            cul = ''.join(raw_line)
            actual = self._regex.sub(r"\1;", cul)
            res += actual + '\n'
        return res


vt = VT()
for i in dis.get_instructions(a):
    # We only want to look at the list of variables after AES decryption
    if 2778 > i.offset > 600 and i.opname == "LOAD_NAME":
        pos = i.positions
        # Write out the symbol at the exact location.
        # This assumes the symbol has length of 1
        vt.write((pos.lineno, pos.col_offset), i.argrepr)

# Write to file: key - the ASCII art
with open("reconstruct.txt", "w") as fd:
    fd.write(str(vt))

# Print to stdout: iv - character in the ASCII art
iv_mapper = [(476, 6), (468, 5), (282, 6), (506, 6), (420, 3), (492, 0), (192, 6), (56, 6), (144, 3), (324, 0), (360, 1), (352, 6), (30, 1), (260, 0), (298, 1), (480, 3)]
# vscode_mapper = [(y + 25, x + 1) for (x, y) in iv_mapper]
actual_mapper = [(y + 24, x) for (x, y) in iv_mapper]
actual = ''.join([vt.get(c) for c in actual_mapper])
print(actual)
