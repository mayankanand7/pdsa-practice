def LDS(L):
    if len(L) == 0:
        return []
    
    if len(L) == 1:
        return L

    elm_count = len(L)

    mat = [[None] * (elm_count-1)] * (elm_count-1)
    sum = [0] * (elm_count-1)
    for i in range(0, elm_count-1):
        l = [None] * (elm_count-1)
        for j in range(i, elm_count - 1):
            if L[i] > L[j+1]:
                l[j] = 1
                sum[i] += 1
            else:
                l[j] = 0
        mat[i] = l

    # Max length
    results = []
    max = 0
    count = -1
    for i in range(0, len(sum)):
        if sum[i] >= max:
            max = sum[i]
            l = mat[i]
            results.append([])
            count += 1
            results[count].append(L[i])
            for j in range(i, len(l)):
                if l[j] == 1:
                    val = L[j+1]
                    while len(results[count]) > 0:
                        prev = results[count].pop()
                        if prev < val:
                            continue
                        else:
                            results[count].append(prev)
                        if val not in results[count]:
                            results[count].append(val)
                        break
    
    finalResult = []
    for result in results:
        if len(result) > len(finalResult):
            finalResult = result
    
    return finalResult

    

# L = [47, 20, 46, 96, 44, 58, 29, 12, 2, 86]
# L = [0, 2, 7, 3, 7, 3, 8, 2, 1, 0]
L = [11, 16, 32, 60, 50, 58, 8, 59, 45, 48]
print(LDS(L))



# max_elm_idx = -1
#     max = -1
#     lds = []
#     count = -1
#     for i in range(0, len(sum)):
#         if max < sum[i]:
#             lds.append([])
#             count += 1
#             max = sum[i]
#             max_elm_idx = i
#             lds[count].append(L[max_elm_idx])
            
#             l = mat[i]
#             score = 0
#             for j in range(i, len(l)):
#                 if l[j] == 1:
#                     if score < sum[j]:
#                         score = sum[j]
#                         if len(lds[count]) == 1:
#                             lds[count].append(L[j+1])
#                         else:
#                             lds[count].pop()
#                             lds[count].append(L[j+1])
#                     elif score > sum[j]:
#                         if L[j+1] in lds[count]:
#                             pass
#                         else:
#                             lds[count].append(L[j+1])

#     result = []
#     for c in lds:
#         if len(c) > len(result):
#             result = c
#     return result