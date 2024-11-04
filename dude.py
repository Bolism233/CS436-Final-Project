import torch
import numpy
import pandas
import statsmodels
import sklearn
import einops
import sympy
import numba
from platform import python_version  # Import python_version

print("Python version:", python_version())
print("Torch version:", torch.__version__)
print("Numpy version:", numpy.__version__)
print("Pandas version:", pandas.__version__)
print("Statsmodels version:", statsmodels.__version__)
print("Scikit-learn version:", sklearn.__version__)
print("Einops version:", einops.__version__)
print("Sympy version:", sympy.__version__)
print("Numba version:", numba.__version__)

import torch

if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("No GPU available.")
