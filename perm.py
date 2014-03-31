def perm(lst):
    if len(lst) <= 1:
        return [lst]
    out = []
    for i in range(len(lst)):
        lstcopy = lst[:]
        del lstcopy[i]
        for j in perm(lstcopy):
            out.append(lst[i:i+1] + j)
    return out
