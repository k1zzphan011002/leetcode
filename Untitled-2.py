def pack_boxes(items):
    items.sort(reverse=True)  
    boxes = []  
    for item in items:
        found_box = False
        for box in boxes:
            if sum(box) + item <= 9:
                box.append(item)
                found_box = True
                break
        if not found_box:
            boxes.append([item])
    return boxes