from greengraph.map import Map
from greengraph.graph import Greengraph
from mock import patch
import geopy
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
import os
import yaml

start = "London"
end = "Durham"

def test_Greengraph_init():
    #Test instance of Greengraph class instantiated correctly
    with patch.object(geopy.geocoders,'GoogleV3') as mock_GoogleV3:
        test_Greengraph = Greengraph(start,end)
        #Test that GoogleV3 is called with the correct parameters
        mock_GoogleV3.assert_called_with(domain="maps.google.co.uk")
        #Test that the start and end fields are initialised correctly
        assert_equal(test_Greengraph.start,start)
        assert_equal(test_Greengraph.end,end)

def test_geolocate():
    #Test that the geolocate method returns the correct latitude and longitude coordinates for various places
        with open(os.path.join(os.path.dirname(__file__),"fixtures","geolocate.yaml")) as fixtures_file:
            test_Greengraph = Greengraph(start,end)
            fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            assert_almost_equal(
            test_Greengraph.geolocate(fixture.pop("place")),(fixture.pop("lat"),fixture.pop("lon"))
            )

def test_location_sequence():
    #Test that the location_sequence method computes the steps between two coordinates correctly
    test_Greengraph = Greengraph(start,end)
    test_sequence = test_Greengraph.location_sequence((0,0),(50,50),6)
    expected_results = [0.,10.,20.,30.,40.,50.]
    i = 0
    for result in expected_results:
        test_Greengraph = Greengraph(start,end)
        assert_equal(test_sequence[i][0],result)
        assert_equal(test_sequence[i][1],result)
        i += 1
