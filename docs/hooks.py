import os
import shutil

def copy_privacy_policy(config, **kwargs):
    site_dir = config['site_dir']
    shutil.copy('assets/privacy_policy.html', site_dir)
