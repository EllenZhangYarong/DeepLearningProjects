
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


hs_no_noise_test_score =  [[0.034058465317028455, 0.9903],
 [0.03484758692863115, 0.9907],
 [0.047855256396724964, 0.9902],
 [0.041164532752268404, 0.9921],
 [0.05266680776539063, 0.9889],
 [0.11739789315166929, 0.9898],
 [0.09764875334677674, 0.9886],
 [0.0632206972522277, 0.991],
 [0.09815478362253953, 0.9782],
 [0.08796581521126948, 0.9833],
 [0.07882386782268225, 0.9897],
 [0.09493261912277291, 0.9914],
 [0.06445855880243351, 0.9885],
 [0.10370552434645244, 0.9906],
 [0.1012516388016398, 0.9909],
 [0.10424824315333628, 0.9874],
 [0.12694154746300657, 0.9911],
 [0.11463687477970591, 0.9895],
 [0.11919253374170269, 0.9909],
 [0.1025763259003261, 0.9923]]


# In[3]:


hs_random_noise_test_score =   [[0.04829297218225449, 0.9902],
 [0.04320124557657609, 0.9904],
 [0.047471891228427966, 0.9893],
 [0.05874376216948381, 0.987],
 [0.053791355742009044, 0.987],
 [0.06325576037409922, 0.9882],
 [0.0867570142872686, 0.9824],
 [0.0826000678765977, 0.9897],
 [0.08580701754699838, 0.9896],
 [0.08968187244730577, 0.9859],
 [0.09480713811860275, 0.9912],
 [0.08384132597796659, 0.9907],
 [0.08962813374010209, 0.9913],
 [0.11838997870919354, 0.9886],
 [0.11488485456030291, 0.9888],
 [0.11201329010772249, 0.991],
 [0.09536086477248147, 0.9909],
 [0.1332961245259463, 0.9882],
 [0.13069431855936361, 0.9892],
 [0.10660658323409268, 0.9889]]


# In[4]:


hs_no_noise_test_score = np.asarray(hs_no_noise_test_score)
hs_random_noise_test_score= np.asarray(hs_random_noise_test_score)


# In[5]:


st_no = hs_no_noise_test_score[:,1].std()
print(st_no)
st_random = hs_random_noise_test_score[:,1].std() 
print(st_random)


# ### avarage accuracy ( no noise )

# In[6]:


av_no_noise_accuray = np.mean(hs_no_noise_test_score[:,1])
av_no_noise_accuray


# ### variance 

# In[7]:


var_no_noise = np.sum((hs_no_noise_test_score[:,1] - av_no_noise_accuray)**2) / 20
var_no_noise


# ### standard deviation

# In[8]:


st_no_noise = np.sqrt(var_no_noise)
st_no_noise


# ### avarage accuracy  (random noise -- 6000)

# In[9]:


av_random_noise_accuray = np.mean(hs_random_noise_test_score[:,1])
av_random_noise_accuray


# ### variance

# In[10]:


var_random_noise = sum((hs_random_noise_test_score[:,1] - av_random_noise_accuray)**2) / 20
var_random_noise


# ### standard deviation

# In[11]:


st_random_noise = np.sqrt(var_random_noise)
st_random_noise


# ### Loss

# In[12]:


av_no_noise_loss = np.mean(hs_no_noise_test_score[:,0])
av_no_noise_loss


# In[13]:


av_random_noise_loss = np.mean(hs_random_noise_test_score[:,0])
av_random_noise_loss


# In[14]:


X =np.arange(1,21,1)
X


# In[15]:


plt.plot(X, hs_no_noise_test_score[:,1], color='red', label="no noise")
plt.plot(X, hs_random_noise_test_score[:,1],color='blue', label="random noise")
plt.title("Compare score between no noise and random noise")
plt.xlabel("Training Times")
plt.ylabel("Accuracy")
plt.xlim(0,21)
plt.legend()
plt.show()


# In[16]:


plt.plot(X, hs_no_noise_test_score[:,0], color='red', label="no noise")
plt.plot(X, hs_random_noise_test_score[:,0],color='blue', label="random noise")
plt.title("Compare score between no noise and random noise")
plt.xlabel("Training Times")
plt.ylabel("Loss")
plt.xlim(0,21)
plt.legend()
plt.show()

