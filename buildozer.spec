[app]
# (str) Title of your application
title = ANITA

# (str) Package name
package.name = anita

# (str) Package domain (needed for android packaging)
package.domain = org.anita

# (list) Source files to include (let it include python files and images)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,customtkinter,pillow

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
# Log level
log_level = 2