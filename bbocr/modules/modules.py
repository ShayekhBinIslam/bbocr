#-*- coding: utf-8 -*-
from __future__ import print_function
#-------------------------
# imports
#-------------------------
from abc import ABCMeta, abstractmethod

class Recognizer(metaclass=ABCMeta):
    """Recognizer base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def infer(self):
        pass

class Detector(metaclass=ABCMeta):
    """Line and Word detector base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_word_boxes(self):
        pass

    @abstractmethod
    def get_line_boxes(self):
        pass
    
    @abstractmethod
    def get_crops(self):
        pass


class Detector(metaclass=ABCMeta):
    """Line and Word detector base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_word_boxes(self):
        pass

    @abstractmethod
    def get_line_boxes(self):
        pass
    
    @abstractmethod
    def get_crops(self):
        pass


class WordDetector(metaclass=ABCMeta):
    """Word detector base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_word_boxes(self):
        pass

    @abstractmethod
    def get_line_boxes(self):
        pass
    
    @abstractmethod
    def get_crops(self):
        pass

class LineDetector(metaclass=ABCMeta):
    """Line detector base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_word_boxes(self):
        pass

    @abstractmethod
    def get_line_boxes(self):
        pass
    
    @abstractmethod
    def get_crops(self):
        pass

class LayoutAnalyzer(metaclass=ABCMeta):
    """layout analyzer base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_rois(self):
        pass
    


class IlluminationCorrection(metaclass=ABCMeta):
    """Illumination correction base class
    """
    def __init__(self):
        pass

    @abstractmethod
    def get_corrected_image(self):
        pass


class GeometricRectification(metaclass=ABCMeta):
    """Geometric rectification base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_backward_mapping(self): 
        pass

    @abstractmethod
    def get_rectified_image(self):
        pass

    