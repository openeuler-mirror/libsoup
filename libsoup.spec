Name:           libsoup
Version:        2.74.3
Release:        1
Summary:        An HTTP library implementation
License:        LGPLv2
URL:            https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/%{name}/2.74/%{name}-%{version}.tar.xz
BuildRequires:  glib2-devel glib-networking krb5-devel gobject-introspection-devel gettext
BuildRequires:  libxml2-devel libpsl-devel sqlite-devel vala gtk-doc meson libxslt
BuildRequires:  samba-winbind-clients brotli-devel 
BuildRequires:  pkgconfig(sysprof-capture-4)

Requires:       glib2 glib-networking

Patch6000:      backport-skip-tls_interaction-test.patch

%description
libsoup is an HTTP client/server library for GNOME. It uses GObjects and the glib main loop,
to integrate well with GNOME applications, and also has a synchronous API,
for use in threaded applications.

%package        devel
Summary:        Header files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for %{name}.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install
sed -i 's/idm[0-9]\{5,32\}/idm12345678912345/g' %{buildroot}%{_datadir}/gtk-doc/html/libsoup-2.4/ix01.html

%check
%meson_test

%files
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{_libdir}/*.so.*
%{_datadir}/locale/*
%{_libdir}/girepository-1.0/Soup*2.4.typelib

%files          devel
%defattr(-,root,root)
%{_includedir}/%{name}*-2.4
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Soup*2.4.gir
%{_datadir}/vala/vapi/libsoup-2.4.*

%files          help
%defattr(-,root,root)
%doc README NEWS
%{_datadir}/gtk-doc/html/libsoup-2.4/*

%changelog
* Mon Jan 2 2023 lin zhang <lin.zhang@turbolinux.com.cn> - 2.74.3-1
- update to 2.74.3

* Wed Oct 26 2022 zhouwenpei <zhouwenpei1@h-partners.com> - 2.74.2-2
- Rebuild for next release

* Thu Dec 09 2021 liuyumeng <liuyumeng5@huawei.com> - 2.74.2-1
- update to libsoup-2.74.2

* Mon Apr 19 2021 zhanzhimin<zhanzhimin@huawei.com> - 2.72.0-3
- DESC:fix the complie failure due to glib-networking upgrade

* Mon Apr 19 2021 zhanzhimin<zhanzhimin@huawei.com> - 2.72.0-2
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:sed html idm for eliminate difference

* Wed Jan 27 2021 hanhui <hanhui15@huawei.com> - 2.72.0-1
- Type: enhancement
- ID:   NA
- SUG:  NA
- DESC: update to 2.72.0

* Thu Jul 23 2020 openEuler Buildteam <buildteam@openeuler.org> - 2.71.0-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:upgrade to 2.71.0

* Wed Aug 28 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.66.1-1
- Package init
