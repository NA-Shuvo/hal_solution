#!/usr/bin/env python
# coding: utf-8

# In[1]:


from solution import CompositionMatrix as CM
import numpy as np


# ## Two example matrices

# In[2]:


A = [[1, 0, 0, -3, 0, 0], 
     [0, 4, 0, 0, 7, 0],
     [0, 0, 5, 0, 0, 9],
     [2, 0, 0, -17, 0, 0],
     [0, 7, 0, 0, 9, 0],
     [0, 0, 13, 0, 0, -5]]
B = [[2, 0, 0, -1, 0, 0], 
     [0, 1, 0, 0, -5, 0],
     [0, 0, 1, 0, 0, -17],
     [-2, 0, 0, 1, 0, 0],
     [0, -9, 0, 0, 9, 0],
     [0, 0, -11, 0, 0, 15]]


# ## Their associated representative matrices
# Definitions of representative matrices of a matrix is given in the write-up document.

# In[3]:


a = [[[1, -3], 
      [2, - 17]],
     [[4, 7],
      [7, 9]],
     [[5, 9],
      [13, -5]]]

b = [[[2, -1], 
      [-2, 1]],
     [[1, -5],
      [-9, 9]],
     [[1, -17],
      [-11, 15]]]


# ## Elementary Operations
# 

# In[4]:


CA = CM(a) ## Composition matrix for A
CB = CM(b) ## Composition matrix for B


# ### A+B with CA + CB

# In[5]:


Csum = CA + CB
print("Representation matrices of Csum:\n", np.array(Csum.r))


# #### Checking with the full view

# In[6]:


print(np.array(Csum.transform()))


# ### A*B with CA * CB

# In[7]:


Cdot = CA * CB
print("Representation matrices of Cdot:\n", np.array(Cdot.r))


# #### Checking with the full view

# In[8]:


print(np.array(Cdot.transform()))


# ### Inverse of A
# Note that the ~ operator is overloaded as if ~A = inverse(A)

# In[9]:


Ainv =  ~CA
print("Representation matrices of Ainv:\n", np.array(Ainv.r))


# #### Checking with the full view

# In[10]:


print(np.array(Ainv.transform()))

