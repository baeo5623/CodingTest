def solution(my_string, overwrite_string, s):
    answer = my_string[0:s]
    answer = answer+overwrite_string
    answer = answer+my_string[len(answer):len(my_string)]
    return answer