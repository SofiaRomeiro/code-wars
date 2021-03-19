def comparador(s):
    val : int = 0
    st_l : list = []

    for c in s:
        if ord(c) != ord(' '):
            st_l += [c]  
 
    if len(st_l) % 2 == 0:
        while st_l != []:
            if st_l[0] != st_l[-1]:
                return 0
            st_l = st_l[1:-1]

    else:        
        while len(st_l) > 1:
            if st_l[0] != st_l[-1]:
                return 0
            st_l = st_l[1:-1]
    return 1   

s = input()
print(comparador(s))



