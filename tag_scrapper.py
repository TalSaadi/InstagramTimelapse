from instagram_scraper import InstagramScraper


def scrape_tag(tag, directory, num_images=50):
    """
    Scrape instagram and download hash tag photos
    :param tag: instagram hash tag
    :param directory: destination directory
    :param num_images: number of images
    """

    args = {
            'usernames': [tag],
            'destination': directory,
            'login_user': None,
            'login_pass': None,
            'quiet': True,
            'maximum': num_images,
            'retain_username': False,
            'media_metadata': False,
            'media_types': ['image'],
            'latest': False
        }

    scraper = InstagramScraper(**args)
    scraper.authenticate_as_guest()
    scraper.scrape_hashtag()
    scraper.save_cookies()


if __name__ == "__main__":
    scrape_tag('eifeltower', ("./%s" % 'eifeltower'))
