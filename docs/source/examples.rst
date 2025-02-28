Examples
==========

This describes the validation and example datasets, along with sample ``mesher`` inputs.

A zip containing all the example code and data can be found `here <https://github.com/Chrismarsh/mesher/raw/master/examples.zip>`_. 

flat
----

Flat DEM, produces 2 triangles

|image0|

.. literalinclude:: ../../examples/flat/flat.py

flat_veg
--------

Uses the EOSD dataset to mesh with a ``mode=0.9`` threshold. This
captures most of the vegetation patches. ALthough it result in an
over-generation of triangles between patches, this is due to producing a
good gradation from small to larger triangles.

|image1|

.. literalinclude:: ../../examples/flat_veg/flat_veg.py

gaussian_hill
-------------

Using the generated gaussian hill dataset, produces a mesh for a
guassian hill.

|image2|

.. literalinclude:: ../../examples/gaussian_hill/gaussian_hill.py


ideal_ridge
-----------

An idealized ridge line

|image3|

.. literalinclude:: ../../examples/ideal_ridge/ideal_ridge.py

ideal_ridge_low_tol
-------------------

Same as the ideal_ridge, but with a tighter tolerance. Produces more
triangles along the rige to better capture it.

|image4|

.. literalinclude:: ../../examples/ideal_ridge_low_tol/ideal_ridge_low_tol.py

uniform
-------

Produces a uniform mesh with area = 100 m x 100 m.

|image5|

.. literalinclude:: ../../examples/uniform/uniform.py

lloyd
-----

Demonstrates the impact of 100 `lloyd
optimization <https://doc.cgal.org/latest/Mesh_2/index.html#secMesh_2_optimization>`__
iterations on the above uniform domain. Compare to the uniform case

|image6|

.. literalinclude:: ../../examples/lloyd/lloyd.py

flat_stream
-----------

The flat DEM has been constrained to a stream network input as a shape
file. This shows the greater number of triangles near the stream.
Simplified stream networks produce fewer triangles along the river
constraint.

|image7|

.. literalinclude:: ../../examples/flat_stream/flat_stream.py

stream_dem
----------

Same as above, but including the the Granger subset DEM. |image8|

.. literalinclude:: ../../examples/stream_dem/stream_dem.py

granger
-------

The Granger subset is used, deriving a mesh from only the elevation map. 

|image9|

.. literalinclude:: ../../examples/granger/granger.py


granger_low_veg_weight
----------------------

The granger subset is used with a low elevation tolerance plus low
weights on the vegetation map, showing mesher mostly ignoring the
vegetation constraints.

|image10|

.. literalinclude:: ../../examples/granger_low_veg_weight/granger_low_veg_weight.py

granger_high_veg_weight
-----------------------

Same as above but with high weight on the vegetation map, showing the
algorithm refining triangles to capture the vegetation patches.

|image11|

.. literalinclude:: ../../examples/granger_high_veg_weight/granger_high_veg_weight.py

flow_accumulation
-----------------

This domain shows large-extent meshing with a mountain domain for the
Bow Valley region near Canmore, Alberta, Canada. This mesh uses a
DEM-derived flow accumulation via
`RichDEM <https://richdem.readthedocs.io/en/latest/flow_metrics.html#d-tarboton-1997>`__
to ensure the mesh captures the high-accumulation locations. The flow
accumulation input is generated with the ``flow.py`` script in ``data``
folder. This requires the RichDEM Python package `to be
installed <https://richdem.readthedocs.io/en/latest/using_it.html>`__.

|image12|

.. literalinclude:: ../../examples/flow_accumulation/flow_accumulation.py



flow_accumulation_granger
-------------------------

Flow accumulation for the smaller Granger subbasin.

|image16|

.. literalinclude:: ../../examples/flow_accumulation_granger/flow_accumulation_granger.py

dem_smoothing
-------------

A small subset of the above Bow Valley domain is extracted to show the
impact of smoothing on the output mesh. If the ``min_area`` is
approximately equal to the cell size of the raster and tolerance
parameter ensures triangles of this size are being produced, then in
complex terrain the stair stepping of the raster (due to non-continous
first derivative; i.e., slope) impacts the mesh quality as shown below.

|image13|

mesher has an option to smooth the input DEM to lessen this impact. This
is enabled via

::

   do_smoothing = True
   max_smooth_iter = 1
   smoothing_scaling_factor = 1

Each iteration the smoothing magnitude increases by
``iteration * smoothing_scaling_factor``. This is the result of 1
smoothing iteration. |image14|

Subsequent iterations, or increases in ``smoothing_scaling_factor`` can
reduce the stair-stepping further at the cost of increased smoothing of
complex terrain.

::

   do_smoothing = True
   max_smooth_iter = 2
   smoothing_scaling_factor = 1

|image15|

.. literalinclude:: ../../examples/dem_smoothing/dem_smoothing.py

.. |image0| image:: example-images/flat.png
.. |image1| image:: example-images/flat_veg.png
.. |image2| image:: example-images/gaussian_hill.png
.. |image3| image:: example-images/ideal_ridge.png
.. |image4| image:: example-images/ideal_ridge_low_tol.png
.. |image5| image:: example-images/uniform.png
.. |image6| image:: example-images/lloyd.png
.. |image7| image:: example-images/flat_stream.png
.. |image8| image:: example-images/stream_dem.png
.. |image9| image:: example-images/granger.png
.. |image10| image:: example-images/granger_low_veg_weight.png
.. |image11| image:: example-images/granger_high_veg_weight.png
.. |image12| image:: example-images/flow_accumulation.png
.. |image13| image:: example-images/dem_no_smoothing.png
.. |image14| image:: example-images/dem_smoothing_1.png
.. |image15| image:: example-images/dem_smoothing_2.png
.. |image16| image:: example-images/flow_accumulation_granger.png
