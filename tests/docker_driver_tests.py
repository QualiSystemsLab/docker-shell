from unittest import TestCase

from dockerhostdriver import DockerHostDriver


class DockerApiService(object):

    def get_address_information(self, container_id):
        #some implementation of which APIs to call..:



class DescribeDockerHostDriverRefreshIP  (TestCase):

    def it_can_be_initialized(self):
        driver = DockerHostDriver()
        self.assertIsNotNone(driver, "Driver can't be none")


    def it_gets_the_ip_from_the_container(self):

        context=None
        ports = ''

        docker_api_service = DockerApiService()

        driver = DockerHostDriver(docker_api_service)

        #Given I have a docker host up with an IP of x
        #When I refresh the IP
        #The driver should poll the docker API for the IP


        driver.remote_refresh_ip(context,ports)

        docker_api_service.WasCalled("get_address_information")





    def it_sets_the_updated_ip_on_the_cloudshell_resource(self):
        pass

    def it_gets_specific_port_information_for_each_protocol(self):
        pass

    def it_sets_the_specific_port_information_on_the_cloudshell_resource(self):
        pass

    def it_returns_an_intelligible_error_message_if_host_is_unreachable(self):
        pass
