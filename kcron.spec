#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcron
Version  : 19.12.2
Release  : 17
URL      : https://download.kde.org/stable/release-service/19.12.2/src/kcron-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/kcron-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/kcron-19.12.2.tar.xz.sig
Summary  : Configure and schedule tasks
Group    : Development/Tools
License  : GPL-2.0
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
%setup -q -n kcron-19.12.2
cd %{_builddir}/kcron-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581017446
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581017446
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcron
cp %{_builddir}/kcron-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/kcron/d357e60aa8efd63b4475c3363700ba54f9a71343
pushd clr-build
%make_install
popd
%find_lang kcron

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/kcm_cron.desktop
/usr/share/metainfo/org.kde.kcron.metainfo.xml
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_cron.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcron/d357e60aa8efd63b4475c3363700ba54f9a71343

%files locales -f kcron.lang
%defattr(-,root,root,-)

