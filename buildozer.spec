[app]

# App info
title = MyApp
package.name = myapp
package.domain = org.test

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# Version
version = 1.0

# Requirements
requirements = python3,kivy

# Screen
orientation = portrait
fullscreen = 0


# -------- ANDROID CONFIG --------

# Stable API (very important)
android.api = 33
android.minapi = 21
android.target = 33
android.sdk = 33

# Correct NDK
android.ndk = 25b

# CPU
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Accept licenses automatically
android.accept_sdk_license = True


# -------- BUILD SETTINGS --------
log_level = 2
warn_on_root = 0


# -------- Python for Android --------
p4a.branch = stable
