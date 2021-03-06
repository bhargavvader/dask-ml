from sklearn.linear_model import Perceptron as _Perceptron

from dask_ml.base import _BigPartialFitMixin, _copy_partial_doc


@_copy_partial_doc
class PartialPerceptron(_BigPartialFitMixin, _Perceptron):
    _init_kwargs = ['classes']
    _fit_kwargs = ['classes']
