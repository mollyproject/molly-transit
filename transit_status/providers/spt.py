from transit_status.providers import BaseTransitLineStatusProvider
from lxml import etree
import urllib2

class SubwayStatusProvider(BaseTransitLineStatusProvider):
    
    JOURNEYCHECK_URL = 'http://www.spt.co.uk/journeycheck/index.aspx'
    
    def get_status(self):
        statuses = []
        xml = etree.parse(urllib2.urlopen(self.JOURNEYCHECK_URL), parser = etree.HTMLParser())
        ul = xml.find(".//ul[@id='jc']")
        for li in ul:
            statuses.append({
                'line_name': ''.join(li.itertext()).strip(),
                'status': li.find(".//img").attrib['alt']
            })
        return statuses