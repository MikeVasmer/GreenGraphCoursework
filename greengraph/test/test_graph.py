from greengraph.map import Map
from greengraph.graph import Greengraph
from mock import Mock, patch, call
import numpy as np
import geopy
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
import os
import yaml

start = "London"
end = "Durham"


def test_Greengraph_init():
    with patch.object(geopy.geocoders, 'GoogleV3') as mock_GoogleV3:
        test_Greengraph = Greengraph(start, end)
        # Test that GoogleV3 is called with the correct parameters
        mock_GoogleV3.assert_called_with(domain="maps.google.co.uk")
        # Test that the start and end fields are initialised correctly
        assert_equal(test_Greengraph.start, start)
        assert_equal(test_Greengraph.end, end)


def test_geolocate():
    # Test that the geolocate method calls the geocode method of the GoogleV3
    # class with the expected parameters
    with patch.object(geopy.geocoders.GoogleV3, "geocode") as mock_geocode:
        test_Greengraph = Greengraph(start, end)
        test_Greengraph.geolocate(start)
        mock_geocode.assert_called_with(start, exactly_one=False)


def test_location_sequence():
    # Test that the location_sequence method computes the steps between two
    # coordinates correctly
    test_Greengraph = Greengraph(start, end)

    with open(os.path.join(os.path.dirname(__file__), "fixtures", "location_sequence.yaml")) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            expected_results = fixture.pop("result")
            i = 0
            test_sequence = test_Greengraph.location_sequence(
                (fixture.pop("startlat"), fixture.pop("startlon")), (fixture.pop("endlat"), fixture.pop("endlon")), fixture.pop("steps"))
            for result in expected_results:
                assert_equal(test_sequence[i][0], result)
                assert_equal(test_sequence[i][1], result)
                i += 1


@patch("greengraph.map.Map.count_green")
@patch("greengraph.graph.Greengraph.geolocate")
def test_green_between(mock_count_green, mock_geolocate):
    # Test Map objects created during green_between method are called with the
    # expected parameters
    with patch.object(Greengraph, "location_sequence") as mock_location_sequence:
        mock_location_sequence.return_value = [
            [0., 0.], [1., 1.], [2., 2.], [3., 3.]]
        expected_calls = [call(0.0, 0.0), call(
            1.0, 1.0), call(2.0, 2.0), call(3.0, 3.0)]
        with patch.object(Map, "__init__") as mock_Map_init:
            mock_Map_init.return_value = None
            test_Greengraph = Greengraph(start, end)
            test_Greengraph.green_between(6)
            mock_Map_init.assert_has_calls(expected_calls)
