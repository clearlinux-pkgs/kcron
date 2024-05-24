#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcron
Version  : 24.05.0
Release  : 66
URL      : https://download.kde.org/stable/release-service/24.05.0/src/kcron-24.05.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.0/src/kcron-24.05.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.0/src/kcron-24.05.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: kcron-data = %{version}-%{release}
Requires: kcron-lib = %{version}-%{release}
Requires: kcron-license = %{version}-%{release}
Requires: kcron-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KCron
KDE Task Scheduler
GUI crontab editor
Requires:
Unix POSIX libraries for localized dates and times (glibc)
Cron (vixie-cron)
Crontab (crontabs)

%package data
Summary: data components for the kcron package.
Group: Data

%description data
data components for the kcron package.


%package doc
Summary: doc components for the kcron package.
Group: Documentation

%description doc
doc components for the kcron package.


%package lib
Summary: lib components for the kcron package.
Group: Libraries
Requires: kcron-data = %{version}-%{release}
Requires: kcron-license = %{version}-%{release}

%description lib
lib components for the kcron package.


%package license
Summary: license components for the kcron package.
Group: Default

%description license
license components for the kcron package.


%package locales
Summary: locales components for the kcron package.
Group: Default

%description locales
locales components for the kcron package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kcron-24.05.0
cd %{_builddir}/kcron-24.05.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716572662
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1716572662
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcron
cp %{_builddir}/kcron-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcron/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kcron-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcron/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcron
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kauth/kcron_helper
/usr/lib64/libexec/kf6/kauth/kcron_helper

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_cron.desktop
/usr/share/dbus-1/system-services/local.kcron.crontab.service
/usr/share/dbus-1/system.d/local.kcron.crontab.conf
/usr/share/metainfo/org.kde.kcron.metainfo.xml
/usr/share/polkit-1/actions/local.kcron.crontab.policy
/usr/share/qlogging-categories6/kcron.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/de/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/de/kcontrol/kcron/kcronstart.png
/usr/share/doc/HTML/de/kcontrol/kcron/newtask.png
/usr/share/doc/HTML/de/kcontrol/kcron/newvariable.png
/usr/share/doc/HTML/en/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/en/kcontrol/kcron/kcronstart.png
/usr/share/doc/HTML/en/kcontrol/kcron/newtask.png
/usr/share/doc/HTML/en/kcontrol/kcron/newvariable.png
/usr/share/doc/HTML/es/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/es/kcontrol/kcron/print.png
/usr/share/doc/HTML/et/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/et/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/fr/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/fr/kcontrol/kcron/kcron.png
/usr/share/doc/HTML/fr/kcontrol/kcron/kcronstart.png
/usr/share/doc/HTML/fr/kcontrol/kcron/newtask.png
/usr/share/doc/HTML/fr/kcontrol/kcron/newvariable.png
/usr/share/doc/HTML/fr/kcontrol/kcron/print.png
/usr/share/doc/HTML/it/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/ko/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/ko/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/nl/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/nl/kcontrol/kcron/newtask.png
/usr/share/doc/HTML/nl/kcontrol/kcron/newvariable.png
/usr/share/doc/HTML/nl/kcontrol/kcron/print.png
/usr/share/doc/HTML/pt/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/pt/kcontrol/kcron/kcron.png
/usr/share/doc/HTML/pt/kcontrol/kcron/kcronstart.png
/usr/share/doc/HTML/pt/kcontrol/kcron/newtask.png
/usr/share/doc/HTML/pt/kcontrol/kcron/newvariable.png
/usr/share/doc/HTML/pt/kcontrol/kcron/print.png
/usr/share/doc/HTML/pt_BR/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/kcron/kcronstart.png
/usr/share/doc/HTML/pt_BR/kcontrol/kcron/newtask.png
/usr/share/doc/HTML/pt_BR/kcontrol/kcron/newvariable.png
/usr/share/doc/HTML/ru/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/sv/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/sv/kcontrol/kcron/kcronstart.png
/usr/share/doc/HTML/sv/kcontrol/kcron/newtask.png
/usr/share/doc/HTML/sv/kcontrol/kcron/newvariable.png
/usr/share/doc/HTML/uk/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/kcron/index.docbook
/usr/share/doc/HTML/uk/kcontrol/kcron/kcronstart.png
/usr/share/doc/HTML/uk/kcontrol/kcron/newtask.png
/usr/share/doc/HTML/uk/kcontrol/kcron/newvariable.png
/usr/share/doc/HTML/zh_CN/kcontrol/kcron/index.cache.bz2
/usr/share/doc/HTML/zh_CN/kcontrol/kcron/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cron.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cron.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcron/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kcron/8287b608d3fa40ef401339fd907ca1260c964123

%files locales -f kcron.lang
%defattr(-,root,root,-)

