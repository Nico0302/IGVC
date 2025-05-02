import albumentations as A

# training set images augmentation
def get_train_transform(width: int, height: int):
    train_transform = [
        A.HorizontalFlip(p=0.5),
        A.PadIfNeeded(min_height=width, min_width=height),
        A.RandomResizedCrop(size=(width, width), scale=(0.8, 1.0), p=1),
        A.OneOf(
            [
                A.CLAHE(p=1),
                A.RandomBrightnessContrast(p=1),
                A.RandomGamma(p=1),
            ],
            p=0.4,
        ),
        A.OneOf(
            [
                A.Sharpen(p=1),
                A.Blur(blur_limit=3, p=1),
                A.MotionBlur(blur_limit=3, p=1),
            ],
            p=0.2,
        ),
        A.OneOf(
            [
                A.RandomBrightnessContrast(p=1),
                A.HueSaturationValue(p=1),
            ],
            p=0.4,
        ),
    ]
    return A.Compose(train_transform)


def get_valid_transform(width: int, height: int):
    """Add paddings to make image shape divisible by 32"""
    test_transform = [
        A.PadIfNeeded(min_height=height, min_width=width),
        A.CenterCrop(height=height, width=width),
    ]
    return A.Compose(test_transform)