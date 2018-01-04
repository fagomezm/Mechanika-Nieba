# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:26:10 2017

@author: Fabian
"""
#Necessary modules
import numpy as np

import astropy.units as u
from astropy import time

from poliastro import iod
from poliastro.bodies import Sun
from poliastro.twobody import Orbit

from poliastro.util import time_range

from astropy.coordinates import solar_system_ephemeris, get_body_barycentric_posvel
solar_system_ephemeris.set("jpl")

# Initial data
N = 50

date_launch = time.Time('2011-11-26 15:02', scale='utc')
date_arrival = time.Time('2012-08-06 05:17', scale='utc')
tof = (date_arrival - date_launch)

tof.to(u.h)

#Array of positions of Earth and Mars
times_vector = time_range(date_launch, end=date_arrival, periods=N)
times_vector[:5]

rr_earth, vv_earth = get_body_barycentric_posvel("earth", times_vector)
rr_earth[:3]
vv_earth[:3]

rr_mars, vv_mars = get_body_barycentric_posvel("mars", times_vector)
rr_mars[:3]
vv_mars[:3]

# Compute the transfer orbit!
r0 = rr_earth[0].xyz
rf = rr_mars[-1].xyz

(va, vb), = iod.lambert(Sun.k, r0, rf, tof)

ss0_trans = Orbit.from_vectors(Sun, r0, va, date_launch)
ssf_trans = Orbit.from_vectors(Sun, rf, vb, date_arrival)

#Plot
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

from poliastro.plotting import OrbitPlotter3D
from poliastro.bodies import Earth, Mars

#Visual setting of the graph
color_earth0 = '#3d4cd5'
color_earthf = '#525fd5'
color_mars0 = '#ec3941'
color_marsf = '#ec1f28'
color_sun = '#ffcc00'
color_orbit = '#888888'
color_trans = '#444444'

frame = OrbitPlotter3D()

frame.set_attractor(Sun)

frame.plot_trajectory(rr_earth, label=Earth)
frame.plot_trajectory(rr_mars, label=Mars, color=color_marsf)

frame.plot_trajectory(ss0_trans.sample(times_vector), label="MSL trajectory", color=color_trans)

frame.set_view(30 * u.deg, 260 * u.deg, distance=3 * u.km)
frame.show(title="MSL Mission: from Earth to Mars")

