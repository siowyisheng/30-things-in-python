from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {
    'keywords': 'beautiful snakes',
    'limit': 10,
    # 'color': 'gray',
}
paths = response.download(arguments)
print(paths)
