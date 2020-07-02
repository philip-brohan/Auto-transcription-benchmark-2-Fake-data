Scripts to make the images and data
===================================

These scripts need to know where to put their output files. They rely on an environment variable ``SCRATCH`` - set this variable to a directory with plenty of free disc space.

These scripts will only work in a `python <https://www.python.org/>`_ environment with the appropriate python version and libraries available. 

One python script makes a pair of outputs: an image (.png) and a data array (`pickled <https://docs.python.org/3/library/pickle.html>`_ as a .pkl).

.. literalinclude:: ../make_data/make_image_data_pair.py

We're going to want thousands of examples to train and test transcription methods on, so it's good to have a script that will make batches of such image::data pairs.

.. literalinclude:: ../make_data/make_set_of_images.py
