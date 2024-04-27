import os
from pytube import YouTube

def download_video(url, output_path, format=''):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        if format == 'mp4':
            stream = yt.streams.get_highest_resolution()
        elif format == 'mp3':
            stream = yt.streams.filter(only_audio=True).first()
        else:
            print("Format yang diminta tidak didukung")
            return

        print(f"Downloading {format.upper()}: {yt.title}")
        stream.download(output_path)
        print(f"Download {format.upper()} completed!")
    except Exception as e:
        print("Error:", str(e))

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"\rDownload progress: {percentage:.2f}% ", end='')

def main_loop():
    while True:
        print("Simple YouTube Downloader")
        url = input("Masukkan URL YouTube: ")
        
        # Membuat direktori Downloads jika belum ada
        output_path = "ytDownloaderVideo"
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        format_option = input("Pilih format (mp3/mp4): ").lower()
        if format_option not in ['mp3', 'mp4']:
            print("Format yang diminta tidak valid")
            continue

        download_video(url, output_path, format_option)

        user_option = input('Apakah kamu ingin mendownload video YouTube lagi? [y/n]')
        if user_option == 'n':
            break

if __name__ == "__main__":
    main_loop()
