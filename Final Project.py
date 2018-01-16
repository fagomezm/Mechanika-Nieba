# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:03:41 2018

@author: Fabian
"""
#Libraries and API needed for the calculations
from astropy import units as u
from astropy import time
from astropy.time import Time

from poliastro.bodies import Earth, Moon
from poliastro.twobody import Orbit
from poliastro.maneuver import Maneuver
from poliastro import iod

from poliastro.util import time_range
from astropy.coordinates import solar_system_ephemeris
solar_system_ephemeris.set("jpl")

from poliastro.frames import HeliocentricEclipticJ2000
from astropy.coordinates import (
    ICRS, GCRS,
    CartesianRepresentation, CartesianDifferential
)

from poliastro.patched_conics import compute_soi

from poliastro.plotting import OrbitPlotter3D
from poliastro.plotting import OrbitPlotter, plot
import matplotlib.pyplot as plt
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

#Times
date_liftoff=time.Time('1969-07-16 14:32', scale='tdb')
date_launch=date_liftoff + (2 * u.h + 44 * u.min)
#date_launch is the time at which Translunar Insertion Maneuver is performed
date_arrival=date_launch + (75 * u.h + 54 * u.min)
#date_arrival is the time at which Cislunar Insertion Maneuver is performed
tof=date_arrival - date_launch

#Apollo Parking Orbit Around Earth
apollo=Orbit.circular(Earth,alt=185.21 * u.km, inc=32.521 * u.deg, epoch=date_launch)

#Moon Orbit aqcuisition and conversion to GCRS
EPOCH=date_arrival
moon = Orbit.from_body_ephem(Moon, EPOCH)
moon_icrs = ICRS(
x=moon.r[0], y=moon.r[1], z=moon.r[2],
v_x=moon.v[0], v_y=moon.v[1], v_z=moon.v[2],
representation=CartesianRepresentation,
differential_cls=CartesianDifferential
)

moon_gcrs = moon_icrs.transform_to(GCRS(obstime=EPOCH))
moon_gcrs.representation = CartesianRepresentation
moon_gcrs

moon = Orbit.from_vectors(
Earth,
[moon_gcrs.x, moon_gcrs.y, moon_gcrs.z] * u.km,
[moon_gcrs.v_x, moon_gcrs.v_y, moon_gcrs.v_z] * (u.km / u.s),
epoch=EPOCH
)

ss0=apollo
ssf=moon

#Solve for Lambert's Problem (Determining Translunar Trajectory)
(v0, v), = iod.lambert(Earth.k, ss0.r, ssf.r, tof)
ss0_trans=Orbit.from_vectors(Earth,ss0.r,v0,date_launch)

dv=(ss0_trans.v-ss0.v)
dv=dv.to(u.m/u.s)
man = Maneuver.impulse(dv)
ss_f = ss0.apply_maneuver(man)
print("The required Delta-V to perform the Translunar Injection maneuver is: " + str(dv))

#Plotting Solution in 2D - Earth close-up
plt.ion()
op=OrbitPlotter()
op.plot(ss0, label="Apollo")
op.plot(ssf, label="Moon")
op.plot(ss0_trans, label="Transfer")
plt.xlim(-7000, 7000)
plt.ylim(-7000, 7000)
plt.gcf().autofmt_xdate()

#Plotting Solution in 2D - Moon close-up
plt.ion()
op=OrbitPlotter()
op.plot(ss0, label="Apollo")
op.plot(ssf, label="Moon")
op.plot(ss0_trans, label="Transfer")
plt.xlim(-394000, -392000)
plt.ylim(24000, 26000)
plt.gcf().autofmt_xdate()

#Plotting Solution in 2D
plt.ion()
op=OrbitPlotter()
op.plot(ss0, label="Apollo")
op.plot(ssf, label="Moon")
op.plot(ss0_trans, label="Transfer")
plt.gcf().autofmt_xdate()

#Plotting Solution in 3D
N=50
times_vector = time_range(date_launch, end=date_arrival, periods=N)

frame = OrbitPlotter3D()

frame.set_attractor(Earth)

frame.plot_trajectory(ss0.sample(times_vector), label="Apollo")
frame.plot_trajectory(ssf.sample(times_vector), label="Moon")
frame.plot_trajectory(ss0_trans.sample(times_vector), label="Trajectory")

frame.plot(moon, label="Moon")

frame.set_view(30 * u.deg, 260 * u.deg, distance=3 * u.km)
frame.show(title="Apollo Mission: Trans-Lunar Trajectory")
