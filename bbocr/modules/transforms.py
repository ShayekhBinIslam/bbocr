#-*- coding: utf-8 -*-
from __future__ import print_function
#-------------------------
# imports
#-------------------------
from abc import ABCMeta, abstractmethod

class PaperEdgeLocalDistortionPostProcessor(metaclass=ABCMeta):
    """Recognizer base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_rectified_image_from_backward_mapping(self):
        pass