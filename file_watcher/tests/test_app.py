import os, file_watcher
from testfixtures import TempDirectory


tempdir = TempDirectory()
path = tempdir.makedir('tests/fixtures')
tempdir.write('tests/fixtures/test.txt', b'')

def teardown_module(module):
  TempDirectory.cleanup_all();


def test_get_files_in_dir():
  files = file_watcher.get_files_in_dir(path)
  assert len(files) == 1
  assert files[0] == path + '/test.txt'


def test_get_file_last_mod():
  last_mod_time = file_watcher.get_file_last_mod(path + '/test.txt')
  assert last_mod_time == os.stat(path + '/test.txt')[8]


def test_get_files_last_mod():
  files = file_watcher.get_files_in_dir(path)
  files_last_mod = file_watcher.get_files_last_mod(files)
  assert len(files_last_mod) == 1
  assert files_last_mod[0] == os.stat(files[0])[8]


def test_get_files_data():
  files_data = file_watcher.get_files_data(path)
  assert len(files_data) == 1
  assert list(files_data.keys())[0] == path + '/test.txt'
  assert list(files_data.values())[0] == os.stat(path + '/test.txt')[8]
