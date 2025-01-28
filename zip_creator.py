import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    # Convert the destination directory to a Path object
    dest_dir = pathlib.Path(dest_dir)

    # Ensure the destination directory exists
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Define the full path for the compressed file
    dest_path = dest_dir / "compressed.zip"

    # Create the ZIP archive
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            # Convert the filepath to a Path object
            filepath = pathlib.Path(filepath)
            # Write the file to the archive
            archive.write(filepath, arcname=filepath.name)


# if __name__ == "__main__":
#     make_archive(filepaths=['android-chrome-192x192.png'], dest_dir='compre')