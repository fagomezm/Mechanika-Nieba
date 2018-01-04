# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:27:21 2017

@author: Fabian
"""

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun
from poliastro.twobody import Orbit

plt.style.use("seaborn")

r=[-6045,-3490,2500] * u.km
v=[-3.457,6.618,2.533] * u.km / u.s

ss=Orbit.from_vectors(Earth, r, v)

from poliastro.plotting import plot
#plot(ss)

a=1.523679 * u.AU
ecc=0.093315 * u.one
inc=1.85 *u.deg
raan=49.562 * u.deg
argp=286.537 * u.deg
nu=23.33 * u.deg

ss=Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

ss.state.period.to(u.day)
ss.state.v

#plot (ss)

from poliastro.examples import iss
iss

#plot (iss)
iss.epoch
iss.nu.to(u.deg)
iss.n.to(u.deg / u.min)

iss_30m =iss.propagate(30 * u.min)
iss_30m.epoch

iss_30m.nu.to(u.deg)
#plot (iss_30m)

earth=Orbit.from_body_ephem(Earth)

#plot(earth)
earth_30d=earth.propagate(30 * u.day)
#plot(earth_30d)

from poliastro.maneuver import Maneuver
dv=[5, 0, 0] * u.m / u.s
man=Maneuver.impulse(dv)
man=Maneuver((0 * u.s, dv))

ss_i=Orbit.circular(Earth, alt=700* u.km)
ss_i
#plot(ss_i)
hoh=Maneuver.hohmann(ss_i,36000 * u.km)
hoh.get_total_cost()
hoh.get_total_time()
print (hoh.get_total_cost())
print (hoh.get_total_time())

hoh.impulses[0]
hoh[0]
tuple(val.decompose([u.km, u.s]) for val in hoh[1])

ss_f=ss_i.apply_maneuver(hoh)
#plot(ss_f)

from poliastro.plotting import OrbitPlotter

op = OrbitPlotter()
ss_a, ss_f = ss_i.apply_maneuver(hoh, intermediate=True)
#op.plot(ss_i, label="Initial orbit")
#op.plot(ss_a, label="Transfer orbit")
#op.plot(ss_f, label="Final orbit")

from astropy import time
epoch=time.Time("2015-05-09 10:43")

Orbit.from_body_ephem(Earth, epoch)

from astropy.coordinates import solar_system_ephemeris
solar_system_ephemeris.set("jpl")

date_launch=time.Time('2011-11-26 15:02', scale='utc')
date_arrival=time.Time('2012-08-06 05:17', scale='utc')
tof=date_arrival - date_launch
ss0=Orbit.from_body_ephem(Earth, date_launch)
ssf=Orbit.from_body_ephem(Mars, date_arrival)
from poliastro import iod
(v0, v), = iod.lambert(Sun.k, ss0.r, ssf.r, tof)

#op.plot(ss0)
#op.plot(ssf)