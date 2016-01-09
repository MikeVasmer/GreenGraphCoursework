from greengraph.map import Map
import numpy as np
from nose.tools import assert_equal
from mock import patch
import os
import requests
import yaml

lat = 50
lon = 50
size = (10, 10)


@patch("matplotlib.image.imread")
@patch("StringIO.StringIO")
def test_Map_init(mock_imread, mock_StringIO):
    # Test that requests.get() is called with the expected default parameters
    # when creating an instance of the Map class
    with patch.object(requests, 'get') as mock_get:
        testMap = Map(lat, lon)
        mock_get.assert_called_with(
            "http://maps.googleapis.com/maps/api/staticmap?",
            params={
                "sensor": "false",
                "zoom": 10,
                "size": "400x400",
                "center": str(lat) + "," + str(lon),
                "style": "feature:all|element:labels|visibility:off",
                "maptype": "satellite"
            }
        )


@patch("requests.get")
@patch("matplotlib.image.imread")
@patch("StringIO.StringIO")
def test_green(mock_get, mock_imread, mock_StringIO):

    def assert_images_equal(r, g, b, checkArray):
        testMap.pixels = np.dstack((r, g, b))
        np.testing.assert_array_equal(testMap.green(threshold), checkArray)

    testMap = Map(lat, lon)
    threshold = 1
    green = np.ones(size)

    # Check that the green() method returns the correct logical matrix for
    # images with different combinations of red, green and blue pixels
    with open(os.path.join(os.path.dirname(__file__), "fixtures", "green.yaml")) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            if fixture.pop("redVal") == 1:
                red = np.ones(size)
            else:
                red = np.zeros(size)
            if fixture.pop("blueVal") == 1:
                blue = np.ones(size)
            else:
                blue = np.zeros(size)
            if fixture.pop("result") == True:
                checkArray = np.ones(size, dtype=bool)
            else:
                checkArray = np.zeros(size, dtype=bool)
            assert_images_equal(red, green, blue, checkArray)


@patch("requests.get")
@patch("matplotlib.image.imread")
@patch("StringIO.StringIO")
def test_count_green(mock_get, mock_imread, mock_StringIO):

    testMap = Map(lat, lon)

    # Test that the number sum of the green pixels with values greater than
    # the values of both the red and blue pixels is zero for an empty image
    # (zeros everywhere)
    green = np.zeros(size)
    red = np.zeros(size)
    blue = np.zeros(size)
    testMap.pixels = np.dstack((red, green, blue))
    assert_equal(testMap.count_green(), 0)

    # Test that the sum of the green pixels with values greater than the
    # values of both the red and blue pixels is n*m for a n*m*3 array with the
    # value of green pixels equal to one and red/blue pixels equal to zero
    green = np.ones(size)
    testMap.pixels = np.dstack((red, green, blue))
    assert_equal(testMap.count_green(), size[0] * size[1])
