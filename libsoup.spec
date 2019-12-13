Name:           libsoup
Version:        2.66.1
Release:        1
Summary:        An HTTP library implementation
License:        LGPLv2
URL:            https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/%{name}/2.66/%{name}-%{version}.tar.xz
BuildRequires:  glib2-devel glib-networking krb5-devel gobject-introspection-devel gettext
BuildRequires:  libxml2-devel libpsl-devel sqlite-devel vala gtk-doc meson libxslt

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
%meson -Ddoc=true
%meson_build

%install
%meson_install

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
%{_datadir}/gtk-doc/html/*

%changelog
* Wed Aug 28 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.66.1-1
- Package init
