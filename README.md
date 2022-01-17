# HDM

This is the repository for the Holographic Declarative Memory (HDM) module for Python ACT-R.

This repository contains:
- documentation: a paper, conference poster, and slides that describe the theory and applications of HDM
- example models: sample ACT-R models that use HDM
- hdm.py the HDM module itself, which uses HRRs
- hrr.py code for Holographic Reduced Representations (HRRs)

External links:
- The paper on HDM can be found here: https://doi.org/10.1111/cogs.12904
- A talk that discusses HDM and the model's future can be found here: https://www.youtube.com/watch?v=BtnUvpQg6bI
- Tutorials on how to use Python ACT-R can be found here: https://sites.google.com/site/pythonactr/home

To install HDM for use on your own computer:


1. pip install python_actr_hdm

2. Create a Python ACT-R model (see Python ACT-R tutorials).

3. Instead of creating an instance of DM, create an instance of HDM in your model (see example code in this repository).

USING HDM

To use HDM:

   from python_actr import *
   from python_actr_hdm import *

 ...

   retrieval=Buffer()

   memory=HDM(retrieval)

The HDM module provides six methods for use by an ACT-R model:

1. The constructor, which takes a retrieval buffer and creates an HDM:
memory = HDM(retrieval)

2. Add a chunk, which takes a chunk and adds it to HDM:
memory.add(chunk)

3. Request a chunk, which takes a chunk and finds the best match in HDM:
memory.request(chunk)

4. Get activation, which takes a chunk and returns the chunk's activation as a cosine in HDM:
memory.get_activation(chunk)

5. Get and 6. set methods for defining compositional relationships between the environmental stimuli represented as environment vectors:
e.g., we can define the stimulus 'customer1' as a conjunction of the features 'a white person with long, blonde hair and moustache'
DM.set('customer1', DM.get('moustache') + DM.get('blond') + DM.get('long_hair') + DM.get('white'))

PARAMETERS OF HDM SHARED WITH DM

1. **buffer**
2. **latency**
3. **threshold**
As in DM, threshold is the minimum activation threshold for a chunk to be retrieved. We recommend using lower thresholds for HDM than is standard for DM. The default threshold for DM is 0. The default threshold for HDM is -4.6. 
Internally, HDM uses cosines, which approximate the square root of the probability. Conversely DM uses log odds as activation. For compatibility with DM, the threshold parameter is in logodds. It is immediately converted to a cosine for internal use by HDM.
The default threshold of -4.6 is converted to a cosine of 0.1.

4. **maximum_time**
5. **finst_size**
6. **finst_time**

NEW PARAMETERS UNIQUE TO HDM

1. **N** is the vector dimensionality. Defaults to 512 dimensions, which is plenty. We recommend setting N to values in the range from 32 to 2048. Smaller dimensions introduce more noise and error into the model. 32 dimensions will introduce a high amount of noise/error for small study sets. 2048 dimensions allows for good recall for millions of items. 
2. **verbose** defaults to false. When set to true, HDM reports its internal computations, allowing the user to understand what HDM is doing.
3. **forgetting** controls the forgetting rate due to retroactive inhibition
range [0 to 1]
1 = no forgetting
0 = no remembering
When updating memory:
memory vector =  forgetting * memory vector + new information vector

4. **noise** controls the amount of noise added to memory per time step. Gaussian noise is added to all memory vectors whenever Request or Add is called.
When adding noise:
memory vector = memory vector + noise * time since last update * noise vector
Noise ranges from [0 ... ], where 0 is no noise and more is more noise
