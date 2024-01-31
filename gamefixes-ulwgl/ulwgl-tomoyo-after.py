""" Game fix for Tomoyo After ~It's a Wonderful Life~
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Installs cjkfonts, d3dx9, dirac, dotnet35, dotnet40, lavfilters, vcrun2005, vcrun2008
    """

    util.protontricks('cjkfonts')
    util.protontricks('d3dx9')
    util.protontricks('dirac')
    util.protontricks('dotnet35')
    util.protontricks('dotnet40')
    util.protontricks('lavfilters')
    util.protontricks('vcrun2005')
    util.protontricks('vcrun2008')

    """ Prevents the window manager from decorating and controlling windows
    """

    util.protontricks('windowmanagerdecorated=n')
    util.protontricks('windowmanagermanaged=n')

    """ Sets Japanese locale and change time zone
    """

    util.set_environment('LC_ALL', 'ja_JP.UTF-8')
    util.set_environment('TZ', 'Asia/Tokyo')

    """ 
    """

    util.set_environment('LIBGL_ALWAYS_SOFTWARE', '1')
    util.set_environment('__GLX_VENDOR_LIBRARY_NAME', 'mesa')

    """ Disables NvAPI, DXVK, Esync, Fsync and protonaudioconverter
    """

    util.disable_nvapi()
    util.disable_dxvk()
    util.disable_esync()
    util.disable_fsync()
    util.disable_protonaudioconverter()
