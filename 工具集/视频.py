from moviepy.editor import *

# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))

if __name__ == "__main__":
    mp4 = r'"D:\Git\编程\python\工具集\test.mp4"'
    video = VideoFileClip(mp4).subclip(50, 60)
    # 制作文字
    txt_clip = (TextClip("test", fontsize=70, color='white').set_position('center').set_duration(10))
    # 添加字幕
    result = CompositeVideoClip([video, txt_clip])
    # 输出视频
    result.write_videofile("myHolidays_edited.webm", fps=25)
