# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'volumes_with_meta'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'project'
# The slug of the panel group the PANEL is associated with.
PANEL_GROUP = 'compute'

# Python panel class of the PANEL to be added.
ADD_PANEL = \
    'horizon_metadata_plugin.content.volumes.panel.Volumes'
