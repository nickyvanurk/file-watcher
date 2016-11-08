import file_watcher

def test_get_command_line_args():
  args = file_watcher.get_command_line_args()

  assert args['path'] == '.'
  assert args['filename'] == None
  assert args['extensions'] == '*'
  assert args['commands'] == 'make'

def test_get_files_in_dir():
  files = file_watcher.get_files_in_dir('./test-dir');

  assert len(files) == 1
  assert files[0] == './test-dir/test_file.txt'
