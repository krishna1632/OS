import os


def copy_file(source, destination):
    with open(source, "rb") as src:
        with open(destination, "wb") as dest:
            while True:
                chunk = os.read(src.fileno(), 1024)
                if not chunk:
                    break
                os.write(dest.fileno(), chunk)


copy_file("example.html", "destination.txt")
