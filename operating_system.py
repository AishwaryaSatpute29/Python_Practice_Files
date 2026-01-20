#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[5]:


os.getcwd()


# In[4]:


# To rename/move files
os.rename("source_file_path","destination_file_path")

# To check file exists or not
os.path.exists("file_path")

# To remove file
os.remove("file_path")

# To create folder
os.mkdir("folder_path")
         
# To create multiple folders
os.makedirs("folder_path")      

# To delete directory
os.rmdir("folder_path")

# To delete non empty directory or non empty folder
import shutil
shutil.rmtree("folder path")

# To check current working directory
os.getcwd()

# Join two path
os.path.join("folder_path1","folder_path2")

# list all directory
os.listdir()

# copy files from one directory to other
shutil.copy("source_file_path","destination_file_path")


# In[7]:


# To rename file

os.rename("machine_learning.txt","ml.txt")


# In[16]:


# To move file from one source to other destination

source1 = r"C:\Users\HP ECS\OS\data1.txt"
source2 = r"C:\Users\HP ECS\OS\data2.txt"
des1 = r"C:\Users\HP ECS\OS\images\data1.txt"
des2 = r"C:\Users\HP ECS\OS\images\data2.txt"

os.rename(source1,des1)
os.rename(source2,des2)


# In[24]:


if os.path.exists("C:\\Users\\HP ECS\\OS\\images\\linear_regression.txt"):
    print("file is present")
else:
    print("file not found")


# In[25]:


# To remove file

os.remove("C:\\Users\\HP ECS\\OS\\images\\linear_regression.txt")


# In[27]:


# Create folder

os.mkdir(r"C:\Users\HP ECS\OS\cv\vehicles")


# In[28]:


os.mkdir(r"C:\Users\HP ECS\OS\cv\pv\vehicles")


# In[30]:


# create multiple folders

os.makedirs(r"C:\Users\HP ECS\OS\cv\vehicles\img1\img2\img3")


# In[33]:


os.makedirs(r"C:\Users\HP ECS\OS\cv\pv\vehicles\img1\img2\img3")


# In[42]:


# Delete directory

os.rmdir(r"C:\Users\HP ECS\OS\cv\vehicles\img1\img2\img3")


# In[43]:


os.rmdir(r"C:\Users\HP ECS\OS\cv\vehicles\img1\img2")


# In[44]:


os.rmdir(r"C:\Users\HP ECS\OS\cv\vehicles\img1")


# In[47]:


# Delete non empty Directory

import shutil
if os.path.exists(r"C:\Users\HP ECS\OS\cv\vehicles"):
    shutil.rmtree(r"C:\Users\HP ECS\OS\cv\vehicles")
    print("Folder deleted")
else:
    print("folder not found")


# In[49]:


# Join two paths

os.path.join(r"C:\Users\HP ECS\OS\cv",r"C:\Users\HP ECS\OS\pv")


# In[50]:


# list of all directory

os.listdir()


# In[51]:


# copy files from one directory to other

shutil.copy(r"C:\Users\HP ECS\OS\pv\bike.txt",r"C:\Users\HP ECS\OS\pv\vehicles\img1\img2\img3")


# In[ ]:




