%define name lavaps
%define version 2.7
%define release %mkrel 5

Summary: 	A lava lamp of currently running processes
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Monitoring
URL:	 	http://www.isi.edu/~johnh/SOFTWARE/LAVAPS
Source0: 	%{name}-%{version}.tar.bz2
Patch0:		lavaps-gcc.patch.bz2
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  GConf2

%description
Lavaps is an interactive process-tracking program like ``top'', but
with a much different attitude.  Rather than presenting lots of
specific info in digital form, it tries to present certain important
information in a graphical analog form.  The idea is that you can run
it in the background and get a rough idea of what's happening to your
system without devoting much concentration to the task.


%prep
rm -rf $RPM_BUILD_ROOT

%setup

%patch0 -p1

%build
%configure

make

%install
%makeinstall

%find_lang %name

(cd $RPM_BUILD_ROOT
mkdir -p .%{_menudir}
cat > ./usr/lib/menu/%{name} <<EOF
?package(lavaps):needs="x11" section="Applications/Monitoring"  title="Lavaps" \
longtitle="A graphical process viewer" icon="monitoring_section.png" command="lavaps"
EOF
)

rm -rf $RPM_BUILD_ROOT%_sysconfdir/gconf/gconf.xml.defaults/%gconf.xml
rm -rf $RPM_BUILD_ROOT%_sysconfdir/gconf/gconf.xml.defaults/apps/%gconf.xml

rm -rf $RPM_BUILD_ROOT%_sysconfdir/gconf/gconf.xml.defaults/schemas/%gconf.xml
rm -rf $RPM_BUILD_ROOT%_sysconfdir/gconf/gconf.xml.defaults/schemas/apps/%gconf.xml

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_menudir}/*
#%_sysconfdir/gconf/gconf.xml.defaults/apps/lavaps/%gconf.xml
#%_sysconfdir/gconf/gconf.xml.defaults/schemas/apps/lavaps/%gconf.xml
%_sysconfdir/gconf/schemas/lavaps.schemas

