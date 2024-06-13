from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

def downloader():
    url = url_entry.get()
    if not url:
        messagebox.showinfo("Error", "Please enter the link")
        return
    try:
        video = YouTube(url)
        
        resolution = res.get()
        if resolution == '360p':
            video_stream = video.streams.filter(res='360p').first()
        elif resolution == '720p':
            video_stream = video.streams.filter(res='720p').first()
        elif resolution == '1080p':
            video_stream = video.streams.filter(res='1080p').first()
        else:
            messagebox.showinfo("Error", "Please select the resolution")
            return
        
        video_stream.download()
        messagebox.showinfo("Success", "Video downloaded successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.geometry("700x350")
window.title("YouTube Video Downloader")

# Title label
tk.Label(window, text="YOUTUBE VIDEO DOWNLOADER", bg='grey', font=('Calibri', 15)).pack(pady=10)

# URL entry label and field
tk.Label(window, text="Enter the link to download", font=('Calibri', 12)).pack(pady=5)
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

# Resolution radio buttons
res = tk.StringVar()
res.set(None)

tk.Radiobutton(window, text='360p', variable=res, value='360p').pack()
tk.Radiobutton(window, text='720p', variable=res, value='720p').pack()
tk.Radiobutton(window, text='1080p', variable=res, value='1080p').pack()

# Download button
tk.Button(window, text="Download", bg='green', command=downloader).pack(pady=20)

# Start the GUI event loop
window.mainloop()
