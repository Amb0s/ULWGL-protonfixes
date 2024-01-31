""" Game fix for Baldr Sky
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Installs d3dx9, d3dcompiler_43, d3dcompiler_47, lavfilters, quartz
    """

    util.protontricks('d3dx9')
    util.protontricks('d3dcompiler_43')
    util.protontricks('d3dcompiler_47')
    util.protontricks('lavfilters')
    util.protontricks('quartz')

    """ Disables NvAPI, Esync, Fsync and protonaudioconverter
    """

    util.disable_nvapi()
    util.disable_esync()
    util.disable_fsync()
    util.disable_protonaudioconverter()
