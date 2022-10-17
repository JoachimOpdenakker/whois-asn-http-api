from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/", status_code=200)
async def get_asn_info(asn: str, host: str):
    """
    Get AS-name and ORG-name from whois service
    
    parameters:
        asn: AS number to lookup 
    """
    return get_info(asn=asn, host=host)

def get_info(asn: str, host: str):
    record = whois(asn, host)
    return record

def whois(asn, host):
    """ whois the source for the given ASN
    :param asn:         ASN number to get info on
    :param host:        whois hostname
    :return: dict of parsed attribute/values
    """
    WHOIS_CMD = ["whois", "-h", host, "AS%s" % asn]

    proc = subprocess.Popen(WHOIS_CMD,
                            stdout= subprocess.PIPE, stdin=None)

    output = (proc.stdout.read()).decode("utf-8", "ignore")
    proc.communicate()
    return output