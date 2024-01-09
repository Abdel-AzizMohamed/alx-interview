#!/usr/bin/python3
"""Define module to check boxes keys"""
# def canUnlockAll(boxes: list) -> bool:
#     """
#     Check if the all boxes have keys

#     Arguments:
#         boxes: list contains boxes with its keys

#     Returns:
#         true if all boxes have keys else false
#     """
#     current_keys = [key for key in boxes[0]]
#     seen_boxes = {0}

#     while current_keys:
#         current_key = current_keys.pop(0)
#         if current_key in seen_boxes:
#             continue

#         current_keys += [key for key in boxes[current_key]]
#         seen_boxes.add(current_key)

#     print(seen_boxes)

#     return len(seen_boxes) == len(boxes)


def canUnlockAll(boxes):
    """determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
