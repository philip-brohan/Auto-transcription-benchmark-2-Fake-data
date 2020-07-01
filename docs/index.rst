Auto-transcription benchmark 2: Fake data
=========================================

This is a benchmark dataset for document transcription tools. 

Document transcription is hard - the images to be transcribed are often poor-quality; document fonts, formats, colours, and other details vary even within one set of documents; and we often have very limited (and inaccurate) transcribed samples to use in development and validation of transcription software. For writing and testing transcription software it would be nice to have an ideal set of test document images - perfectly crisp and consistent, and accompanied by transcribed data with no errors.

No such ideal documents exist, but we can fake it - this dataset includes no images and no transcribed results. Instead there are scripts to make fake image::transcription pairs, so we can make an ideal dataset of any size.

The objective is to facilitate development and testing of automated tools for document transcription. Any such tools can be run on the generated images, and their results validated by comparison to the associated transcriptions. It should be easier to produce successful transcription tools for this dataset than for any real set of documents - so it's a good way to get started.

.. toctree::
   :maxdepth: 1

   Getting started <preface>
   Fake images and data <examples>
   Scripts to make the dataset <scripts>
   
.. toctree::
   :maxdepth: 1

   Authors and acknowledgements <credits>

This dataset is distributed under the terms of the `Open Government Licence <https://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/>`_. Source code included is distributed under the terms of the `BSD licence <https://opensource.org/licenses/BSD-2-Clause>`_.

