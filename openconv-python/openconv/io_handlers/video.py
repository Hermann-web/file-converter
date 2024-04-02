from pathlib import Path
from typing import List, Union

import numpy as np
from convcore.io_handler import FileReader, FileWriter

from openconv.utils.image_to_video import save_video_from_array_images


class VideoArrayWriter(FileWriter):
    """
    Writes a video to a file using a list of image arrays.
    """

    def _check_output_format(self, content) -> bool:
        """
        Validates if the provided content is suitable for writing as a video.

        Args:
            content: Content to be validated.

        Returns:
            bool: True if the content is suitable for writing as a video, False otherwise.
        """
        # Check if content is a numpy array with 4 dimensions
        is_array = isinstance(content, np.ndarray) and content.ndim == 4
        is_list = (
            isinstance(content, list)
            and isinstance(content[0], np.ndarray)
            and content[0].ndim == 3
        )
        return is_array or is_list

    def _write_content(
        self, output_path: Path, output_content: Union[np.ndarray, list], fps: int = 15
    ) -> bool:
        """
        Writes a video to a file using a list of image arrays.

        Args:
            output_path (Path): Path to save the video.
            output_content (Union[np.ndarray, list]): Video frames as a numpy array or a list of numpy arrays.
            fps (int, optional): Frames per second. Defaults to 15.

        Returns:
            bool: True if the video is successfully written, False otherwise.
        """
        if not len(output_content):
            print("No valid images found.")
            return False

        img_array = output_content

        save_path = Path(output_path)

        img_array = np.asarray(img_array)

        assert (
            img_array.ndim == 4
        ), f"img_array.ndim={img_array.ndim} instead of 4"  # Ensure img_array is 4-dimensional (frames, height, width, channels)

        # Get the number of frames
        nb_frames = img_array.shape[0]
        print(f"Proceeding to write {nb_frames} frames to video...")

        # Get the size of one frame
        img_size = (img_array.shape[2], img_array.shape[1])  # (width, height)

        return save_video_from_array_images(
            img_array=img_array,
            size=img_size,
            save_path=save_path,
            fps=fps,
            label="img",
        )
