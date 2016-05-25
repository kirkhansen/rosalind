def overlapping_occurrences(string, sub_string):
    count = start = 0
    while True:
        start = string.find(sub_string, start) + 1
        if start > 0:
            count += 1
        else:
            return count
