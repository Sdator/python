import cv2
import os

# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))
# 打开图片


def 打开图片():
    img = cv2.imread("123.png")
    cv2.imshow("Output", img)
    cv2.waitKey(1000)


def 打开视频():
    cap = cv2.VideoCapture("test.mp4")
    while True:
        # 读取视频中每一帧
        success, img = cap.read()
        # 显示图片
        cv2.imshow("Video", img)
        # 1毫秒显示一张等同播放视频 按 q 退出
        if cv2.waitKey(1) & 0xff == ord('q'):
            break


def 打开摄像头():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # 设置宽度
    cap.set(4, 480)  # 设置告诉
    cap.set(10, 100)  # 设置亮度
    while True:
        # 读取视频中每一帧
        success, img = cap.read()
        # 显示图片
        cv2.imshow("Video", img)
        # 1毫秒显示一张等同播放视频 按 q 退出
        if cv2.waitKey(1) & 0xff == ord('q'):
            break


# 打开图片()
# 打开视频()
打开摄像头()
