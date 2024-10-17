Summary: 	A lava lamp of currently running processes
Name: 		lavaps
Version: 	2.7
Release: 	%{mkrel 10}
License: 	GPLv2+
Group: 		Monitoring
URL:	 	https://www.isi.edu/~johnh/SOFTWARE/LAVAPS
Source0: 	%{name}-%{version}.tar.bz2
Patch0:		lavaps-gcc.patch
# Drop an unnecessary include that breaks build - AdamW 2008/12
Patch1:		lavaps-2.7-include.patch
# GCC 4.3 include issues - AdamW 2008/12
Patch2:		lavaps-2.7-gcc43.patch
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  GConf2
BuildRequires:  gnomeui2-devel
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
Lavaps is an interactive process-tracking program like ``top'', but
with a much different attitude.  Rather than presenting lots of
specific info in digital form, it tries to present certain important
information in a graphical analog form.  The idea is that you can run
it in the background and get a rough idea of what's happening to your
system without devoting much concentration to the task.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .include
%patch2 -p1 -b .gcc43

%build
%configure
make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Categories=System;Monitor;
Name=Lavaps
Comment=A graphical process viewer
Icon=monitoring_section
Exec=lavaps
EOF

rm -rf %{buildroot}%_sysconfdir/gconf/gconf.xml.defaults/%gconf.xml
rm -rf %{buildroot}%_sysconfdir/gconf/gconf.xml.defaults/apps/%gconf.xml

rm -rf %{buildroot}%_sysconfdir/gconf/gconf.xml.defaults/schemas/%gconf.xml
rm -rf %{buildroot}%_sysconfdir/gconf/gconf.xml.defaults/schemas/apps/%gconf.xml

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-*.desktop
#%_sysconfdir/gconf/gconf.xml.defaults/apps/lavaps/%gconf.xml
#%_sysconfdir/gconf/gconf.xml.defaults/schemas/apps/lavaps/%gconf.xml
%{_sysconfdir}/gconf/schemas/lavaps.schemas

