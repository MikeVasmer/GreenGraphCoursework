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

    size = (10,10)
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

@patch('requests.get')
@patch('matplotlib.image.imread')
@patch('StringIO.StringIO')
def test_count_green(mock_get,mock_imread,mock_StringIO):

    lat = 50
    lon = 50
    testMap = Map(lat,lon)
    size = (10,10)

    #Test that the number sum of the green pixels with values greater than the values of both the red and blue pixels is zero for an empty image (zeros everywhere)
    green = np.zeros(size)
    red = np.zeros(size)
    blue = np.zeros(size)
    testMap.pixels = np.dstack((red,green,blue))
    assert_equal(testMap.count_green(),0)

    #Test that the sum of the green pixels with values greater than the values of both the red and blue pixels is n*m for a n*m*3 array with the value of green pixels equal to one and red/blue pixels equal to zero
    green = np.ones(size)
    testMap.pixels = np.dstack((red,green,blue))
    assert_equal(testMap.count_green(),size[0]*size[1])
