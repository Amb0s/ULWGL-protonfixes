""" Game fix for Baldr Force Standard Edition
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Installs cjkfonts, d3dx9, d3dcompiler_43, d3dcompiler_47, lavfilters, quartz_feb2010
    """

    util.protontricks('cjkfonts')
    util.protontricks('d3dx9')
    util.protontricks('d3dcompiler_43')
    util.protontricks('d3dcompiler_47')
    util.protontricks('lavfilters')
    util.protontricks('quartz_feb2010')
    
    """ Sets the necessary dll override for the english patch
    """
    
    util.winedll_override('wined3d', 'n,b')

    """ Prevents the window manager from decorating and controlling windows
    """

    util.protontricks('windowmanagerdecorated=n')
    util.protontricks('windowmanagermanaged=n')

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


