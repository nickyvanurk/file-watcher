import collections, argparse

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

def main():
  args = get_command_line_args()

if __name__ == '__main__':
  main()
