import random

def basic_func(a):
    return a

def compara(a,b,reversed):
    if reversed:
        return a > b
    return a < b 

def sort_aux(arr, func=basic_func, reversed=False):
    x = random.randint(0,500)
    if x%2 == 0:
        # Merge sort
        Merge_Sort(arr, func, reversed)
    else:
        # Bingo sort
        arr = Bingo_Sort(arr, func, reversed)
    return arr

def Merge_Sort(arr, func=basic_func, reversed=False):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        Merge_Sort(L,func,reversed)
        Merge_Sort(R,func,reversed)

        i = j = k = 0

        # interclasam L si R in arr
        while i < len(L) and j < len(R):
            if compara(func(L[i]), func(R[j]), reversed):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def Bingo_Sort(arr, func=basic_func, reversed=False):
    mini = min(list(map(func, arr)))
    maxi = max(list(map(func, arr)))
    Bingo = mini
    NextAvail = 0
    NextBingo = maxi
    while Bingo < maxi:
        start = NextAvail
        for i in range(start,len(arr)):
            if func(arr[i]) == Bingo:
                arr[i],arr[NextAvail] = arr[NextAvail],arr[i]
                NextAvail += 1
            elif func(arr[i]) < NextBingo:
                NextBingo = func(arr[i])
        Bingo = NextBingo
        NextBingo = maxi

    if reversed:
        return arr[::-1]
    return arr
    


class TestClass2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def TestFunc2(e):
    return e.x

def TestFunc3(e):
    return e*e

def Test_Merge():
    l1 = [1,7,9,3,2]
    Merge_Sort(l1)
    assert l1 == [1,2,3,7,9]

    el1 = TestClass2(1,3)
    el2 = TestClass2(7,7)
    el3 = TestClass2(5,4)
    l2 = [el1,el2,el3]
    Merge_Sort(l2, func=TestFunc2, reversed=True)
    assert l2 == [el2,el3,el1]

    l3 = [5,5,7,5,3,-2,-9]
    Merge_Sort(l3 ,TestFunc3 ,reversed=True)
    assert l3 == [-9,7,5,5,5,3,-2]

def Test_Bingo():
    l1 = [1,7,9,3,2]
    l1 = Bingo_Sort(l1)
    assert l1 == [1,2,3,7,9]

    el1 = TestClass2(1,3)
    el2 = TestClass2(7,7)
    el3 = TestClass2(5,4)
    l2 = [el1,el2,el3]
    l2 = Bingo_Sort(l2, func=TestFunc2, reversed=True)
    assert l2 == [el2,el3,el1]

    l3 = [5,5,7,5,3,-2,-9]
    l3 = Bingo_Sort(l3 ,TestFunc3 ,reversed=True)
    assert l3 == [-9,7,5,5,5,3,-2]

def Test_Sortare():
    l1 = [1,7,9,3,2]
    l1 = sort_aux(l1)
    assert l1 == [1,2,3,7,9]

    el1 = TestClass2(1,3)
    el2 = TestClass2(7,7)
    el3 = TestClass2(5,4)
    l2 = [el1,el2,el3]
    l2 = sort_aux(l2, func=TestFunc2, reversed=True)
    assert l2 == [el2,el3,el1]

    l3 = [5,5,7,5,3,-2,-9]
    l3 = sort_aux(l3 ,TestFunc3 ,reversed=True)
    assert l3 == [-9,7,5,5,5,3,-2]

Test_Sortare()
Test_Bingo()
Test_Merge()