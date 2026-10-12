def merge(arr:list):
    if len(arr) <= 1: return arr

    # nienawidzę rekursji 2h nad tym siedzialem
    lewa, prawa = merge(arr[:len(arr) // 2]), merge(arr[len(arr) // 2:])

    #cały algorytm
    i, j, output = 0, 0, []

    # kiedy żadna lista nie wyczerpana
    while i < len(lewa) and j < len(prawa):

        #zapisz to co mniejsze i zwiększ odpowiedni index
        if lewa[i] < prawa[j]:
            output.append(lewa[i])
            i += 1
        else:
            output.append(prawa[j])
            j += 1

    #to co zostało już jest posortowane
    return output + lewa[i:] + prawa[j:]