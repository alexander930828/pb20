def quick_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
    if n <= 1:
        return a
    # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1] # 편의상 리스트의 마지막 값을 기준 값으로 정함
    g1 = []
    g2 = []
    for i in range(0, n-1): # 마지막 값은 기준 값이므로 제외
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6, 8, 3, 9, 10, 1, 2,  4, 7, 5]
print(quick_sort(d))