import os
import pytest


@pytest.yield_fixture(scope='session')
def dir_path(tmpdir_factory):
    """
    Setup our fixture directory.

    :param tmpdir_factor: Pytest fixture
    :return: Directory path
    """
    path = tmpdir_factory.mktemp('data')
    yield str(path)


@pytest.yield_fixture(scope='session')
def file_path(dir_path):
    """
    Setup our test data.

    :param dir: Pytest fixture
    :return: File path
    """
    p = os.path.join(dir_path, 'test.txt')
    with open(p, 'w') as f:
        f.write('Hello World!')
    yield p
