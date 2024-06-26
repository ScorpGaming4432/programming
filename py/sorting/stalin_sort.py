def stalin(l):
    max_val = l[0]
    return [max_val := x for x in l if x >= max_val]