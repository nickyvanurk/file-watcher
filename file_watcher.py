import contextlib, time, os, collections, argparse

def get_command_line_args():
  defaults = {'path': '.', 'filename': None,'extensions': '*', 'commands': 'make'}

  parser = argparse.ArgumentParser()
  parser.add_argument('-p', dest='path', help='path of the directory tree to watch')
  parser.add_argument('-f', dest='filename', help='path of the file to watch')
  parser.add_argument('-e', dest='extensions', help='extentions to watch')
  parser.add_argument('-c', dest='commands', help='commands to execute')
  namespace = parser.parse_args()
  command_line_args = {k:v for k, v in vars(namespace).items() if v}

  return collections.ChainMap(command_line_args, defaults)

def get_files_in_dir(path):
  file_list = []
  for dir_name, subdirs, files in os.walk(path):
    for file in files:
      file_list.append(os.path.join(dir_name, file))
  return file_list

def main():
  args = get_command_line_args()

  while True:
    files = get_files_in_dir(args['path']);
    time.sleep(1)

if __name__ == '__main__':
  with contextlib.suppress(KeyboardInterrupt):
    main()
