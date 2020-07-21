def solution(A):
    # write your code in Python 3.6
    events = []
    for i, v in enumerate(A):
        events.append(((i-v), "lower"))
        events.append(((i+v), "upper"))

    events.sort()

    intersections = 0
    intervals = 0

    for event in events:
        if event[1] == "upper":
            intervals -= 1
        elif event[1] == "lower":
            intersections += intervals
            intervals += 1

    return -1 if intersections > 10000000 else intersections
