from greengraph.map import Map
import numpy as np
from nose.tools import assert_equal
import yaml

def test_green():
    size = (10,10)
    zoom = 10
    lat = 50
    lon = 50
    satellite = True
    testMap = Map(lat,lon,satellite,zoom,size)

    threshold = 1
    trueArray = np.ones(size,dtype=bool)
    falseArray = np.zeros(size,dtype=bool)

    def assert_images_equal(r,g,b,checkArray):
        testPixels = np.dstack((r,g,blue))
        testMap.pixels = testPixels
        np.testing.assert_array_equal(testMap.green(threshold),checkArray)

    green = np.ones(size)
    red = np.ones(size)
    blue = np.ones(size)
    assert_images_equal(red,green,blue,falseArray)

    blue = np.zeros(size)
    assert_images_equal(red,green,blue,falseArray)

    red = np.zeros(size)
    blue = np.ones(size)
    assert_images_equal(red,green,blue,falseArray)

    blue = np.zeros(size)
    assert_images_equal(red,green,blue,trueArray)
