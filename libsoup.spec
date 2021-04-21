Name:           libsoup
Version:        2.72.0
Release:        2
Summary:        An HTTP library implementation
License:        LGPLv2
URL:            https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/%{name}/2.72/%{name}-%{version}.tar.xz
BuildRequires:  glib2-devel glib-networking krb5-devel gobject-introspection-devel gettext
BuildRequires:  libxml2-devel libpsl-devel sqlite-devel vala gtk-doc meson libxslt
BuildRequires:  samba-winbind-clients brotli-devel 
BuildRequires:  pkgconfig(sysprof-capture-4)

Requires:       glib2 glib-networking

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
