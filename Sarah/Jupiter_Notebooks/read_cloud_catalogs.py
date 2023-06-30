import matplotlib as plt2 #need this for patches for shaded circles
import numpy as np
import matplotlib.pyplot as plt
import gizmo_analysis as gizmo 
import utilities as ut
import matplotlib.colors as colors
from matplotlib import rc #to use Latex math symbols like 'phi'
import astropy
from astropy.io import ascii
import matplotlib
import pdb
from importlib import reload
from sl_utilities import distance_functions
#pdb.set_trace()  #<--in case need to troubleshoot
import pickle

#this is just for m12i!  need to change name for m12m cloud catalog and input data for fof

dirname_gmc = '/path/to/gmc_cloud_catalog' #change this! 
filename_gmc = 'cloud_props_m12i_mhd_stamp_fire2650.txt'


#load gmc catalog data
data_gmc  = astropy.io.ascii.read(dirname_gmc+filename_gmc) #data_gmc.keys() #to see content
#gind = np.where(data_gmc['mass'] > 1e6)  #leave this commented for now

gxcm  = data_gmc['xcm']
gycm  = data_gmc['ycm']
gzcm  = data_gmc['zcm']
gmtot = data_gmc['mass']
gr90  = data_gmc['r_90']
gn = len(gxcm)

#load particle data here as you normally do to get the star information
#cut on Rxy, |z| and age

#run fof
#sind, sxcm, sycm, szcm, smtot, sgrpid, sr90, sr50, srmax =fof.find(x[si],y[si],z[si], b=b_kpc, mass=mass[si], ncut=ncut_min)
#srcm = np.sqrt(sxcm**2. + sycm**2.)

sn = len(sxcm)

bool_arr = distance_functions.array_embedded_check(sxcm, sycm, szcm, srmax, gxcm, gycm, gzcm, gr90)  #this is just a little function that i wrote (but didn't check) to see if the cluster is inside the radius of gmc.  it will need to be visualized to confirm this

#modify this loop as needed
for i in range(sn):
    if (srcm[i] >= 6) and (srcm[i] <= 7) and (bool_arr[i] == True):
        #print(srcm[i], bool_arr[i], smtot[i], scount[i])

        gind, drmin = distance_functions.closest_cluster_index(sxcm[i], sycm[i], szcm[i], gxcm, gycm, gzcm)
        print(i,sxcm[i], sycm[i], gxcm[gind][0], gycm[gind][0])
#i = 11; gind = 44
        print(gind[0], cloud_number[gind][0])
