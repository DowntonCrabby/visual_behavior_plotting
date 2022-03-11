import allensdk
from allensdk.brain_observatory.behavior.behavior_project_cache import VisualBehaviorOphysProjectCache
import matplotlib.pyplot as plt
import numpy as np
import path as Path
import pytest

from plotting.neural_plots import *

@pytest.fixture(autouse=True)
def set_variables():
    data_storage_directory = Path("/./visual_behavior_ophys_cache_dir")
    cache = VisualBehaviorOphysProjectCache.from_s3_cache(cache_dir=data_storage_directory)
    pytest.experiment_data = cache.get_behavior_ophys_experiment(940433497)
    assert("ophys_experiment_id" in pytest.experiment_data)

    return

def test_plot_max_intensity_projection():
    fig, ax = None
    def decorator_plot_func():
        assert('max_projection' in pytest.experiment_data)
        fig, ax = plot_max_intensity_projection(pytest.experiment_data) # plotting
        assert(fig != None)
    
    decorator_plot_func()
    assert(fig is None)
    assert(True)

def test_plot_segmentation_masks():
    fig, ax = None
    def decorator_plot_func():
        assert('segmentation_mask_image' in pytest.experiment_data)
        fig, ax = plot_segmentation_masks(pytest.experiment_data) # plotting
        assert(fig != None)

    decorator_plot_func()
    assert(fig is None)
    assert(True)

def test_plot_segmentation_mask_overlay():
    fig, ax = None
    def decorator_plot_func():
        assert('segmentation_mask_image' in pytest.experiment_data)
        fig, ax = plot_segmentation_mask_overlay(pytest.experiment_data) # plotting
        assert(fig != None)
    
    decorator_plot_func()
    assert(fig is None)
    assert(True)

def test_plot_dff():
    fig, ax = None
    def decorator_plot_func():
        assert('dff' in pytest.experiment_data) 
        fig, ax = plot_dff(pytest.experiment_data) # plotting
        assert(fig != None)
    
    decorator_plot_func()
    assert(fig is None)
    assert(True)

def test_plot_dff_heatmap():
    fig, ax = None
    def decorator_plot_func():
        assert('dff' in pytest.experiment_data) 
        fig, ax = plot_dff_heatmap(pytest.experiment_data) # plotting
        assert(fig != None)
    
    decorator_plot_func()
    assert(fig is None)
    assert(True)