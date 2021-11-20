def iou_torchvison(bb1, bb2):
    """:ivar
    bbox format be prepared as [x1,y1,x2,y2]
    """
    import torch
    import torchvision.ops.boxes as bops
    box1 = torch.tensor(bb1, dtype=torch.float)
    box2 = torch.tensor(bb2, dtype=torch.float)
    iou = bops.box_iou(box1, box2)
    return iou


def iou_polygon(bb1, bb2):
    """:param
    bb1 or bb2 format as [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
    """
    from shapely.geometry import Polygon
    bbox_1 = Polygon(bb1)
    bbox_2 = Polygon(bb2)
    iou = bbox_1.intersection(bbox_2).area/bbox_1.union(bbox_2).area
    return iou
