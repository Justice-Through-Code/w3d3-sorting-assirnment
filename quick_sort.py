def quick_sort(data, key=lambda x: x):
    if len(data) <= 1:
        return data
    pivot = data[0]
    lesser = [x for x in data[1:] if key(x) <= key(pivot)]
    greater = [x for x in data[1:] if key(x) > key(pivot)]
    return quick_sort(lesser, key) + [pivot] + quick_sort(greater, key)
