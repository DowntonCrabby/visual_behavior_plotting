import sys,os
import pytest
import numpy as np
import path as Path
import matplotlib.pyplot as plt

import allensdk
from allensdk.brain_observatory.behavior.behavior_project_cache import VisualBehaviorOphysProjectCache


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plotting.behavior_plots import *

@pytest.fixture(autouse=True)
def set_variables():
    data_storage_directory = os.path.join(".","visual_behavior_ophys_cache_dir")
    cache = VisualBehaviorOphysProjectCache.from_s3_cache(cache_dir=data_storage_directory)
    pytest.experiment_data = cache.get_behavior_ophys_experiment(940433497)
    pytest.behavior_data = cache.get_behavior_session(870987812)
    assert("ophys_experiment_id" in pytest.experiment_data.list_data_attributes_and_methods())
    assert("behavior_session_id" in pytest.behavior_data.list_data_attributes_and_methods())
    return

def test_plot_behavioral_streams():
    fig = ax = None
    def decorator_plot_func():
        fig, ax = plot_behavioral_streams(pytest.experiment_data) # plotting
        assert(fig != None)
        fig, ax = plot_behavioral_streams(pytest.behavior_data) # plotting
        assert(fig != None)
    
    decorator_plot_func()
    assert(ax is None)
    assert(True)

def test_plot_running():
    fig = ax = None
    def decorator_plot_func():
        assert("running_speed" in pytest.experiment_data.list_data_attributes_and_methods() and "running_speed" in pytest.behavior_data.list_data_attributes_and_methods())
        ax = plot_running(pytest.experiment_data) # plotting
        assert(ax!= None)
        ax = plot_running(pytest.behavior_data) # plotting
        assert(ax != None)
    
    decorator_plot_func()
    assert(fig is None)
    assert(True)

def test_plot_pupil_area():
    fig = ax = None
    def decorator_plot_func():
        assert("eye_tracking" in pytest.experiment_data.list_data_attributes_and_methods() and "running_speed" in pytest.behavior_data.list_data_attributes_and_methods())
        ax = plot_pupil_area(pytest.experiment_data) # plotting
        assert(ax!= None)
        # ax = plot_pupil_area(pytest.behavior_data) # plotting
        # assert(ax != None)
    
    decorator_plot_func()
    assert(fig is None)
    assert(True)

def test_plot_licks():
    fig = ax = None
    def decorator_plot_func():
        assert("licks" in pytest.experiment_data.list_data_attributes_and_methods() and "licks" in pytest.behavior_data.list_data_attributes_and_methods())
        ax = plot_licks(pytest.experiment_data) # plotting
        assert(ax != None)
        ax = plot_licks(pytest.behavior_data) # plotting
        assert(ax != None)
    
    decorator_plot_func()
    assert(ax is None)
    assert(True)

def test_plot_rewards():
    fig = ax = None
    def decorator_plot_func():
        assert("rewards" in pytest.experiment_data.list_data_attributes_and_methods() and "rewards" in pytest.behavior_data.list_data_attributes_and_methods())
        ax = plot_rewards(pytest.experiment_data) # plotting
        assert(ax != None)
        ax = plot_rewards(pytest.behavior_data) # plotting
        assert(ax != None)
    
    decorator_plot_func()
    assert(ax is None)
    assert(True)

def test_plot_stimuli():
    fig = ax = None
    def decorator_plot_func():
        assert("stimulus_presentations" in pytest.experiment_data.list_data_attributes_and_methods() and "stimulus_presentations" in pytest.behavior_data.list_data_attributes_and_methods())
        ax = plot_stimuli(pytest.experiment_data) # plotting
        assert(ax != None)
        ax = plot_stimuli(pytest.behavior_data) # plotting
        assert(ax != None)
    
    decorator_plot_func()
    assert(ax is None)
    assert(True)
