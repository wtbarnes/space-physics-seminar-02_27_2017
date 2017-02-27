import os

import numpy as np
import astropy.units as u

import synthesizAR
from synthesizAR.instruments import InstrumentHinodeEIS,InstrumentSDOAIA

ar_root = '/data/datadrive2/ar_viz/seminar_poc/'

field = synthesizAR.Skeleton.restore(os.path.join(ar_root,'checkpoint'))

eis = InstrumentHinodeEIS([0,4990]*u.s)
aia = InstrumentSDOAIA([0,4990]*u.s,use_temperature_response_functions=False)

observer = synthesizAR.Observer(field,[eis,aia],ds=field._convert_angle_to_length(0.3*u.arcsec))

observer.build_detector_files(ar_root)

observer.bin_detector_counts(ar_root)