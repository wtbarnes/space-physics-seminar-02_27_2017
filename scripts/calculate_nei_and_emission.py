import os

import astropy.units as u

import synthesizAR
from synthesizAR.model_ext import EbtelInterface
from synthesizAR.atomic import EmissionModel
from synthesizAR.instruments import InstrumentSDOAIA

ar_root = '/data/datadrive2/ar_viz/seminar_poc'

#restore field and emission model
field = synthesizAR.Skeleton.restore(os.path.join(ar_root,'checkpoint'))
emiss_model = EmissionModel.restore(os.path.join(ar_root,'checkpoint_emiss_model'))

#create dummy ebtel interface for calculating NEI populations
class DummyHeatingModel(object):
    def __init__(self):
        self.base_config = {}
ebtel_plug = EbtelInterface({},DummyHeatingModel(),'','')

#Finally, calculate NEI
field.calculate_fractional_ionization(emiss_model,ebtel_plug,
                                        savefile=os.path.join(ar_root,'nei_populations.h5'))

#And then calculate the emission for each loop
aia = InstrumentSDOAIA([0,4990]*u.s,use_temperature_response_functions=False)
field.calculate_emission(emiss_model,savefile=os.path.join(ar_root,'loop_emiss.h5'),
                            imagers=[aia])
