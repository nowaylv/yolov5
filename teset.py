import numpy as np
import random
import torch
ai = torch.tensor([2.3,3.7])
g = 0.5
print(((ai % 1. < g) & (ai > 1.)).T),exit()

