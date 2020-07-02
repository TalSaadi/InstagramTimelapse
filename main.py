from tag_scrapper import scrape_tag
from timelapse import create_timelapse
import sys, shutil


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ig-timelapse.py <hashtag>")
        exit(1)

    tag = sys.argv[1]
    print("Downloading images from instagram...")
    scrape_tag(tag, ('./%s' % tag), num_images=500)
    print("Creating your time lapse...")
    create_timelapse(tag, tag + '.avi')
    shutil.rmtree('./%s' % tag)
    print("Your time lapse is ready at: %s.avi!" % tag)
