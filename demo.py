#!/usr/bin/env python
from operator import itemgetter

examples = [
    (3, 5),  # reservation A
    (2, 9),  # reservation B
    (0, 4),  # reservation C
    (0, 2),  # reservation D
    (8, 8),  # reservation E
    (3, 7),  # reservation F
    (6, 9),  # reservation G
    (5, 6),  # reservation H
    (7, 9),  # reservation I
    (1, 2)  # reservation J
]


def calculate_rooms(reservation_list):
    meeting_times = list()
    # add "tag" for each of meeting time
    for start, end in reservation_list:
        meeting_times.append((start, 'start'))
        meeting_times.append((end, 'end'))
    # sort all times from earliest to latest
    meeting_times = sorted(meeting_times, key=itemgetter(0))

    # loop each time, find max concurrent running meetings --> Min meeting room requirement
    minimum, current = 0, 0
    for time, type in meeting_times:
        if type == 'start':
            current += 1
            minimum = max(minimum, current)
        elif type == 'end':
            current -= 1
        else:
            print "Invalid meeting time type, Neither start nor end"
            exit(1)

    return minimum


if __name__ == '__main__':
    rooms = calculate_rooms(examples)
    print "We need %s meeting rooms for arranging those meetings." % rooms
