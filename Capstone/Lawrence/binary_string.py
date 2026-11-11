def binary_strings(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    result = []
    current = []

    def build():
        if len(current) == n:
            result.append("".join(current))
            return

        for bit in ("0", "1"):
            current.append(bit)  # choose
            build()              # explore
            current.pop()        # unchoose

    build()
    return result



def binary_no_adjacent_ones(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    result = []
    path = []

    def backtrack():
        if len(path) == n:
            result.append("".join(path))
            return

        path.append("0")
        backtrack()
        path.pop()

        if not path or path[-1] != "1":
            path.append("1")
            backtrack()
            path.pop()

    backtrack()
    return result

print(binary_strings(0))  # [""]
print(binary_strings(1))  # ["0", "1"]
print(binary_strings(2))  # ["00", "01", "10", "11"]
print(len(binary_strings(4)))  # 16




def binary_string(n):
    result = []
    def backtrack(path):
        if len(path) == n:
            result.append("".join(path))
            return

        for bit in ("0", "1"):
            path.append(bit)
            backtrack(path)
            path.pop()

    backtrack([])
    return result

print(binary_string(2))
print(binary_string(4))
print(len(binary_string(4)))


def binary_no_adjacent(n):
    result = []

    def backtrack(curr):
        if len(curr) == n:
            result.append("".join(curr))
            return

        curr.append("0")
        backtrack(curr)
        curr.pop()

        if not curr or curr[-1] != "1":
            curr.append("1")
            backtrack(curr)
            curr.pop()

    backtrack([])
    return result

print(binary_no_adjacent(4))
