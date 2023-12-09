def principal(list_eleman):
    list_eleman.sort()

    rezilta = [list_eleman[0]]

    for enteval in list_eleman[1:]:
        eleman1, denye_eleman = enteval
        dernye_rezilta = rezilta[-1]

        if eleman1 <= dernye_rezilta[1]:
            # Si gen overlap
            rezilta[-1] = [min(dernye_rezilta[0], eleman1), max(dernye_rezilta[1], denye_eleman)]
        else:
            # Si pa gen overlap
            rezilta.append(enteval)

    return rezilta

lis_enteval = [[1, 4], [3, 6]]
result = principal(lis_enteval)
print(result)
