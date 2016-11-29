#!/usr/bin/python3
import contextlib, time, os, collections, argparse

def get_command_line_args():
  defaults = {'path': '.', 'filename': None,'extensions': '*', 'commands': 'make', 'interval': '500'}

  parser = argparse.ArgumentParser()
  parser.add_argument('-p', dest='path', help='path of directory tree to watch')
  parser.add_argument('-f', dest='filename', help='path of file to watch')
  parser.add_argument('-e', dest='extensions', help='extensions to watch')
  parser.add_argument('-c', dest='commands', help='commands to execute')
  parser.add_argument('-i', dest='interval', help='interval in milliseconds')
  namespace = parser.parse_args()
  command_line_args = {k:v for k, v in vars(namespace).items() if v}

  return collections.ChainMap(command_line_args, defaults)

def get_files_in_dir(path):
  file_list = []
  for dir_name, subdirs, files in os.walk(path):
    for file in files:
      file_list.append(os.path.join(dir_name, file))

  return file_list

def get_file_last_mod(path):
  return os.stat(path)[8];

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

def main():
  args = get_command_line_args()
  path = args['path']

  files_data = get_files_data(path)

  while True:
    time.sleep(int(args['interval']) / 1000)

    temp = get_files_data(path)
    unshared_items = set(files_data.items()) ^ set(temp.items())

    if len(unshared_items) != 0:
      filename = unshared_items.pop()[0]
      file_ext = filename.split('.')[-1]

      if (filename == args['filename'] or
          '*' == args['extensions'] or
          file_ext in args['extensions']):
        os.system(args['commands'])

    files_data = get_files_data(path)

if __name__ == '__main__':
  with contextlib.suppress(KeyboardInterrupt):
    main()
