""" Game fix for The House in Fata Morgana
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
    
    """ Sets virtual desktop
    """

    screen_width,screen_height = util.get_resolution()
    screen_resolution = str(screen_width) + 'x' + str(screen_height)  
    util.protontricks('vd=' + screen_resolution)

    """ Disables NvAPI, DXVK, Esync, Fsync and protonaudioconverter
    """

    util.disable_nvapi()
    util.disable_dxvk()
    util.disable_esync()
    util.disable_fsync()
    util.disable_protonaudioconverter()

