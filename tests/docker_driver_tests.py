from unittest import TestCase

from dockerhostdriver import DockerHostDriver


class DescribeDockerHostDriver  (TestCase):

    def test_it_can_be_initialized(self):
        driver = DockerHostDriver()
        self.assertIsNone(driver,msg="Can't allow that can we")