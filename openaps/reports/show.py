
"""
show   - show all reports
"""

from openaps.devices.device import Device
from openaps.reports.report import Report

def configure_app (app, parser):
  parser.set_defaults(report='*')
  parser._actions[-1].nargs = '?'
  if parser._actions[-1].choices:
    parser._actions[-1].choices.append('*')
def main (args, app):
  print args
  for device in Report.FromConfig(app.config):
    print device.format_url( )

