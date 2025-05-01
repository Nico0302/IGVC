from huggingface_hub import HfApi
import os

REPO_NAME = "Nico0302/IGVC-Segmentation"

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dataset"))


def upload_dataset():
    api = HfApi(token=os.getenv("HF_TOKEN"))
    api.upload_folder(
        folder_path=base_dir,
        repo_id=REPO_NAME,
        repo_type="dataset",
    )


if __name__ == "__main__":
    print("Uploading dataset to Hugging Face Hub...")
    upload_dataset()
    print("Upload complete.")
