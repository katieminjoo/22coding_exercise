def solution(N):
    str_n = str(N)
    c = '5'
    idx_list = [pos for pos, char in enumerate(str_n) if char == c]

    answer = -9999999
    for idx in idx_list:
        done_num = int(str_n[0:idx]+str_n[idx+1:])
        if done_num > answer:
            answer = done_num

    return(answer)