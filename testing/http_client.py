import requests
from tqdm import tqdm
import time

def download_with_speed(url, filename, speed_limit_kb=0, chunk_size=1024):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
        ascii=True
    ) as bar:
        start_time = time.time()
        downloaded = 0
        for chunk in response.iter_content(chunk_size=chunk_size):
            elapsed_time = time.time() - start_time
            if speed_limit_kb and elapsed_time < downloaded / speed_limit_kb:
                time.sleep((downloaded / speed_limit_kb) - elapsed_time)

            file.write(chunk)
            downloaded += len(chunk)
            bar.update(len(chunk))

    print(f"\nDownloaded {filename} successfully!")


if __name__ == '__main__':
    url = 'https://speed.hetzner.de/100MB.bin'
    filename = 'downloaded_file.txt'
    speed_limit_kb = 1000000  # Adjust download speed limit in KB/s

    download_with_speed(url, filename, speed_limit_kb)
