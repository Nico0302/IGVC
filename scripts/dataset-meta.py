import os
import csv
import re

# --- Configuration ---
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dataset"))
image_dir = os.path.join(base_dir, "composite")
obstacle_mask_dir = os.path.join(base_dir, "obstacle")
lane_mask_dir = os.path.join(base_dir, "lane")
output_csv = os.path.join(base_dir, "metadata.csv")
image_extensions = (".png", ".jpg", ".jpeg")  # Add other extensions if needed
# --- End Configuration ---

# Regex to parse image filenames like "X-Y.ext"
# It captures X, Y, and the extension separately.
image_pattern = re.compile(r"^([^-]+)-(.+?)(\.[^.]+)$")


def find_and_validate_mask(
    mask_base_dir, mask_subdir_name, expected_mask_filename, image_filename
):
    """
    Checks if a mask file exists and returns its relative path if found.

    Args:
        mask_base_dir (str): The absolute base directory for this type of mask.
        mask_subdir_name (str): The name of the subdirectory (e.g., 'obstacle', 'lane').
        expected_mask_filename (str): The filename expected for the mask.
        image_filename (str): The original image filename (for logging).

    Returns:
        str or None: The relative path to the mask using forward slashes if found,
                     otherwise None. Prints a warning if the mask is not found.
    """
    if not os.path.isdir(mask_base_dir):
        print(
            f"Warning: {mask_subdir_name.capitalize()} mask directory not found: {mask_base_dir}"
        )
        return None  # Indicate directory missing, prevents further file checks

    mask_path_abs = os.path.join(mask_base_dir, expected_mask_filename)
    if os.path.isfile(mask_path_abs):
        mask_path_rel = os.path.join(mask_subdir_name, expected_mask_filename)
        return mask_path_rel.replace(os.sep, "/")
    else:
        print(
            f"  - Missing {mask_subdir_name} mask for image '{image_filename}': Expected '{expected_mask_filename}' in {mask_base_dir}"
        )
        return None


def generate_meta():
    metadata = []

    print(f"Scanning image directory: {image_dir}")

    # Check if image directory exists
    if not os.path.isdir(image_dir):
        print(f"Error: Image directory not found: {image_dir}")
        exit(1)

    # Pre-check mask directories once (optional, find_and_validate_mask handles it too)
    if not os.path.isdir(obstacle_mask_dir):
        print(f"Warning: Obstacle mask directory not found: {obstacle_mask_dir}")
    if not os.path.isdir(lane_mask_dir):
        print(f"Warning: Lane mask directory not found: {lane_mask_dir}")

    # Iterate through files in the image directory
    for filename in os.listdir(image_dir):
        # Check if it's a file and has a valid image extension first
        file_path_abs = os.path.join(image_dir, filename)
        if os.path.isfile(file_path_abs) and filename.lower().endswith(
            image_extensions
        ):
            # Now try to match the expected pattern
            match = image_pattern.match(filename)
            if match:
                x_part, y_part, ext = match.groups()

                # Construct the expected mask filename (Y part + original extension)
                mask_filename = f"{y_part}{ext}"
                image_path_rel = os.path.join("composite", filename).replace(
                    os.sep, "/"
                )

                # Find and validate masks
                obstacle_mask_path_rel = find_and_validate_mask(
                    obstacle_mask_dir, "obstacle", mask_filename, filename
                )
                lane_mask_path_rel = find_and_validate_mask(
                    lane_mask_dir, "lane", mask_filename, filename
                )

                metadata.append(
                    {
                        "file_name": image_path_rel,
                        "obstacle_mask_file_name": obstacle_mask_path_rel,
                        "lane_mask_file_name": lane_mask_path_rel,
                    }
                )
            else:
                print(
                    f"  - Skipping image file (does not match pattern 'X-Y.ext'): {filename}"
                )
        # Optional: Add an else here if you want to log non-image files found
        # else:
        #     if os.path.isfile(file_path_abs): # Only log if it's actually a file
        #          print(f"  - Skipping non-image file: {filename}")

    # Write the metadata to a CSV file
    if metadata:
        print(f"\nFound {len(metadata)} matching image-mask sets.")
        print(f"Writing metadata to: {output_csv}")
        try:
            with open(output_csv, "w", newline="") as csvfile:
                fieldnames = [
                    "file_name",
                    "obstacle_mask_file_name",
                    "lane_mask_file_name",
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(metadata)
            print("Successfully generated metadata.csv")
        except IOError as e:
            print(f"Error writing CSV file: {e}")
    else:
        print("\nNo matching image-mask sets found. No metadata.csv generated.")


if __name__ == "__main__":
    generate_meta()
