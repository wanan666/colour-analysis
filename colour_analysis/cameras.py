# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
from vispy.scene.cameras import TurntableCamera

from colour import is_numeric


class OrbitCamera(TurntableCamera):
    def __init__(self,
                 fov=0.0,
                 elevation=30.0,
                 azimuth=30.0,
                 roll=0.0,
                 distance=None,
                 translate_speed=1.0,
                 **kwargs):
        TurntableCamera.__init__(self,
                                 fov,
                                 elevation,
                                 azimuth,
                                 roll,
                                 distance,
                                 **kwargs)

        self.__translate_speed = None
        self.translate_speed = translate_speed

    @property
    def translate_speed(self):
        """
        Property for **self.__translate_speed** private attribute.

        Returns
        -------
        numeric
            self.__translate_speed.
        """

        return self.__translate_speed

    @translate_speed.setter
    def translate_speed(self, value):
        """
        Setter for **self.__translate_speed** private attribute.

        Parameters
        ----------
        value : numeric
            Attribute value.
        """

        if value is not None:
            assert is_numeric(value), (
                '"{0}" type is not numeric!'.format('translate_speed', value))
            self.__translate_speed = value

        return self.__translate_speed

    def _dist_to_trans(self, distance):
        translate = np.asarray(TurntableCamera._dist_to_trans(self, distance))
        translate *= self.__translate_speed

        return translate