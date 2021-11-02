#pip install moviepy
from moviepy.editor import VideoFileClip, concatenate_videoclips
video_1=VideoFileClip("11.mp4")
video_2=VideoFileClip("22.mp4")
final_video=concatenate_videoclips([video_1,video_2])
final_video.write_videofile("o.mp4")
