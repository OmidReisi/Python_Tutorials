# for Images we should be use binary mode
with open(r"./Test/image.JPG", "rb") as read_image:
    with open(r"./Test/image_copy.JPG", "wb") as write_image:

        # for line in read_image:
        #     write_image.write(line)

        # binary mode raeds in bytes
        chunk_size = 4096
        chunk = read_image.read(4096)
        while len(chunk) > 0:
            write_image.write(chunk)
            chunk = read_image.read(chunk_size)
