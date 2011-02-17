class BaseTransitLineStatusProvider:
    
    def get_status(self):
        # Return a list of dictionaries, where the dictionaries have keys
        # of "line_name", "status" and optional "disruption_reason"
        return {}

from tfl import TubeStatusProvider
from spt import SubwayStatusProvider