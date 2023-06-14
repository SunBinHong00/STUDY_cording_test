def solution(my_string, overwrite_string, s):
    my_string = [i for i in my_string]
    my_string[int(s):int(s)+len(overwrite_string)] = overwrite_string
    return ''.join(my_string)
solution('He11oWor1d','lloWorl','2')