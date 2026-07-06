# tinygo-copr

RPM packaging for the latest [TinyGo](https://tinygo.org) release, built for
Fedora via [COPR](https://copr.fedorainfracloud.org/). This repackages the
official upstream prebuilt Linux binary release (it is self-contained and does
not build against the system LLVM), because the Fedora distro package lags
behind upstream.

## Install

```bash
sudo dnf copr enable blacktau/tinygo
sudo dnf install tinygo
tinygo version
```

## What's here

- `tinygo.spec` — the RPM spec (version-pinned to the packaged release).
- `.copr/Makefile` — COPR `make_srpm` entry point; downloads the upstream
  tarball and builds the SRPM inside the COPR builder.

## Updating to a new TinyGo release

Bump `Version:` and the `%changelog` in `tinygo.spec`, push, and rebuild the
COPR (`copr-cli build blacktau/tinygo` from a checkout, or via the web UI /
webhook).
