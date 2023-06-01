from pytube import YouTube

def download():
    link = input("url: ")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    print("downloading")
    ys.download()
    print("download complete")
    download()
 
download()