from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import skimage
from skimage.feature import hog


class RGB2GrayTransformer(BaseEstimator, TransformerMixin):
    """
    Convert RGB images to grayscale.
    """
    def __init__(self):
        ...

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([skimage.color.rgb2gray(img) for img in X])

    
class HogTransformer(BaseEstimator, TransformerMixin):
    """
    Calculate HOG features for each picture.
    """
    def __init__(self, y=None, orientations=9, pixels_per_cell=(8, 8),
                 cells_per_block=(3, 3), block_norm='L2-Hys'):
        self.y = y
        self.orientations = orientations
        self.pixels_per_cell = pixels_per_cell
        self.cells_per_block = cells_per_block
        self.block_norm = block_norm

    def fit(self, X, y=None):
        return self

    def local_hog(self, X):
        return hog(
            X,
            orientations=self.orientations,
            pixels_per_cell=self.pixels_per_cell,
            cells_per_block=self.cells_per_block,
            block_norm=self.block_norm
        )

    def transform(self, X, y=None):
        try:
            return np.array([self.local_hog(img) for img in X])
        except:
            return np.array([self.local_hog(img) for img in X])
