""" Game fix for Bible Black - The Game
"""
#pylint: disable=C0103from

from protonfixes import utildef

def main():
    """ Installs directmusic, gmdls                                                                                                                                                                         
    """

    util.protontricks('directmusic')
    util.protontricks('gmdls')

    # Optional: install `timidity` and a soundfont to enable in-game MIDI support.

    """ Prevent the window manager from decorating and controlling windows
    """

    util.protontricks('windowmanagerdecorated=n')
    util.protontricks('windowmanagermanaged=n')

    """ Disables NvAPI, DXVK, Esync, Fsync and disable_protonaudioconverter
    """

    util.disable_nvapi()
    util.disable_dxvk()
    util.disable_esync()
    util.disable_fsync()
    util.disable_protonaudioconverter()
