Summary:	Versatile file search utility for the Xfce desktop
Name:		catfish
Version:	4.20.0
Release:	3
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	https://archive.xfce.org/src/apps/catfish/4.20/%{name}-%{version}.tar.bz2
# Source0-md5:	16e66e895dc997e5effe163f610858b8
URL:		https://docs.xfce.org/apps/catfish/
BuildRequires:	glib2-devel >= 1:2.72.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	python3-dbus
BuildRequires:	python3-distutils-extra
BuildRequires:	python3-modules
BuildRequires:	python3-pexpect
BuildRequires:	python3-pygobject3
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.726
BuildRequires:	xfconf-devel >= 4.20.0
BuildRequires:	zeitgeist-devel
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	mlocate
Requires:	python3-dbus
Requires:	python3-pexpect
Requires:	python3-pygobject3
Suggests:	python3-zeitgeist
Suggests:	zeitgeist
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catfish is a versatile file search utility for the Xfce desktop.
Powered by Python and GTK, it is fast, flexible, and exceptional at
finding files.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/org.xfce.Catfish.desktop
%{_datadir}/metainfo/catfish.appdata.xml
%{_iconsdir}/hicolor/*/*/*
%{py3_sitescriptdir}/catfish
%{py3_sitescriptdir}/catfish_lib
%{_datadir}/catfish
%{_mandir}/man1/catfish.1*
