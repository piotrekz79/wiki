# -*- coding: utf-8 -*-
#
# Copyright 2018 University of Bristol - High Performance Networks Research
# Group
# All Rights Reserved.
#
# Contributors: Anderson Bravalheri, Dimitrios Gkounis, Abubakar Siddique
# Muqaddas, Navdeep Uniyal, Reza Nejabati and Dimitra Simeonidou
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# For those usages not covered by the Apache License, Version 2.0 please
# contact with: <highperformance-networks@bristol.ac.uk>
#
# Neither the name of the University of Bristol nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# This work has been performed in the context of DCMS UK 5G Testbeds
# & Trials Programme and in the framework of the Metro-Haul project -
# funded by the European Commission under Grant number 761727 through the
# Horizon 2020 and 5G-PPP programmes.
##
from .wimconn import WimConnector
import random
import requests
import json
import logging
import uuid
import logging

class OdlConnector(WimConnector):

        def __init__(self, wim, wim_account, mapping =None, logger=None, persistance=None):
                self.logger = logger or logging.getLogger('openmano.wim.wimconn')
                self.wim = wim
                self.wim_account = wim_account
                self.mapping = mapping or {}
                self.logger = logger or {}
                self.persistance = persistance

        def get_connectivity_service_status(self, link_uuid):

                return {"wim_status" : "ACTIVE"}


        def create_connectivity_service(self, *args, **kwargs):
                service_uuid = uuid.uuid1()
                service_info = {"went": "well"}
                service = (str(service_uuid),service_info)

                return service

        def delete_connectivity_service(self, link_uuid):

                return ("Deleted")


