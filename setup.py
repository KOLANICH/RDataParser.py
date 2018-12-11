#!/usr/bin/env python3
import os
from setuptools import setup

from pathlib import Path
thisDir=Path(__file__).parent

formatsPath=thisDir / "kaitai_struct_formats"
kaitaiSetuptoolsCfg={
	"formats":{
		"r_data.py": {
			"path":"serialization/r_data.ksy",
		}
	},
	"formatsRepo": {
		"git": "https://github.com/KOLANICH/kaitai_struct_formats.git",
		"refspec": "RData",
		"localPath" : formatsPath,
		"update": True
	},
	"outputDir": thisDir / "RDataParser",
	"inputDir": formatsPath
}

setup(use_scm_version = True, kaitai=kaitaiSetuptoolsCfg)