# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:09:23 2019

@author: Ray Johnson
Setup for PyRacer game

"""

import cx_Freeze
executables = [cx_Freeze.Executable("PyRacer.py")]

cx_Freeze.setup(
        name="PyRacer",
        options={"build_exe": {"packages": ["pygame","random","time","pickle"],
                               "include_files":["racecarSmCrashed2.png","racecarSm.png","score.dat"]}},
        executables = executables
        )