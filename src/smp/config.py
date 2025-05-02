import torch
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "dataset")
DATASET_NAME = "Nico0302/IGVC-Segmentation"

MODEL_NAME = "Nico0302/IGVC-Segmentation"

BATCH_SIZE = 64
NUM_EPOCHS = 10
VALID_SIZE = 0.125

INPUT_IMAGE_WIDTH = 256
INPUT_IMAGE_HEIGHT = 256

NUM_CLASSES = 1

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
NUM_WORKERS = min(8, os.cpu_count() or 1) 