.. ros_gmapping_movebase documentation master file, created by
   sphinx-quickstart on Sat Mar 26 11:16:19 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ros_gmapping_movebase's documentation!
=================================================
.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
=============
This ROS package implements three behaviors for controlling a simulated mobile robot, which can provide us 
the map of the environment using gmapping and movebase rospackages.

Robot behaviors are these three options:

   #. Choosing a goal point and using the movebase node for path planning
   #. Using teleop twist keyboard rospackage
   #. Using teleop twist keyboard rospackage with obstacle avoidance

.. image:: preview.png
  :width: 800
  :align: center
  :alt: Alternative text

You can find more details about installation, running and source code of this rospackage in the corresponding sections of
this documentation.

Contents
==========
.. toctree::

   usage
   scripts
   
Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`