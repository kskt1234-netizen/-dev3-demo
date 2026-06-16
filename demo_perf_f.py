def find_duplicates(items):
    result = []
    for i in range(len(items)):
        for j in range(len(items)):  # O(N²) — set 변환으로 대체해야 함
            if i != j and items[i] == items[j]:
                result.append(items[i])
