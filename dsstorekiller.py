#!/usr/bin/env python3
import os
import subprocess

from fsevents import Observer, Stream


def main():
    path = os.path.expanduser('~')
    enemy_name = '.DS_Store'
    observer = Observer()

    def callback(path, mask):
        try:
            full_path = os.path.join(path, enemy_name)
            os.remove(full_path)
        except:
            pass

    stream = Stream(callback, path)
    observer.schedule(stream)
    observer.start()
    subprocess.call(['find', path, '-name', '\\' + enemy_name, '-delete'])
    observer.join()


if __name__ == '__main__':
    main()
