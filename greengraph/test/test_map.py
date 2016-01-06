from greengraph.map import Map
import numpy as np
from nose.tools import assert_equal
from mock import patch
import os

@patch('requests.get')
@patch('matplotlib.image.imread')
@patch('StringIO.StringIO')
def test_green(mock_get,mock_imread,mock_StringIO):

    def assert_images_equal(r,g,b,checkArray):
        testMap.pixels = np.dstack((r,g,b))
        np.testing.assert_array_equal(testMap.green(threshold),checkArray)

    lat = 50
    lon = 50
    testMap = Map(lat,lon)

    size = (400,400)
    trueArray = np.ones(size,dtype=bool)
    falseArray = np.zeros(size,dtype=bool)
    threshold = 1

    #Check the returned array is false everywhere when the value of the green pixels is identical to the values of the red and blue pixels
    green = np.ones(size)
    red = np.ones(size)
    blue = np.ones(size)
    assert_images_equal(red,green,blue,falseArray)

    #Check the returned array is false everywhere when the value of the green pixels is greater than the value of the blue pixels but less than the value of the red pixels
    blue = np.zeros(size)
    assert_images_equal(red,green,blue,falseArray)

    #As above but with red and blue pixels switched
    red = np.zeros(size)
    blue = np.ones(size)
    assert_images_equal(red,green,blue,falseArray)

    #Check the returned array is true everywhere when the value of the green pixels is greater than the value of the red and blue pixels
    blue = np.zeros(size)
    assert_images_equal(red,green,blue,trueArray)
