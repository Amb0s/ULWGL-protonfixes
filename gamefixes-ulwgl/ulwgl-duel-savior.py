""" Game fix for Duel Savior
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Installs cjkfonts, d3dx9, d3dcompiler_43, d3dcompiler_47, lavfilters, quartz
    """

    util.protontricks('cjkfonts')
    util.protontricks('d3dx9')
    util.protontricks('d3dcompiler_43')
    util.protontricks('d3dcompiler_47')
    util.protontricks('lavfilters')
    util.protontricks('quartz')

    """ Sets Japanese locale and change time zone
    """

    util.set_environment('LC_ALL', 'ja_JP.UTF-8')
    util.set_environment('TZ', 'Asia/Tokyo')
    
    """ Disables NvAPI, DXVK, Esync, Fsync and protonaudioconverter
    """

    util.disable_nvapi()
    util.disable_dxvk()
    util.disable_esync()
    util.disable_fsync()
    util.disable_protonaudioconverter()



