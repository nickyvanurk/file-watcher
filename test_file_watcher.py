import file_watcher

def test_get_command_line_args():
  args = file_watcher.get_command_line_args()

  assert args['path'] == '.'
  assert args['filename'] == None
  assert args['extensions'] == '*'
  assert args['commands'] == 'make'

def test_main():
  file_watcher.main()
