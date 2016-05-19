#!/usr/bin/python

from subprocess import Popen, PIPE
from autopkglib import Processor, ProcessorError

BASE_URL = "http://series-70.fg.oisin.rc-harwell.ac.uk/update/"

def main(self):
    url = BASE_URL 
    # Using curl to fetch Location header(s) because urllib/2
    proc = Popen(['/usr/bin/curl', '-ILs', url], stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    parsed_url = None
    if err:
        print (err)
        raise ProcessorError("curl returned an error: %s" % out)
        for line in out.splitlines():
            if line.startswith("Location"):
                parsed_url = line.split()[1]
        if not parsed_url:
            raise ProcessorError(
                "curl didn't find a resolved 'Location' header we can use. "
                "Full curl output:\n %s" % "\n".join(out.splitlines()))

    self.env["url"] = parsed_url

#if __name__ == "__main__":
    PROCESSOR = main()
    PROCESSOR.execute_shell()
