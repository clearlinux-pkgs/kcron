#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kcron
Version  : 21.12.0
Release  : 34
URL      : https://download.kde.org/stable/release-service/21.12.0/src/kcron-21.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.0/src/kcron-21.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: kcron-data = %{version}-%{release}
Requires: kcron-lib = %{version}-%{release}
Requires: kcron-license = %{version}-%{release}
Requires: kcron-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

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
%setup -q -n kcron-21.12.0
cd %{_builddir}/kcron-21.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639633371
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1639633371
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcron
cp %{_builddir}/kcron-21.12.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcron/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kcron-21.12.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcron/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang kcron

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/kcron_helper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/local.kcron.crontab.service
/usr/share/dbus-1/system.d/local.kcron.crontab.conf
/usr/share/kservices5/kcm_cron.desktop
/usr/share/metainfo/org.kde.kcron.metainfo.xml
/usr/share/polkit-1/actions/local.kcron.crontab.policy
/usr/share/qlogging-categories5/kcron.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/de/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/de/kcontrol5/kcron/kcronstart.png
/usr/share/doc/HTML/de/kcontrol5/kcron/newtask.png
/usr/share/doc/HTML/de/kcontrol5/kcron/newvariable.png
/usr/share/doc/HTML/en/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/en/kcontrol5/kcron/kcronstart.png
/usr/share/doc/HTML/en/kcontrol5/kcron/newtask.png
/usr/share/doc/HTML/en/kcontrol5/kcron/newvariable.png
/usr/share/doc/HTML/es/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/es/kcontrol5/kcron/print.png
/usr/share/doc/HTML/et/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/et/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/fr/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/fr/kcontrol5/kcron/kcron.png
/usr/share/doc/HTML/fr/kcontrol5/kcron/kcronstart.png
/usr/share/doc/HTML/fr/kcontrol5/kcron/newtask.png
/usr/share/doc/HTML/fr/kcontrol5/kcron/newvariable.png
/usr/share/doc/HTML/fr/kcontrol5/kcron/print.png
/usr/share/doc/HTML/it/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/ko/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/ko/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/nl/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/nl/kcontrol5/kcron/newtask.png
/usr/share/doc/HTML/nl/kcontrol5/kcron/newvariable.png
/usr/share/doc/HTML/nl/kcontrol5/kcron/print.png
/usr/share/doc/HTML/pt/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/pt/kcontrol5/kcron/kcron.png
/usr/share/doc/HTML/pt/kcontrol5/kcron/kcronstart.png
/usr/share/doc/HTML/pt/kcontrol5/kcron/newtask.png
/usr/share/doc/HTML/pt/kcontrol5/kcron/newvariable.png
/usr/share/doc/HTML/pt/kcontrol5/kcron/print.png
/usr/share/doc/HTML/pt_BR/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol5/kcron/kcronstart.png
/usr/share/doc/HTML/pt_BR/kcontrol5/kcron/newtask.png
/usr/share/doc/HTML/pt_BR/kcontrol5/kcron/newvariable.png
/usr/share/doc/HTML/ru/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/sv/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/sv/kcontrol5/kcron/kcronstart.png
/usr/share/doc/HTML/sv/kcontrol5/kcron/newtask.png
/usr/share/doc/HTML/sv/kcontrol5/kcron/newvariable.png
/usr/share/doc/HTML/uk/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol5/kcron/index.docbook
/usr/share/doc/HTML/uk/kcontrol5/kcron/kcronstart.png
/usr/share/doc/HTML/uk/kcontrol5/kcron/newtask.png
/usr/share/doc/HTML/uk/kcontrol5/kcron/newvariable.png
/usr/share/doc/HTML/zh_CN/kcontrol5/kcron/index.cache.bz2
/usr/share/doc/HTML/zh_CN/kcontrol5/kcron/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_cron.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcron/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kcron/8287b608d3fa40ef401339fd907ca1260c964123

%files locales -f kcron.lang
%defattr(-,root,root,-)

