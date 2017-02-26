import os

import astropy.units as u

import synthesizAR
from synthesizAR.instruments import InstrumentSDOAIA,InstrumentHinodeEIS

ar_root = '/data/datadrive2/ar_viz/seminar_poc'

#restore field
field = synthesizAR.Skeleton.restore(os.path.join(ar_root,'checkpoint'))

#create instruments
aia = InstrumentSDOAIA([0.,4990.]*u.s,use_temperature_response_functions=False)
eis = InstrumentHinodeEIS([0.,4990.]*u.s)

#create observer
observer = synthesizAR.Observer(field,[aia,eis],
                                ds=field._convert_angle_to_length(0.3*u.arcsec))
#build files
observer.build_detector_files(ar_root)
#flatten the counts
observer.flatten_detector_counts()
