import cv2
import os


def create_timelapse(image_folder, video_name):
    """
    Create time lapse from images
    :param image_folder: images folder
    :param video_name: video name
    """
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    video = cv2.VideoWriter(video_name, fourcc, 6, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()


if __name__ == "__main__":
    create_timelapse('./eifeltower', 'video.avi')
