# from moviepy.editor import *

# # 修改当前工作目录为脚本运行目录
# os.chdir(os.path.dirname(__file__))

# %%
if __name__ == "__main__":
    # mp4 = r'D:\Git\编程\python\工具集\test.mp4'
    txt = r"D:\DATA\Desktop\新建文本文档 - 副本.txt"
    # video = VideoFileClip(mp4).subclip(50, 60)
    # # 制作文字
    # txt_clip = (TextClip("test", fontsize=70, color='white').set_position('center').set_duration(10))
    # # 添加字幕
    # result = CompositeVideoClip([video, txt_clip])
    # # 输出视频
    # result.write_videofile("myHolidays_edited.webm", fps=25)

# %%
    f = open(txt, "r")

# %%
    # data = f.readline()
    # utf8 = data.encode("utf-8")
    # q = data[:-1]  # 把字符串最后的换行符去掉
    # utf81 = q.encode("utf-8")
    # # print(type(data))
    # print(data == q, len(data))
    # print(data, 11)
    # print(q, 22)
    for v in f:
        print(v, type(v), 11)

    f.close()


# %%
