""" Game fix for Sharin no Kuni, Himawari no Shoujo
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ installs cjkfonts, d3dx9, dirac, dotnet35, dotnet40, lavfilters, vcrun2005, vcrun2008
    """

    util.protontricks('cjkfonts')
    util.protontricks('d3dx9')
    util.protontricks('dirac')
    util.protontricks('dotnet35')
    util.protontricks('dotnet40')
    util.protontricks('lavfilters')
    util.protontricks('vcrun2005')
    util.protontricks('vcrun2008')
    util.regedit_add('HKEY_CURRENT_USER\Software\Wine\X11 Driver', 'Decorated', 'REG_SZ', 'N') # use 'windowmanagerdecorated=n' instead?
    util.regedit_add('HKEY_CURRENT_USER\Software\Wine\X11 Driver', 'Managed', 'REG_SZ', 'N') # use 'windowmanagerdecorated=n' instead? 
    util.regedit_add('HKEY_CURRENT_USER\Software\Wine\Direct3D', 'renderer', 'REG_SZ', 'gdi') # use 'winetricks renderer=gdi' instead?
    util.set_environment('LC_ALL', 'ja_JP.UTF-8')
    util.set_environment('TZ', 'Asia/Tokyo')
    util.disable_nvapi()
    util.disable_dxvk()
    util.disable_esync()
    util.disable_fsync()
    util.disable_protonaudioconverter()
