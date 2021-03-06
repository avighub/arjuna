# This file is a part of Arjuna
# Copyright 2015-2020 Rahul Verma

# Website: www.RahulVerma.net

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from arjuna import *
from arjex.lib.app_page.app import WordPress

@for_test
def dashboard(request):
    # Setup
    wordpress = WordPress()
    home = wordpress.launch_app()
    dashboard = home.login_with_default_creds()
    yield dashboard

    # Teadown
    dashboard.logout()

@test
def check_with_wp_app_page(request, dashboard):
    dashboard.settings_page.tweak_role_value("editor")