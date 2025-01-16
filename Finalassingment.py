   #Program : Credit Card Assignment
   #Description : a program to sort a list of credit card expiry dates and alert the user if a credit card needs to be renewed or is expired completely
   #VARIABLE DICTIONARY :
     #names (list) = List of the names of the credit card holders
     #cctypes (list) = List of the credit card types
     #ccnums (list) = List of the credit card numbers
     #exp_dates (list) = list of the expirey dates
     #checked_expired_dates (list) = list of the checked expired dates from the list
     #renew_imm_dates (list) = renew immediately dates of the credit cards
     #sorted_exp (list) = the sorted expirey dates of the credit cards
     #i (int) = i is the index in the merge sort
     #l (int) = l is the left index in the merge sort
     # (int) = m is the middle value index in the merge sort
     #r (int) = r is the right index in the merge sort
     #expired_indice (list) = the positions of the expiry dates in relation to the unsorted dates
     #about_indice (list) = the positions of the renew immediately dates in relation to the unsorted dates

names = []
cctypes = []
ccnums = []
exp_dates = []
checked_expired_dates = []
renew_imm_dates = []
sorted_exp = []

def readfile():
    try:
        fh = open("data.dat", 'r')
        eof = False
        fh.readline()
        while not eof:
            line = fh.readline()
            eof = (line == "")
            if not eof:
                line = line.strip()
                fname, lname, cctype, ccnum, exp_mo, exp_yr = line.split(",")
                name = fname + " " + lname
                names.append(name)
                cctypes.append(cctype)
                ccnums.append(ccnum)

                exp_date = int((int(exp_yr) * 100) + int(exp_mo))
                exp_dates.append(exp_date)
                sorted_exp.append(exp_date)

        fh.close()


    except OSError as err:
        print("OSError: ", err)
    except EOFError as err:
        print("EOFError: ", err)
        fh.close()
    except ValueError as err:
        print("ValueError: ", err)




def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)



readfile()
mergeSort(sorted_exp, 0, len(sorted_exp) - 1)


for i in range(len(sorted_exp)):
    if sorted_exp[i] < 202404:
        checked_expired_dates.append(sorted_exp[i])


for i in range(len(sorted_exp)):
    if sorted_exp[i] == 202407 or sorted_exp[i] == 202406:
        renew_imm_dates.append(sorted_exp[i])


about_indice = []
for i in renew_imm_dates:
    for j in range(len(exp_dates)):
        if i == exp_dates[j] and j not in about_indice:
            about_indice.append(j)


expired_indice = []
for i in checked_expired_dates:
    for j in range(len(exp_dates)):
        if i == exp_dates[j] and j not in expired_indice:
            expired_indice.append(j)

