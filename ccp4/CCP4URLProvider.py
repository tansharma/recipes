#!/usr/bin/python
#

from subprocess import Popen, PIPE
from autopkglib import Processor, ProcessorError

__all__ = ["CCP4URLProvider"]

BASE_URL = "http://series-70.fg.oisin.rc-harwell.ac.uk/update/macosx-x86_64/"

class CCP4URLProvider(Processor):
    """Provides URL to the latest Firefox release."""
    description = __doc__
    input_variables = {
        "product_name": {
            "required": False,
            "description":
                "Product to fetch URL .",
        },
        "base_url": {
            "required": False,
            "description": "Default is '%s." % BASE_URL,
        },
    }
    output_variables = {
        "url": {
            "description": "URL to the latest CCP4 product release.",
        },
    }

    def get_ccp4_url(self, base_url, product_name):
        # Construct download URL.
        return base_url % (product_name)

    def main(self):
        """Provide a CCP4 download URL"""
        # Determine product_name,  and base_url.
        product_name = self.env["product_name"]
        base_url = self.env.get(BASE_URL)

        self.env["url"] = self.get_ccp4_url(
            base_url, product_name)
        self.output("Found URL %s" % self.env["url"])


if __name__ == "__main__":
    PROCESSOR = CCP4URLProvider()
    PROCESSOR.execute_shell()
