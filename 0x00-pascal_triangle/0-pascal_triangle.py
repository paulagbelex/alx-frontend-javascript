def pascal_triangle(n):
    if n <= 0:
        return []

    result = []

    for i in range(n):
        row = []
        if i == 0:
            row.append(1)
        else:
            prev_row = result[i - 1]
            row.append(1)
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        result.append(row)

    return result