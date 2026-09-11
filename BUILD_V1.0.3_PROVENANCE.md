# Invertebrate Virtual Laboratory v1.0.3 — build provenance

Source supplied as `InvertebrateLab_1.0.3_android_project.zip`.

- Source ZIP SHA-256: `5535afc6b0f23e14601ee570350edbb39fb7c28376e76e2c31565d4fe58b33be`
- Source HTML SHA-256: `d48d16ef2f66ff5b651e717cfd7e7334d195bf1ef438af8bcb61a038fdd957fe`
- Build environment workflow: run `34587766202`
- Gradle: 8.9
- Android Gradle Plugin: 8.7.3
- Kotlin: 2.0.21
- compileSdk / targetSdk: 36
- minSdk: 24
- Build Tools available: 34.0.0 and 36.0.0
- Build mode: strict Gradle offline mode using the GitHub-provisioned dependency cache and Android SDK

## Produced debug APK

- Package: `com.gasczoology.invertebratelab.debug`
- versionCode: `103`
- versionName: `1.0.3-debug`
- APK SHA-256: `e6c311885d31b6859c947e6b85e79b75700e0ca4ffe68f667592dc5d32292c91`
- Size: 6,089,533 bytes
- APK Signature Scheme v2: verified
- INTERNET permission: absent
- Bundled `index.html` and all nine Museum plate JPEG files match the supplied source byte-for-byte by SHA-256.

## Quality-gate note

`:app:assembleDebug` passed. An offline `lintDebug` attempt could not resolve `com.android.tools.lint:lint-gradle:31.7.3` because that lint-only artifact had not been primed into the frozen Gradle cache. This is an environment/cache limitation, not a compiler or APK packaging error. Do not classify lint as passed until it is rerun with the required lint dependency available.
