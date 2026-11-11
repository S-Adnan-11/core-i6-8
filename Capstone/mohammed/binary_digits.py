def binary_strings(n):
    result = []

    def generate_fn(current_list, chars):
        if len(current_list) == n:
            result.append("".join(current_list))
            return 
        for char in chars:
            current_list.append(char)
            generate_fn(current_list, chars)
            current_list.pop()

    generate_fn([], "01")
    return result 


print(binary_strings(4))