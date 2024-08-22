from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

video = VideoFileClip('video.mp4')
video.write_videofile('result.mp4')
short_video = video.subclip(8, 18)  # Mendapatkan 10 detik pertama
short_video.write_videofile('short_result.mp4')
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')
reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('reversed_result.mp4')
sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('sped_up_result.mp4')
root = tk.Tk()
root.title("Multimedia Application")
root.mainloop()
image = Image.open('example.jpg')
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()