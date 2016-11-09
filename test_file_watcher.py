import file_watcher

def test_get_command_line_args():
  args = file_watcher.get_command_line_args()

  assert args['path'] == '.'
  assert args['filename'] == None
  assert args['extensions'] == '*'
  assert args['commands'] == 'make'

def test_get_files_in_dir():
  files = file_watcher.get_files_in_dir('./test-dir')

  assert len(files) == 1
  assert files[0] == './test-dir/test_file.txt'

def test_get_file_last_mod():
  pathname = './test-dir/test_file.txt'
  last_mod_time = file_watcher.get_file_last_mod(pathname)

  assert last_mod_time == 1478643910

def test_get_files_last_mod():
  files = file_watcher.get_files_in_dir('./test-dir')
  files_last_mod = file_watcher.get_files_last_mod(files)

  assert len(files_last_mod) == 1
  assert files_last_mod[0] == 1478643910

def test_get_files_data():
  pathname = './test-dir'
  files_data = file_watcher.get_files_data(pathname)

  assert len(files_data) == 1
  assert list(files_data.keys())[0] == './test-dir/test_file.txt'
  assert list(files_data.values())[0] == 1478643910
