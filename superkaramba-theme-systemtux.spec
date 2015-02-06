%define theme_name systemtux

Summary:	Monitoring theme for superkaramba
Name:		superkaramba-theme-%{theme_name}
Version:	1.3
Release:	8
License:	GPL
Group:		Monitoring
Url:		http://kde-look.org/content/show.php?content=16265
Source0:	%{theme_name}_%{version}.tar.bz2
Requires:	superkaramba
BuildArch:	noarch

%description
This is a superkaramba theme which is a desktop applet that displays
system information.

%files
%doc COPYING
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*

%post
if [ $1 = 1 ]; then
echo "THEME path=%{theme_name}/%{theme_name}-ModAmarok.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{theme_name}-Modjuk.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{theme_name}-ModClock.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{theme_name}-ModNoatun.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{theme_name}-ModSystem.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{theme_name}-ModXmms.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{theme_name}_v1.1.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
fi

%postun
if [ $1 = 0 ]; then
cat %{_datadir}/apps/superkaramba/themes/default.theme | grep -v "%{theme_name}" > %{_datadir}/apps/superkaramba/themes/default.theme
exit 0
fi

#----------------------------------------------------------------------------

%prep
%setup -q -n %{theme_name}_%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}
cp -rf * %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}

