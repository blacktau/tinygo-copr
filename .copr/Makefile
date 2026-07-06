# COPR make_srpm entry point. COPR invokes:
#   make -f .copr/Makefile srpm outdir=<abs> spec=<abs>
# from the cloned repo root. We fetch Source0 (the upstream tarball) here so
# the large source is downloaded inside the COPR builder, not uploaded.
outdir ?= $(CURDIR)

.PHONY: srpm
srpm:
	dnf -y install rpm-build rpmdevtools
	spectool -g -C $(CURDIR) tinygo.spec
	rpmbuild -bs tinygo.spec \
	  --define "_sourcedir $(CURDIR)" \
	  --define "_srcrpmdir $(outdir)"
