#-*- coding: utf-8 -*-
from __future__ import print_function
#-------------------------
# imports
#-------------------------
from abc import ABCMeta, abstractmethod



class BackwarpMappingToImage(metaclass=ABCMeta):
    """Recognizer base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_rectified_image(self):
        pass


class ImamgeCropperWithPadding(metaclass=ABCMeta):
    """Recognizer base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_patches(self):
        pass

class ImageComposer(metaclass=ABCMeta):
    """Recognizer base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_composed_image(self):
        ''' Input: Patches
        '''
        pass
      
      
class ImagePadder(metaclass=ABCMeta):
    """Recognizer base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_padded_image(self):
        ''' Input: Patches
        '''
        pass
  
  
class AspectRatioBasedImageResizer(metaclass=ABCMeta):
    """Recognizer base class
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_padded_image(self):
        ''' Input: Patches
        '''
        pass


class BengaliTextNormalizer(metaclass=ABCMeta):
    """A wrapper on bnunicodenormalizer
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def get_padded_image(self):
        ''' Input: Patches
        '''
        pass