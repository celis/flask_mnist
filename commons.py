import io
from mnist.model import LogisticRegression
import boto3
import numpy as np
import os
import torch
from mnist.configuration import Configuration
from PIL import Image
import torchvision.transforms as transforms


def download_model_artifacts(config: Configuration):
    """
    Downloads model artifact from S3
    """
    model_name, model_path = config.model_artifact.split("/")[-1], config.model_artifact

    boto3_client = boto3.client(
        "s3",
        region_name=config.s3["region_name"],
        aws_access_key_id=config.s3["access_key"],
        aws_secret_access_key=config.s3["secret_key"],
    )
    boto3_client.download_file(config.s3["bucket"], model_name, model_path)


def load_model(config: Configuration):

    if not os.path.exists(config.model_artifact):
        download_model_artifacts(config)

    model = LogisticRegression()
    model.load_state_dict(torch.load(config.model_artifact))
    model.eval()
    return model


def transform_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("L")
    image = np.asarray(transforms.Resize(28)(image))
    image = image.reshape(784) / 255
    return torch.Tensor(image)
