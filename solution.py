import pandas as pd
import numpy as np


chat_id = 723988166 # Ваш chat ID, не меняйте название переменной

from scipy.stats import anderson_ksamp
from hyppo.ksample import MMD
from scipy.stats import cramervonmises_2samp

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    
    p_value = cramervonmises_2samp(x=x, y=y, method='exact').pvalue
    return p_value < alpha # Ваш ответ, True или False
