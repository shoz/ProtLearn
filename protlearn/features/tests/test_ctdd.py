import pytest
import numpy as np
from ..ctdd import ctdd
import pkg_resources

PATH = pkg_resources.resource_filename(__name__, 'test_data/')

def test_ctdd():
    "Test CTD distribution"
    
    # load data
    X_list = open(PATH+'multiple.txt').read().splitlines()
    X_err = 'AGT2HT9'
    
    # get ctdd
    ctdd_list, desc = ctdd(X_list)
    
    # test ctdd
    np.testing.assert_almost_equal(ctdd_list, 
    np.array([[  0.        ,   0.        ,   0.        ,   0.        ,
          0.        ,  14.28571429,  14.28571429,  28.57142857,
         42.85714286,  57.14285714,  71.42857143, 100.        ,
         71.42857143,  85.71428571, 100.        ,  42.85714286,
         57.14285714,  42.85714286,  42.85714286,  57.14285714,
         14.28571429,  14.28571429,  28.57142857,  71.42857143,
        100.        ,   0.        ,   0.        ,   0.        ,
          0.        ,   0.        ,  42.85714286,  71.42857143,
         42.85714286,  57.14285714,  71.42857143,  14.28571429,
         28.57142857,  14.28571429,  14.28571429,  28.57142857,
         85.71428571, 100.        ,  85.71428571,  85.71428571,
        100.        ,  42.85714286,  57.14285714,  42.85714286,
         42.85714286,  57.14285714,   0.        ,   0.        ,
          0.        ,   0.        ,   0.        ,  14.28571429,
         14.28571429,  28.57142857,  71.42857143, 100.        ,
         57.14285714,  57.14285714,  57.14285714,  57.14285714,
         57.14285714,  14.28571429,  42.85714286,  14.28571429,
         28.57142857,  42.85714286,  71.42857143, 100.        ,
         71.42857143,  85.71428571, 100.        ,  42.85714286,
         57.14285714,  42.85714286,  42.85714286,  57.14285714,
         14.28571429,  71.42857143,  14.28571429,  28.57142857,
         71.42857143,  85.71428571, 100.        ,  85.71428571,
         85.71428571, 100.        ,  14.28571429,  42.85714286,
         14.28571429,  28.57142857,  42.85714286,  57.14285714,
         57.14285714,  57.14285714,  57.14285714,  57.14285714,
         71.42857143, 100.        ,  71.42857143,  85.71428571,
        100.        ,  14.28571429,  28.57142857,  14.28571429,
         14.28571429,  28.57142857,  85.71428571, 100.        ,
         85.71428571,  85.71428571, 100.        ,  42.85714286,
         71.42857143,  42.85714286,  57.14285714,  71.42857143,
         71.42857143, 100.        ,  71.42857143,  85.71428571,
        100.        ,  14.28571429,  28.57142857,  14.28571429,
         14.28571429,  28.57142857,  42.85714286,  57.14285714,
         42.85714286,  42.85714286,  57.14285714,  14.28571429,
         28.57142857,  14.28571429,  14.28571429,  28.57142857,
         85.71428571, 100.        ,  85.71428571,  85.71428571,
        100.        ,  42.85714286,  71.42857143,  42.85714286,
         57.14285714,  71.42857143,  42.85714286,  57.14285714,
         42.85714286,  42.85714286,  57.14285714,  14.28571429,
         14.28571429,  28.57142857,  71.42857143, 100.        ,
          0.        ,   0.        ,   0.        ,   0.        ,
          0.        ,  14.28571429,  14.28571429,  42.85714286,
         57.14285714, 100.        ,  71.42857143,  71.42857143,
         71.42857143,  71.42857143,  71.42857143,   0.        ,
          0.        ,   0.        ,   0.        ,   0.        ,
         14.28571429,  14.28571429,  28.57142857,  85.71428571,
        100.        ,  42.85714286,  57.14285714,  42.85714286,
         42.85714286,  57.14285714,  71.42857143,  71.42857143,
         71.42857143,  71.42857143,  71.42857143],
       [ 22.22222222,  22.22222222,  55.55555556,  77.77777778,
        100.        ,  44.44444444,  44.44444444,  44.44444444,
         44.44444444,  44.44444444,  11.11111111,  11.11111111,
         33.33333333,  66.66666667,  88.88888889,  22.22222222,
         22.22222222,  66.66666667,  77.77777778, 100.        ,
         11.11111111,  33.33333333,  11.11111111,  11.11111111,
         33.33333333,  44.44444444,  44.44444444,  44.44444444,
         44.44444444,  44.44444444,  22.22222222,  22.22222222,
         55.55555556,  66.66666667,  88.88888889,  77.77777778,
        100.        ,  77.77777778,  77.77777778, 100.        ,
         11.11111111,  44.44444444,  11.11111111,  33.33333333,
         44.44444444,  22.22222222,  55.55555556,  22.22222222,
         22.22222222,  55.55555556,  66.66666667,  66.66666667,
         77.77777778,  88.88888889, 100.        ,  11.11111111,
         44.44444444,  11.11111111,  33.33333333,  44.44444444,
         22.22222222,  22.22222222,  55.55555556,  66.66666667,
         88.88888889,  77.77777778, 100.        ,  77.77777778,
         77.77777778, 100.        ,  11.11111111,  44.44444444,
         11.11111111,  33.33333333,  44.44444444,  22.22222222,
         55.55555556,  22.22222222,  22.22222222,  55.55555556,
         66.66666667,  66.66666667,  77.77777778,  88.88888889,
        100.        ,  11.11111111,  44.44444444,  11.11111111,
         33.33333333,  44.44444444,  22.22222222,  22.22222222,
         55.55555556,  77.77777778, 100.        ,  44.44444444,
         44.44444444,  44.44444444,  44.44444444,  44.44444444,
         11.11111111,  11.11111111,  33.33333333,  66.66666667,
         88.88888889,  44.44444444,  44.44444444,  66.66666667,
         77.77777778, 100.        ,  11.11111111,  33.33333333,
         11.11111111,  22.22222222,  33.33333333,   0.        ,
          0.        ,   0.        ,   0.        ,   0.        ,
         11.11111111,  44.44444444,  11.11111111,  33.33333333,
         44.44444444,  66.66666667,  66.66666667,  77.77777778,
         88.88888889, 100.        ,  22.22222222,  55.55555556,
         22.22222222,  22.22222222,  55.55555556,  55.55555556,
        100.        ,  55.55555556,  77.77777778, 100.        ,
         11.11111111,  11.11111111,  33.33333333,  44.44444444,
         88.88888889,   0.        ,   0.        ,   0.        ,
          0.        ,   0.        ,   0.        ,   0.        ,
          0.        ,   0.        ,   0.        ,  11.11111111,
         11.11111111,  44.44444444,  77.77777778, 100.        ,
         22.22222222,  55.55555556,  22.22222222,  22.22222222,
         55.55555556,  11.11111111,  33.33333333,  11.11111111,
         22.22222222,  33.33333333,  44.44444444,  44.44444444,
         44.44444444,  44.44444444,  44.44444444,  55.55555556,
         55.55555556,  66.66666667,  77.77777778, 100.        ,
         11.11111111,  11.11111111,  33.33333333,  44.44444444,
        100.        ,  22.22222222,  55.55555556,  22.22222222,
         22.22222222,  55.55555556,  66.66666667,  88.88888889,
         66.66666667,  66.66666667,  88.88888889],
       [ 62.5       , 100.        ,  62.5       ,  87.5       ,
        100.        ,  12.5       ,  12.5       ,  25.        ,
         37.5       ,  75.        ,   0.        ,   0.        ,
          0.        ,   0.        ,   0.        ,  12.5       ,
         12.5       ,  62.5       ,  87.5       , 100.        ,
         25.        ,  50.        ,  25.        ,  37.5       ,
         50.        ,  75.        ,  75.        ,  75.        ,
         75.        ,  75.        ,  12.5       ,  12.5       ,
         62.5       ,  87.5       , 100.        ,  25.        ,
         50.        ,  25.        ,  37.5       ,  50.        ,
         75.        ,  75.        ,  75.        ,  75.        ,
         75.        ,  12.5       , 100.        ,  12.5       ,
         87.5       , 100.        ,  62.5       ,  62.5       ,
         62.5       ,  62.5       ,  62.5       ,  25.        ,
         25.        ,  37.5       ,  50.        ,  75.        ,
         62.5       , 100.        ,  62.5       ,  87.5       ,
        100.        ,  12.5       ,  12.5       ,  25.        ,
         37.5       ,  50.        ,  75.        ,  75.        ,
         75.        ,  75.        ,  75.        ,  12.5       ,
         12.5       ,  62.5       ,  87.5       , 100.        ,
         25.        ,  50.        ,  25.        ,  37.5       ,
         50.        ,  75.        ,  75.        ,  75.        ,
         75.        ,  75.        ,  12.5       ,  12.5       ,
         37.5       ,  62.5       , 100.        ,  75.        ,
         75.        ,  75.        ,  75.        ,  75.        ,
          0.        ,   0.        ,   0.        ,   0.        ,
          0.        ,  25.        ,  25.        ,  50.        ,
         75.        , 100.        ,  62.5       ,  62.5       ,
         62.5       ,  62.5       ,  62.5       ,  12.5       ,
         12.5       ,  12.5       ,  12.5       ,  12.5       ,
         75.        ,  75.        ,  75.        ,  75.        ,
         75.        ,  25.        ,  50.        ,  25.        ,
         37.5       ,  50.        ,  12.5       ,  12.5       ,
         62.5       ,  87.5       , 100.        ,  25.        ,
         25.        ,  37.5       ,  50.        , 100.        ,
         62.5       ,  75.        ,  62.5       ,  62.5       ,
         75.        ,  12.5       ,  12.5       ,  12.5       ,
         12.5       ,  12.5       ,  12.5       ,  12.5       ,
         12.5       ,  12.5       ,  12.5       ,  25.        ,
         25.        ,  37.5       ,  50.        ,  75.        ,
         87.5       , 100.        ,  87.5       ,  87.5       ,
        100.        ,  12.5       ,  12.5       ,  25.        ,
         37.5       ,  50.        ,  75.        ,  75.        ,
         75.        ,  75.        ,  75.        ,  62.5       ,
        100.        ,  62.5       ,  87.5       , 100.        ,
         25.        ,  25.        ,  37.5       ,  50.        ,
         75.        ,  12.5       ,  12.5       ,  62.5       ,
         87.5       , 100.        ,   0.        ,   0.        ,
          0.        ,   0.        ,   0.        ]])
    , decimal=3)

    # test ValueError
    with pytest.raises(ValueError):
        ctdd_error, desc = ctdd(X_err)