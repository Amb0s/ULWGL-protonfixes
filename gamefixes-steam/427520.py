""" Game fix for Factorio
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Installs d3dcompiler_47
    """

    util.protontricks('d3dcompiler_47')

    """ Disables NvAPI, DXVK, Esync, Fsync and protonaudioconverter
    """

    util.disable_nvapi()
    util.disable_dxvk()
    util.disable_esync()
    util.disable_fsync()
    util.disable_protonaudioconverter()
