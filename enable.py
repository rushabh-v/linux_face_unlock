#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
print("Enter 'y' id you want to add your face now else press 'n':")
s = input()
if s=='y':
    os.system("python ./add_new.py")
    print("Enter 'y' id you want to enable the face unlock now else press 'n'")
    s = input()
    if s=='y':
        os.system("pam-auth-update")
    else:
        pass
else:
    pass
    


# In[ ]:




