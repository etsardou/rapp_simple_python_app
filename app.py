#!/usr/bin/env python

import time
import sys

from rapp_robot_api import RappRobot
rh = RappRobot()
from RappCloud import RappPlatformAPI
ch = RappPlatformAPI()

rh.audio.setVolume(100)
rh.audio.speak("Hello there reviewers")



