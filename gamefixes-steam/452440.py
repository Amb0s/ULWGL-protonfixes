""" Game fix for Flowers -Le volume sur printemps- 
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Installs d3dx9, dirac, lavfilters, vcrun2005, vcrun2008
    """

    util.protontricks('d3dx9')
    util.protontricks('dirac')
    util.protontricks('lavfilters')
    util.protontricks('vcrun2005')
    util.protontricks('vcrun2008')

    """ Disables NvAPI, DXVK, Esync, Fsync and protonaudioconverter
    """

    util.disable_nvapi()
    util.disable_dxvk()
    util.disable_esync()
    util.disable_fsync()
    util.disable_protonaudioconverter()
