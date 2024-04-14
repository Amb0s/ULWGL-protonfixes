""" Game fix for Cosmos no Sora ni
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Installs cjkfonts
    """

    util.protontricks('cjkfonts')

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


