from pathlib import Path
from urllib.request import urlretrieve

# Where the dataset will be stored
DATA_DIR = Path("data/fashion_mnist")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Official Fashion-MNIST dataset location
BASE_URL = (
    "http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/"
)

FILES = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",
]

for filename in FILES:
    destination = DATA_DIR / filename

    if destination.exists():
        print(f"Already downloaded: {filename}")
        continue

    url = BASE_URL + filename

    print(f"Downloading: {filename}")

    try:
        urlretrieve(url, destination)
        print(f"Saved to: {destination}")

    except Exception as error:
        print(f"Download failed: {filename}")
        print(f"Reason: {error}")
        raise

print("\nAll four dataset files are ready!")