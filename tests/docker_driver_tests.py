from unittest import TestCase
from mock import Mock
from dockerhostdriver import DockerHostDriver
from refresh_ip_request import RefreshIpRequest
from cloudshell.shell.core.context import ResourceCommandContext


class CloudShellContextObjectStub(object):
    def __init__(self, resource_name):
        self.resource = ""


class DockerNewDriver(object):
    def __init__(self, docker_api_service, cloudshell_service):
        self.docker_api_service = docker_api_service
        self.cloudshell_service=cloudshell_service

    def refresh_ip(self):
        ip = self.docker_api_service.get_container_ip()
        self.cloudshell_service.set_resource_address(ip)


class StubDockerApiService:

    def get_container_ip(self):
        return self.ip_to_return


class DescribeRefreshIPOnDockerHostDriver (TestCase):


    def it_gets_the_ip_from_the_docker_host(self):
        docker_api_service = Mock()
        cloudshell_service = Mock()

        driver = DockerNewDriver(docker_api_service,cloudshell_service).refresh_ip()
        docker_api_service.get_container_ip.assert_called()

    def it_updates_cloudshell_with_the_ip_it_got_from_the_docker_host(self):
        docker_api_service = Mock(spec=StubDockerApiService)
        docker_api_service.get_container_ip.return_value="192.12.33.22"
        print docker_api_service.get_container_ip()
        cloudshell_service = Mock()

        DockerNewDriver(docker_api_service,cloudshell_service).refresh_ip()
        cloudshell_service.set_resource_address.assert_called_once_with("192.12.33.22")


    #
    #
    #
    #
    #
    #
    # def it_converts_the_cloudshell_execution_context_to_a_refresh_ip_request(self):
    #     mock_domain_logic = Mock()
    #     driver = DockerHostDriver(mock_domain_logic)
    #     driver.remote_refresh_ip(context=CloudShellContextObjectStub("resource1"), ports="")
    #     mock_domain_logic.refresh_ip.assert_called_once_with(RefreshIpRequest("resource1"))
    #     self.assertTrue(False)

