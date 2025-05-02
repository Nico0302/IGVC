ifneq (,$(wildcard ./.env))
	include .env
	export
endif

video-composite:
	./scripts/video.sh "./dataset/composite/1-*.png" ./video/composite.mp4

video-seg:
	./scripts/video.sh "./dataset/seg/*.png" ./video/seg.mp4

clean-video:
	rm -f ./video/composite/*.mp4
	rm -f ./video/seg/*.mp4

video: video-composite video-seg

clean-render:
	rm -f ./dataset/composite/*-1*.png
	rm -f ./dataset/obstacle/1*.png
	rm -f ./dataset/seg/1*.png
	rm -f ./dataset/lane/1*.png

dataset-upload:
	uv run ./scripts/dataset-upload.py

dataset-meta:
	uv run ./scripts/dataset-meta.py train
	uv run ./scripts/dataset-meta.py test