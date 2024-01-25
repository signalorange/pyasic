# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from pyasic.miners.backends import M3X
from pyasic.miners.models import M33SPlusPlusVG40, M33SPlusPlusVH20, M33SPlusPlusVH30


class BTMinerM33SPlusPlusVH20(M3X, M33SPlusPlusVH20):
    pass


class BTMinerM33SPlusPlusVH30(M3X, M33SPlusPlusVH30):
    pass


class BTMinerM33SPlusPlusVG40(M3X, M33SPlusPlusVG40):
    pass
