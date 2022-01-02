import random

def basic_func(a):
    return a

def xor(a,b):
    return bool(a) != bool(b)

def compara(a,b):
    if a == b:
        return 0
    elif a < b:
        return 1
    return -1 

def sort_aux(arr, func=basic_func, reversed=False, cmp=compara, key=compara):
    if key != compara:
        cmp = key
    x = random.randint(0,500)
    if x%2 == 0:
        # Merge sort
        Merge_Sort(arr, func, reversed, cmp)
    else:
        # Bingo sort
        arr = Bingo_Sort(arr, func, reversed, cmp)
    return arr

def Merge_Sort(arr, func=basic_func, reversed=False, cmp=compara):
    # O(n logn)
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid] #left
        R = arr[mid:] #right

        Merge_Sort(L,func,reversed,cmp)
        Merge_Sort(R,func,reversed,cmp)

        i = j = k = 0

        # interclasam L si R in arr
        while i < len(L) and j < len(R):
            if xor(reversed, cmp(func(L[i]), func(R[j])) == 1):
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

def Bingo_Sort(arr, func=basic_func, reversed=False, cmp=compara):
    # O(n^2)
    mini = func(arr[0])
    maxi = func(arr[0])
    for el in arr:
        if cmp(func(el),mini) == 1:
            mini = func(el)
        if cmp(func(el),maxi) == -1:
            maxi = func(el)

    Bingo = mini
    NextAvail = 0
    NextBingo = maxi
    
    while cmp(Bingo, maxi) == 1:
        start = NextAvail
        for i in range(start,len(arr)):
            if cmp(func(arr[i]), Bingo) == 0:
                arr[i],arr[NextAvail] = arr[NextAvail],arr[i]
                NextAvail += 1
            elif cmp(func(arr[i]), NextBingo) == 1:
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

class TestClass4:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

def TestFunc2(e):
    return e.x

def TestFunc3(e):
    return e*e

def TestFunc4(a,b): #inlocuitor pt cmp
    if a.x == b.x and a.y == b.y and a.z == b.z:
        return 0
    if a.x < b.x:
        return 1
    elif a.x == b.x and a.y < b.y:
        return 1
    elif a.x == b.x and a.y == b.y and a.z < b.z:
        return 1
    return -1

def TestFunc5(a,b): #inlocuitor pt cmp
    if a*a == b*b:
        return 0
    elif a*a < b*b:
        return 1
    return -1

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
    
    el1 = TestClass4(1,3,4)
    el2 = TestClass4(1,4,7)
    el3 = TestClass4(5,4,4)
    el4 = TestClass4(5,4,2)
    l4 = [el2, el4, el3, el1 ,el4]
    Merge_Sort(l4, cmp=TestFunc4)
    #for el in l4:
        #print(el)
    assert l4 == [el1, el2, el4, el4, el3]

    l5 = [5,5,7,5,3,-2,-9]
    Merge_Sort(l5 ,reversed=True, cmp=TestFunc5)
    assert l5 == [-9,7,5,5,5,3,-2]


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
    l3 = Bingo_Sort(l3, TestFunc3, reversed=True)
    assert l3 == [-9,7,5,5,5,3,-2]

    el1 = TestClass4(1,3,4)
    el2 = TestClass4(1,4,7)
    el3 = TestClass4(5,4,4)
    el4 = TestClass4(5,4,2)
    l4 = [el2, el4, el3, el1 ,el4]
    Bingo_Sort(l4, cmp=TestFunc4)
    #for el in l4:
        #print(el)
    assert l4 == [el1, el2, el4, el4, el3]

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

    l3 = [4,4,7,4,2,-4,-10]
    l3 = sort_aux(l3 ,TestFunc3 ,reversed=True)
    assert l3 == [-10,7,4,4,4,2,-4]

Test_Merge()
Test_Bingo()
Test_Sortare()