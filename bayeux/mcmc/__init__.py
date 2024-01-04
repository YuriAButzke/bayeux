# Copyright 2023 The bayeux Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Imports from submodules."""
# pylint: disable=g-importing-member
# pylint: disable=g-import-not-at-top
import importlib

__all__ = []
if importlib.util.find_spec("blackjax") is not None:
  from bayeux._src.mcmc.blackjax import CheesHMC as CheesHMCblackjax
  from bayeux._src.mcmc.blackjax import HMC as HMCblackjax
  from bayeux._src.mcmc.blackjax import HMCPathfinder as HMC_Pathfinder_blackjax
  from bayeux._src.mcmc.blackjax import MeadsHMC as MeadsHMCblackjax
  from bayeux._src.mcmc.blackjax import NUTS as NUTSblackjax
  from bayeux._src.mcmc.blackjax import NUTSPathfinder as NUTS_Pathfinder_blackjax
  __all__.extend(["HMCblackjax", "CheesHMCblackjax", "MeadsHMCblackjax",
                  "NUTSblackjax", "HMC_Pathfinder_blackjax",
                  "NUTS_Pathfinder_blackjax"])

if importlib.util.find_spec("numpyro") is not None:
  from bayeux._src.mcmc.numpyro import HMC as HMCnumpyro
  from bayeux._src.mcmc.numpyro import NUTS as NUTSnumpyro

  __all__.extend(["HMCnumpyro", "NUTSnumpyro"])
