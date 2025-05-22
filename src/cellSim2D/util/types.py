
from typing import Union

import numpy as np
import numpy.typing as npt

# Custom Types
ComplexArray = Union[np.complexfloating, npt.NDArray[np.complexfloating]]
FloatArray = Union[np.floating, npt.NDArray[np.floating]]
IntArray = Union[np.integer, npt.NDArray[np.integer]]