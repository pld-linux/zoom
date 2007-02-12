%define		_beta beta1
Summary:	X Window System interpreter for old Infocom text games
Summary(pl.UTF-8):   Działający pod X Window System interpreter dla starych tekstówek Infocomu
Name:		zoom
Version:	1.0.2
Release:	0.%{_beta}.1
License:	GPL
Group:		Applications/Games
Source0:	http://www.logicalshift.co.uk/unix/zoom/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	bb5e302194634715c9d1c8c4951f1257
Patch0:		%{name}-freetype.patch
Patch1:		%{name}-paths.patch
URL:		http://www.logicalshift.demon.co.uk/unix/zoom/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	t1lib-devel
BuildRequires:	xft-devel >= 2.0
Provides:	zcode-interpreter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Window System interpreter for old Infocom text games, so called
Interactive Fiction Adventure.

%description -l pl.UTF-8
Działający pod X Window System interpreter dla starych tekstówek
Infocomu, zwanych także Interactive Fiction Adventure.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/zoom/zoomrc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO THANKS
%doc manual/{*.html,*.png,*.gif}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zoomrc
%attr(755,root,root) %{_bindir}/zoom
