#!/bin/bash
# filepath: /Users/nicolas/Developer/csuchico.edu/IGVC/simulation/render_video.sh

# Usage: ./render_video.sh <folder_name>
# Example: ./render_video.sh composite

if [ -z "$1" ]; then
  echo "Usage: $0 <folder_name>"
  exit 1
fi

INPUT_FILES="$1"
OUTPUT_FILE="$2"

# Create folders for output files if they don't exist
mkdir -p "$(dirname "$OUTPUT_FILE")"

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
  echo "Error: ffmpeg is not installed. Please install it to proceed."
  exit 1
fi

ffmpeg -y -framerate 1 -pattern_type glob -i "$INPUT_FILES" -c:v libx264 -pix_fmt yuv420p "$OUTPUT_FILE"

echo "Video created: $OUTPUT_FILE"

exit 0
