from unittest import TestCase

from dockerhostdriver import DockerHostDriver


class DescribeDockerHostDriver  (TestCase):

    def test_it_can_be_initialized(self):
        driver = DockerHostDriver()
        self.assertIsNotNone(driver, "Driver can't be none")