import pandas as pd
import numpy as np
from scipy.stats import kstest

chat_id = 252623629

def solution(x: np.array, y: np.array) -> bool:
  p_value = kstest(x, y)[0.1]
  return p_value < 0.05
