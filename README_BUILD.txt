INVERTEBRATE VIRTUAL LABORATORY - ANDROID BUILD

Native Android WebView wrapper around the complete offline Invertebrate Virtual Laboratory HTML application.

Package: com.gasczoology.invertebratelab
Version: 1.0.2 (102)
Minimum Android: 7.0 (API 24)
Target/Compile SDK: 36
Core operation: offline; no INTERNET permission
Launcher icon: starfish

GitHub build:
1. Open Actions -> Build Android APK.
2. Run the workflow, or push to main to trigger it automatically.
3. The workflow builds app-debug.apk with the official Android Gradle toolchain.
4. It verifies the APK using apksigner and inspects package metadata using aapt.
5. Download the artifact named Invertebrate-Virtual-Laboratory-v1.0.2-debug-APK.

This workflow output is a debug-signed verification build. Before classroom
distribution, install it on a physical Android device, verify an upgrade from
v1.0.0, test all language modes offline, and create a separately signed release
build using a protected release keystore.

The bundled laboratory is stored at app/src/main/assets/www/index.html.
