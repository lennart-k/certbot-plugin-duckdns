from typing import Optional
import zope.interface
import logging
import requests
from time import sleep

from certbot import interfaces, errors
from certbot.plugins.dns_common import DNSAuthenticator

LOGGER = logging.getLogger(__name__)

DUCKDNS_URL = "https://www.duckdns.org/update?domains={domains}&token={token}&txt={txt}&clear={clear}"


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(DNSAuthenticator):
    description = "Obtain certificates using a DNS TXT record"

    credentials: Optional[str] = None

    @classmethod
    def add_parser_arguments(cls, add) -> None:
        super().add_parser_arguments(add)
        add("token", help="DuckDNS token")

    def more_info(self) -> str:
        return "This plugin configures a DNS TXT record using the DuckDNS API."

    def _setup_credentials(self):
        pass

    def _perform(self, domain: str, validation_name: str, validation: str):
        domains = domain.split(".duckdns.org", 1)[0]
        response = requests.get(
            DUCKDNS_URL.format(domains=domains, token=self.conf("token"),
                               txt=validation, clear="false"))
        if response.text != "OK":
            raise errors.PluginError("DuckDNS API returned an error")
        LOGGER.info(response.text)
        sleep(5)

    def _cleanup(self, domain: str, validation_name: str, validation: str):
        domains = domain.split(".duckdns.org", 1)[0]
        response = requests.get(
            DUCKDNS_URL.format(domains=domains, token=self.conf("token"),
                               txt="nice", clear="true"))
        if response.text != "OK":
            raise errors.PluginError("DuckDNS API returned an error")
        LOGGER.info(response.text)
