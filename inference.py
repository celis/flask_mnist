from commons import transform_image
import torch


def get_prediction(model, image_bytes):
    try:
        tensor = transform_image(image_bytes=image_bytes)
        pred = model.forward(tensor)
    except Exception:
        return 0, 'error'
    return str(torch.argmax(pred.unsqueeze(0), dim=1).item())