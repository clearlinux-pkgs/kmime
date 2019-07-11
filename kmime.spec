#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmime
Version  : 19.04.3
Release  : 22
URL      : https://download.kde.org/stable/applications/19.04.3/src/kmime-19.04.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.3/src/kmime-19.04.3.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.3/src/kmime-19.04.3.tar.xz.sig
Summary  : Library for handling mail messages and newsgroup articles
Group    : Development/Tools
License  : LGPL-2.1
Requires: kmime-lib = %{version}-%{release}
Requires: kmime-license = %{version}-%{release}
Requires: kmime-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# KMime #
[TOC]
# Introduction # {#introduction}
KMime is a library for handling mail messages and newsgroup articles. Both mail messages and
newsgroup articles are based on the same standard called MIME, which stands for
**Multipurpose Internet Mail Extensions**. In this document, the term `message` is used to
refer to both mail messages and newsgroup articles.

%package dev
Summary: dev components for the kmime package.
Group: Development
Requires: kmime-lib = %{version}-%{release}
Provides: kmime-devel = %{version}-%{release}
Requires: kmime = %{version}-%{release}
Requires: kmime = %{version}-%{release}

%description dev
dev components for the kmime package.


%package lib
Summary: lib components for the kmime package.
Group: Libraries
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
%setup -q -n kmime-19.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562875101
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1562875101
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmime
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kmime/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libkmime5

%files
%defattr(-,root,root,-)

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
/usr/include/KF5/kmime_version.h
/usr/lib64/cmake/KF5Mime/KF5MimeConfig.cmake
/usr/lib64/cmake/KF5Mime/KF5MimeConfigVersion.cmake
/usr/lib64/cmake/KF5Mime/KF5MimeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Mime/KF5MimeTargets.cmake
/usr/lib64/libKF5Mime.so
/usr/lib64/qt5/mkspecs/modules/qt_KMime.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Mime.so.5
/usr/lib64/libKF5Mime.so.5.11.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmime/COPYING.LIB

%files locales -f libkmime5.lang
%defattr(-,root,root,-)

