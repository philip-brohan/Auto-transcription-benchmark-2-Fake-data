Getting started
===============

This dataset is kept under version control in a `git repository <https://en.wikipedia.org/wiki/Git>`_. The repository is hosted on `GitHub <https://github.com/>`_ (and the documentation made with `GitHub Pages <https://pages.github.com/>`_). The repository is `<https://github.com/philip-brohan/Auto-transcription-benchmark-2-Fake-data>`_.

If you are familiar with GitHub, you already know what to do (fork or clone `the repository <https://github.com/philip-brohan/Auto-transcription-benchmark-2-Fake-data>`_): If you'd prefer not to bother with that, you can download the whole thing as `a zip file <https://github.com/philip-brohan/Auto-transcription-benchmark-2-Fake-data/archive/master.zip>`_.

As well as downloading the scripts, some setup is necessary to run them successfully:

These scripts need to know where to put their output files. They rely on an environment variable ``SCRATCH`` - set this variable to a directory with plenty of free disc space.

These scripts will only work in a `python <https://www.python.org/>`_ environment with the appropriate python version and libraries available. I use `conda <https://docs.conda.io/en/latest/>`_ to manage the required python environment - which is specified in a yaml file:

.. literalinclude:: ../environments/atb2.yml

Install `anaconda or miniconda <https://docs.conda.io/en/latest/>`_, `create and activate the environment in that yaml file <https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-envs>`_, and all the scripts in this repository should run successfully.


