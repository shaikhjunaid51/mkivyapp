[app]

# App basic info
title = MyApp
package.name = myapp
package.domain = org.test

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# Version
version = 1.0

# Requirements (safe default)
requirements = python3,kivy

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0



# ---------------- ANDROID ----------------

# Stable Android config (IMPORTANT)
android.api = 33
android.minapi = 21
android.target = 33
android.sdk = 33
android.ndk = 25b

# CPU support
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Don't download random new sdk
android.accept_sdk_license = True



# ---------------- BUILD ----------------

# Log level
log_level = 2

# Warn on root
warn_on_root = 0



# ---------------- GRAPHICS ----------------
fullscreen = 0
orientation = portrait



# ---------------- PYTHON FOR ANDROID ----------------
p4a.branch = stable
