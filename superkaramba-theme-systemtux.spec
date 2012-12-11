%define base_name       superkaramba-theme
%define theme_name      systemtux
%define name            %{base_name}-%{theme_name}
%define version         1.3
%define release         %mkrel 6

Name:	 %{name}
Version: %{version}
Release: %{release}
Summary: Monitoring theme for superkaramba
License: GPL
Group:   Monitoring
Source:  %{theme_name}_%{version}.tar.bz2
URL:     http://kde-look.org/content/show.php?content=16265
Requires: superkaramba >= 0.35
Requires: python
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
This is a superkaramba theme which is a desktop applet 
that displays system information.


%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{theme_name}_%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/apps/superkaramba/themes/%{theme_name}
cp -rf * %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name} 


%clean
rm -rf $RPM_BUILD_ROOT

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


%files
%defattr(-,root,root)
%doc COPYING
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*





%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.3-6mdv2010.0
+ Revision: 434192
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3-5mdv2009.0
+ Revision: 261241
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3-4mdv2009.0
+ Revision: 253760
- rebuild

* Sun Mar 02 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1.3-2mdv2008.1
+ Revision: 177560
- [BUGFIX] Fix uninstall ( thanks misc) (Bug #22642)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.3-1mdv2008.1
+ Revision: 128071
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel


* Sun Mar 06 2005 Sebastien Savarin <plouf@mandriva.org> 1.3-1mdk
-First Mandriva Linux

