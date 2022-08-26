#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kmime
Version  : 22.08.0
Release  : 54
URL      : https://download.kde.org/stable/release-service/22.08.0/src/kmime-22.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.0/src/kmime-22.08.0.tar.xz
Summary  : Library for handling mail messages and newsgroup articles
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: kmime-data = %{version}-%{release}
Requires: kmime-lib = %{version}-%{release}
Requires: kmime-license = %{version}-%{release}
Requires: kmime-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcodecs-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev

%description
SPDX-License-Identifier: CC0-1.0

%package data
Summary: data components for the kmime package.
Group: Data

%description data
data components for the kmime package.


%package dev
Summary: dev components for the kmime package.
Group: Development
Requires: kmime-lib = %{version}-%{release}
Requires: kmime-data = %{version}-%{release}
Provides: kmime-devel = %{version}-%{release}
Requires: kmime = %{version}-%{release}

%description dev
dev components for the kmime package.


%package lib
Summary: lib components for the kmime package.
Group: Libraries
Requires: kmime-data = %{version}-%{release}
Requires: kmime-license = %{version}-%{release}

%description lib
lib components for the kmime package.


%package license
Summary: license components for the kmime package.
Group: Default

%description license
license components for the kmime package.


%package locales
Summary: locales components for the kmime package.
Group: Default

%description locales
locales components for the kmime package.


%prep
%setup -q -n kmime-22.08.0
cd %{_builddir}/kmime-22.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661545180
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
export SOURCE_DATE_EPOCH=1661545180
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmime
cp %{_builddir}/kmime-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmime/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/kmime-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmime/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmime-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmime/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmime-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kmime/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kmime-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmime/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kmime-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kmime/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/kmime-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kmime/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd
%find_lang libkmime5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kmime.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KMime/KMime/Content
/usr/include/KF5/KMime/KMime/ContentIndex
/usr/include/KF5/KMime/KMime/DateFormatter
/usr/include/KF5/KMime/KMime/HeaderParsing
/usr/include/KF5/KMime/KMime/Headers
/usr/include/KF5/KMime/KMime/KMimeMessage
/usr/include/KF5/KMime/KMime/MDN
/usr/include/KF5/KMime/KMime/Message
/usr/include/KF5/KMime/KMime/NewsArticle
/usr/include/KF5/KMime/KMime/Types
/usr/include/KF5/KMime/KMime/Util
/usr/include/KF5/KMime/kmime/kmime_content.h
/usr/include/KF5/KMime/kmime/kmime_contentindex.h
/usr/include/KF5/KMime/kmime/kmime_dateformatter.h
/usr/include/KF5/KMime/kmime/kmime_export.h
/usr/include/KF5/KMime/kmime/kmime_header_parsing.h
/usr/include/KF5/KMime/kmime/kmime_headers.h
/usr/include/KF5/KMime/kmime/kmime_mdn.h
/usr/include/KF5/KMime/kmime/kmime_message.h
/usr/include/KF5/KMime/kmime/kmime_newsarticle.h
/usr/include/KF5/KMime/kmime/kmime_types.h
/usr/include/KF5/KMime/kmime/kmime_util.h
/usr/include/KF5/KMime/kmime_version.h
/usr/lib64/cmake/KF5Mime/KF5MimeConfig.cmake
/usr/lib64/cmake/KF5Mime/KF5MimeConfigVersion.cmake
/usr/lib64/cmake/KF5Mime/KF5MimeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Mime/KF5MimeTargets.cmake
/usr/lib64/libKF5Mime.so
/usr/lib64/qt5/mkspecs/modules/qt_KMime.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Mime.so.5
/usr/lib64/libKF5Mime.so.5.21.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmime/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmime/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kmime/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmime/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kmime/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/kmime/cadc9e08cb956c041f87922de84b9206d9bbffb2

%files locales -f libkmime5.lang
%defattr(-,root,root,-)

