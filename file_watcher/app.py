#!/usr/bin/python3
import contextlib
import time
import os
import click


@click.command()
@click.option('--path', '-p',  default='.',
              help='Path of directory tree to watch.')
@click.option('--file', '-f', default=None, help='Path of file to watch.')
@click.option('--exts', '-e', default='*', help='Extensions to watch.')
@click.option('--cmds', '-c', default='make', help='Commands to execute.')
@click.option('--interval', '-i', default=500,
              help='Scan interval in milliseconds.')
def main(path, file, exts, cmds, interval):
    files_data = get_files_data(path)

    while True:
        time.sleep(int(interval) / 1000)

        temp = get_files_data(path)
        unshared_items = set(files_data.items()) ^ set(temp.items())

        if len(unshared_items) != 0:
            filename = unshared_items.pop()[0]
            file_ext = filename.split('.')[-1]

            if filename == file or '*' == exts or file_ext in exts:
                os.system(cmds)

        files_data = get_files_data(path)


def get_files_in_dir(path):
    file_list = []
    for dir_name, subdirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(dir_name, file))

    return file_list


def get_file_last_mod(path):
    return os.stat(path)[8]


def get_files_last_mod(files):
    files_last_mod = []
    for file_path in files:
        file_last_mod = get_file_last_mod(file_path)
        files_last_mod.append(file_last_mod)

    return files_last_mod


def get_files_data(path):
    files = get_files_in_dir(path)
    files_last_mod = get_files_last_mod(files)

    return dict(zip(files, files_last_mod))


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt):
        main()
