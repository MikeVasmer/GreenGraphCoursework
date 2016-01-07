from greengraph.map import Map
from greengraph.graph import Greengraph
from mock import patch
import geopy
from nose.tools import assert_equal

start = "London"
end = "Durham"

def test_Greengraph_init():
    with patch.object(geopy.geocoders,'GoogleV3') as mock_GoogleV3:
        test_Greengraph = Greengraph(start,end)
        #Test that GoogleV3 is called with the correct parameters
        mock_GoogleV3.assert_called_with(domain="maps.google.co.uk")
        #Test that the start and end fields are initialised correctly
        assert_equal(test_Greengraph.start,start)
        assert_equal(test_Greengraph.end,end)
