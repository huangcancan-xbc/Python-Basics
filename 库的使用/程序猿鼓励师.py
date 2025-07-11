import random
from pynput import keyboard
from playsound import playsound
from threading import Thread

soundList = ['sound/1.mp3']

# 记录当前用户按了多少次键盘
count = 0

def onRelease(key):
    """
    这个函数，就是在用户释放键盘按键的时候，就会被调用到。
    这个函数不是咱们自己主动调用的，而是把这个函数交给了 Listener，
    由 Listener 在用户释放按键的时候自动调用。
    不是咱们自己主动调用，而是交给别人，在合适的时机进行调用，这样的函数，叫做“回调函数”（callback function）
    :param key: 用户按下了哪个键
    """
    print(key)
    global count
    count += 1
    if count % 20 == 0:
        # 播放音频!
        # 生成随机数
        i = random.randint(0, len(soundList) - 1)
        # 此处的播放音频，消耗时间比较多，可能会引起输入的卡顿(不流畅)
        # 可以创建一个线程，在线程里播放音频!!
        # playsound(soundList[i])
        t = Thread(target=playsound, args=(soundList[i],))
        t.start()

# 当我们创建好 Listener 之后，用户的键盘按键动作就会被捕获到。
# 还希望在捕获到之后能够执行一段代码。
listener = keyboard.Listener(on_release=onRelease)
listener.start()
listener.join()

# 编写一段代码，感受一下这个程序的效果
# 播放音频可能出现卡顿