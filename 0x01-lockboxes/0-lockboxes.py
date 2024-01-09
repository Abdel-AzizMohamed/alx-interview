"""Define module to check boxes keys"""


def canUnlockAll(boxes: list) -> bool:
    """
    Check if the all boxes have keys

    Arguments:
        boxes: list contains boxes with its keys

    Returns:
        true if all boxes have keys else false
    """
    keys = {0}
    current_keys = [key for key in boxes[0]]
    seen_boxes = {0}

    while current_keys:
        current_key = current_keys.pop(0)
        if current_key in seen_boxes:
            continue

        current_keys += [key for key in boxes[current_key]]
        keys.add(current_key)
        seen_boxes.add(current_key)

    return len(keys) == len(boxes)
