import sys
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if pressed:
        print('{', '"x":{0}, "y":{1}, "button": "{2}"'.format(x, y, button), '}')
        sys.stdout.flush()


with Listener(on_click=on_click) as listener:
    listener.join()
