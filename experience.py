def vibor(a):
    result1 = []
    if isinstance(a, int):
        result1.append(a)
    elif isinstance(a, str):
        dstr_ = int(len(a))
        result1.append(dstr_)
    elif isinstance(a, set):
        a2 = list(a)
        a3 = list(a2[0])
        for n in a3:
            if isinstance(n, int):
                result1.append(n)
            elif isinstance(n, str):
                dstr_ = int(len(n))
                result1.append(dstr_)
            elif isinstance(n, tuple):
                for t in n:
                    dlina = sum(vibor(t))
                    result1.append(dlina)



    return result1

