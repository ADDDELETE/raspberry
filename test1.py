import snowboydecoder
import sys
import signal

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

model = r'resources/snowboy.umdl'  # 修改model，指定其文件名

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# 唤醒词检测函数，调整sensitivity参数可修改唤醒词检测的准确性
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
# 回调函数 detected_callback=snowboydecoder.play_audio_file 
# 修改回调函数可实现我们想要的功能
detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

# 释放资源
detector.terminate()
