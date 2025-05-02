from torch.utils.data import Dataset
from datasets import load_dataset, Dataset as HFDataset
import os
import numpy as np

DEFAULT_PATH = "Nico0302/IGVC-Segmentation"

class Split:
    TRAIN = "train"
    VALID = "valid"
    TEST = "test"

class SegmentationDataset(Dataset):

    def __init__(self, path=DEFAULT_PATH, split=Split.TRAIN, transform=None, mask_name="obstacle_mask", valid_size=0.125):
        self.path = path
        self.split = split
        self.transform = transform
        self.mask_name = mask_name
        self.valid_size = valid_size

        self.data = self._read_split()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        sample = dict(image=np.array(item["image"]), mask=np.array(item[self.mask_name]))
        if self.transform is not None:
            sample = self.transform(**sample)

        return {
            "image": np.transpose(sample["image"], (2, 0, 1)), # HWC to CHW (3, H, W)
            "mask": np.expand_dims(sample["mask"].astype(np.float32) / 255.0, 0), # HW to CHW (1, H, W)
        }

    def _read_split(self):
        dataset = load_dataset(self.path, split="test" if self.split == Split.TEST else "train")
        assert isinstance(dataset, HFDataset), "Dataset must be a Hugging Face Dataset"

        if (self.split == Split.TEST):
            return dataset
        
        splits = dataset.train_test_split(test_size=self.valid_size, seed=42)
        if self.split == Split.VALID:
            return splits["test"]
        return splits["train"]