import pandas as pd
import numpy as np


chat_id = 723988166 # Ваш chat ID, не меняйте название переменной

from scipy.stats import anderson_ksamp
from hyppo.ksample import MMD
import pandas as pd

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    
    model = MMD(
        compute_kernel='laplacian'
    )
    _, p_value = model.test(x=x, 
               y=y, 
               random_state=26)
    return p_value < alpha # Ваш ответ, True или False
