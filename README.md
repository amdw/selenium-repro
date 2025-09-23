This is a repro for a problem with ChromeDriver:

https://issues.chromium.org/issues/42323434#comment62

As subsequently confirmed on the bug, this problem appears to be due to AppArmor configuration on Ubuntu:

https://issues.chromium.org/issues/42323434#comment74

A list of workarounds is available here:

https://chromium.googlesource.com/chromium/src/+/main/docs/security/apparmor-userns-restrictions.md
