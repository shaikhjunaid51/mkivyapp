[app]

# App info
title = Device Checker
package.name = devicechecker
package.domain = org.junaid

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Main file
entrypoint = main.py

# Requirements (VERY IMPORTANT)
requirements = python3,kivy,pyjnius

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Android permissions (needed for stability)
android.permissions = INTERNET

# Android API (stable for kivy)
android.api = 33
android.minapi = 21
android.ndk = 25b

# Faster builds
android.gradle_dependencies =

# Disable unnecessary stuff
android.enable_androidx = True

# Version
version = 1.0

# Icon (optional)
#icon.filename = %(source.dir)s/icon.png


[buildozer]

log_level = 2
warn_on_root = 1 
