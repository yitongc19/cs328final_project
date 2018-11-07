def sys_sampling(s, i, n, k):
    """Modified systematic sampling that selects k numbers from the
    range [0, n - 1], using s as the starting number and i as the
    interval.
    """
    res_set = set()
    while len(res_set) <= k:
        cur_len = len(res_set)
        res_set.add(s)
        # if getting to a number added before, 
        # increment s by 1 to avoid keep generating the
        # same numbers
        if len(res_set) == cur_len:
            s += 1
        else:
            s = (s + i) % n
    return res_set