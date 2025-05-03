---
library_name: segmentation-models-pytorch
license: mit
pipeline_tag: image-segmentation
tags:
- model_hub_mixin
- pytorch_model_hub_mixin
- segmentation-models-pytorch
- semantic-segmentation
- pytorch
languages:
- python
---
# FPN Model Card

Table of Contents:
- [Load trained model](#load-trained-model)
- [Model init parameters](#model-init-parameters)
- [Model metrics](#model-metrics)
- [Dataset](#dataset)

## Load trained model
```python
import segmentation_models_pytorch as smp

model = smp.from_pretrained("<save-directory-or-this-repo>")
```

## Model init parameters
```python
model_init_params = {
    "encoder_name": "resnet34",
    "encoder_depth": 5,
    "encoder_weights": "imagenet",
    "decoder_pyramid_channels": 256,
    "decoder_segmentation_channels": 128,
    "decoder_merge_policy": "add",
    "decoder_dropout": 0.2,
    "decoder_interpolation": "nearest",
    "in_channels": 3,
    "classes": 1,
    "activation": None,
    "upsampling": 4,
    "aux_params": None
}
```

## Model metrics
[More Information Needed]

## Dataset
Dataset name: Nico0302/IGVC-Segmentation

## More Information
- Library: https://github.com/qubvel/segmentation_models.pytorch
- Docs: https://smp.readthedocs.io/en/latest/

This model has been pushed to the Hub using the [PytorchModelHubMixin](https://huggingface.co/docs/huggingface_hub/package_reference/mixins#huggingface_hub.PyTorchModelHubMixin)