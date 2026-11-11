def binary_strings(n):
    result=[]
    
    def generate(current,moves):
        if len(current)==n:
            result.append("".join(current.copy()))
            return
        for char in moves:
            current.append(char)
            generate(current,moves)
            current.pop()
            
    generate([],"01")
    print(result) 
    return result
binary_strings(3)