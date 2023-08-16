# Not official release yet
%define snapshot 20230216
%define commit 1b35b0269f3d03e56377eb86ffdc55753524f234
%define shortcommit %(c=%{commit}; echo ${c:0:7})


Summary:	Better desktop integration for Riot.im (not only) for GNOME
Name: 		revolt
Version:	0
Release:	%{?snapshot:0.%{snapshot}.}1
License:	GPLv3 and CC-BY-SA-3.0
Group:		Networking/Instant messaging
URL:		https://github.com/aperezdc/revolt/
#Source0:	https://github.com/aperezdc/%{name}/%{version}/%{name}-%{version}.tar.gz
#Source0:	https://github.com/aperezdc/%{name}/archive/%{?snapshot:master}%{!?snapshot:%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:%{version}}.tar.gz
Source0:	https://github.com/aperezdc/%{name}/archive/%{?snapshot:%{commit}}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	python%{pyver}dist(pygobject)

BuildArch: 	noarch

%description
Revolt is a small application which wraps Element to provide better integration
with desktop environments in general, and GNOME in particular:

 * Having Element as a “standalone” application with its own window, launcher,
   icon, etc. instead of it living in a browser tab.
 * Persistent notifications (for desktop environments supporting them, i.e. GNOME).
   Notifications are automatically prevented when the Revolt window is focused.
 * Status icon for desktop environment which have a tray bar applet (XFCE, Budgie,
   likely many others).

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_iconsdir}/hicolor/*/status/*.svg
%{_datadir}/glib-2.0/schemas/*.gschema.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
%configure
%make_build

%install
%make_install

