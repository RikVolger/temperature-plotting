import pytest
import os
import pandas as pd

import temperature_plotting as tpl


def test_compute_mean():
    calc = tpl.compute_mean([0, 10, 20])
    assert calc == 10
    assert type(calc) == float
    
    calc = tpl.compute_mean([-10, 10])
    assert calc == 0
    
    calc = tpl.compute_mean([0, 10, 0])
    assert calc == 10/3
    assert round(calc, 4) == 3.3333
    
    with pytest.raises(TypeError):
        calc = tpl.compute_mean(["a", "b", "c"])
    
    calc = tpl.compute_mean([])
    assert calc == None
    
    calc = tpl.compute_mean("")
    assert calc == None
        
    with pytest.raises(TypeError):
        calc = tpl.compute_mean("hello")
    
    with pytest.raises(TypeError):
        calc = tpl.compute_mean([None, 2, 0])


def test_create_name():
    name = tpl.create_name(5)
    assert name == "plot_0005.png"
    assert type(name) == str
    
    for num in range(0, 10):
        name = tpl.create_name(num)
        # other option to get extension is to split the string on dots, take last part.
        assert name.split(".")[-1] == "png"
        assert name[-8:-4] == f"{num:04}"


def test_read_data():
    data = tpl.read_data("data/temperatures.csv", "Air temperature (degC)", 10)
    assert len(data) == 10
    assert type(data) == pd.core.series.Series
    
    with pytest.raises(KeyError):
        data = tpl.read_data("data/temperatures.csv", "wrong column", 10)

        
def test_main():
    tpl.main()
    assert os.path.exists("plot_0025.png")




# In[ ]:




