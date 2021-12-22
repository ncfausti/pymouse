import sys
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    press_or_release = 'Pressed' if pressed else 'Released'
    if pressed:
        print('[{', '"x":{0}, "y":{1}, "button": "{2}", "action":"{3}"'.format(x, y, button, press_or_release), '},')
        sys.stdout.flush()
    else:
        print('{', '"x":{0}, "y":{1}, "button": "{2}", "action":"{3}"'.format(x, y, button, press_or_release), '}]')
        sys.stdout.flush()

with Listener(on_click=on_click) as listener:
    listener.join()
