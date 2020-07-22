Summary:	Versatile file search utility for the Xfce desktop
Name:		catfish
Version:	1.4.13
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://archive.xfce.org/src/apps/catfish/1.4/%{name}-%{version}.tar.bz2
# Source0-md5:	750b65401c9445e185e71c808d7509a4
URL:		https://docs.xfce.org/apps/catfish/
BuildRequires:	python3-distutils-extra
BuildRequires:	python3-modules
BuildRequires:	python3-pexpect
BuildRequires:	python3-pygobject3
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	mlocate
Requires:	python3-dbus
Requires:	python3-pexpect
Requires:	python3-pygobject3
Suggests:	python3-zeitgeist
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catfish is a versatile file search utility for the Xfce desktop.
Powered by Python and GTK, it is fast, flexible, and exceptional at
finding files.

%prep
%setup -q

# fix #!/usr/bin/env python -> #!/usr/bin/python3:
find -name '*.py' | xargs %{__sed} -i -e '1s,^#!.*python$,#!%{__python3},'

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_localedir}}

cp -a build/share/applications/org.xfce.Catfish.desktop $RPM_BUILD_ROOT%{_desktopdir}/

%{__python3} setup.py install \
	--skip-build \
	--prefix=%{_prefix} \
	--install-purelib=%{py3_sitescriptdir} \
	--install-platlib=%{py3_sitedir} \
	--root=$RPM_BUILD_ROOT

cp -a build/mo/* $RPM_BUILD_ROOT%{_localedir}/

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/org.xfce.Catfish.desktop
%{_datadir}/metainfo/catfish.appdata.xml
%{_iconsdir}/hicolor/*/*/*
%{py3_sitescriptdir}/catfish-*.egg-info
%{py3_sitescriptdir}/catfish
%{py3_sitescriptdir}/catfish_lib
%{_datadir}/catfish
%{_mandir}/man1/catfish.1*
