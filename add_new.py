#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Train
import getFaces
getFaces.getFaces(training=True)
T = Train.Training()
T.train()

