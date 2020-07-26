%define api		0.4
%define major		0
%define libname		%mklibname ayatana-ido3 _%{api} %{major}
%define girayatananame	%mklibname ayatana-ido3-gir %{api}
%define develname	%mklibname ayatana-ido3 -d

Name:		ayatana-ido
Version:	0.5.0
Release:	1
Summary:	Ayatana Indicator Display Objects
Group:		System/Libraries
License:	GPLv3 AND LGPLv3 AND LGPLv2+
URL:		https://ayatanaindicators.github.io/
Source0:	https://github.com/AyatanaIndicators/ayatana-ido/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gtk-doc
BuildRequires:	mate-common
BuildRequires:	vala
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Widgets and other objects used for indicators.

#------------------------------------------------

%package -n	%{libname}
Summary:	Shared library providing extra GTK+3 menu items in system indicators
Group:		System/Libraries

%description -n	%{libname}
Shared library providing extra GTK+3 menu items for display in
system indicators.

This package contains the GTK+3 shared libraries.

#------------------------------------------------

%package -n	%{girayatananame}
Summary:	GObject Introspection interface description for Ayatana Indicator3
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n	%{girayatananame}
This package provides the GObject Introspection interface description
for Ayatana Ido3 and GTK+3.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}3 (GTK+3)
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girayatananame} = %{version}-%{release}
Provides:	%{name}3-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}3 (GTK+3).

#------------------------------------------------

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%license COPYING*
%doc AUTHORS* ChangeLog
%{_libdir}/libayatana-ido3-%{api}.so.%{major}{,.*}

%files -n %{girayatananame}
%{_libdir}/girepository-1.0/AyatanaIdo3-%{api}.typelib

%files -n %{develname}
%{_includedir}/libayatana-ido3-%{api}/
%{_libdir}/libayatana-ido3-%{api}.so
%{_libdir}/pkgconfig/libayatana-ido3-%{api}.pc
%{_datadir}/gir-1.0/AyatanaIdo3-%{api}.gir
%{_datadir}/vala/vapi/AyatanaIdo3-%{api}.vapi
