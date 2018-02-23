import os
import file_watcher


class TestApp(object):
    def test_get_files_in_dir(self, dir_path, file_path):
        """
        Traverse a directory and returns a list with filenames
        successfully.
        """
        files = file_watcher.get_files_in_dir(dir_path)
        assert len(files) == 1
        assert files[0] == file_path

    def test_get_files_data(self, dir_path, file_path):
        """ Zips filenames with last modified property successfully. """
        files_data = file_watcher.get_files_data(dir_path)
        assert len(files_data) == 1
        assert list(files_data.keys())[0] == file_path
        assert list(files_data.values())[0] == os.stat(file_path)[8]
