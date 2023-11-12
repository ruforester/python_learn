import os

def main(folder, ext):
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{folder}/{count+1}.{ext}"
        src = f"{folder}/{filename}"
        os.rename(src, dst)

if __name__ == '__main__':
    main(folder="portfolio/images", ext='png')