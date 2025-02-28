
#Example configuration file using the sample data

dem_filename = '../data/dem.tif'

max_area= 990999999  #Effectively unlimited upper area -- allow tolerance check to refine it further
max_tolerance = 1    #1m maxe RMSE between triangle and underlying elevation set to -1 to skip tolerance checks
min_area = 25**2     #triangle area below which we will no longer refine, regardless of max_tolerance


#paramter files to apply to the resulting mesh
#tolerance = 0.5 ensures that each triangle has at least 50% of 1 vegetation classification from the underlying raster
parameter_files = {
    'landcover': {'file': '../data/veg.tif',
                  'method': 'mode',
                  'tolerance':.5}
   
}


#Simplify the outter boundary allowing at most simplify_tol difference between boundary and simplified boundary
simplify=True
simplify_tol=10


