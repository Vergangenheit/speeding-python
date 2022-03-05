import json
import threading
import time
from urllib.request import Request, urlopen


def write_genre(file_name: str):
    """
        Uses genrenator from binaryjazz.us to write a random genre to the
        name of the given file
        """
    req = Request("https://binaryjazz.us/wp-json/genrenator/v1/genre/", headers={"User-Agent": "Mozilla/5.0"})
    genre: str = json.load(urlopen(req))

    with open(file_name, "w") as f:
        print(f"Writing '{genre}' to '{file_name}'...")
        f.write(genre)


if __name__ == "__main__":
    print("Starting...")
    start = time.time()

    threads = []

    for i in range(5):
        thread = threading.Thread(target=write_genre,
                                  args=[f"./threading/new_file{i}.txt"])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end = time.time()
    print(f"Time to complete synchronous read/writes: {round(end - start, 2)} seconds")
