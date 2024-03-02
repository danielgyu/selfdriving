def calculate_iou(gt_box, pred_box):
    """
    gt_box: ground truth bounding box
    pred_box: prediction bounding box

    box format [x1, y1, x2, y2]
    """

    # get the intersection bounding box
    # y axis descends, so it goes from top -> bottom
    x_left = max(gt_box[0], pred_box[0])
    x_right = min(gt_box[2], pred_box[2])
    y_top = max(gt_box[1], pred_box[1])
    y_bottom = min(gt_box[3], pred_box[3])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    intersection_area = (x_right-x_left) * (y_bottom-y_top)
    
    gt_box_area = (gt_box[2]-gt_box[0]) * (gt_box[3]-gt_box[1])
    pred_box_area = (pred_box[2]-pred_box[0]) * (pred_box[3]-pred_box[1])
    return (
        intersection_area / gt_box_area+pred_box_area-intersection_area
    )
