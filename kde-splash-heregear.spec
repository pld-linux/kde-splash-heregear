%define		_splash		heregear

Summary:	KDE splash screen
Summary(pl.UTF-8):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/27547-heregear.tar.gz
# Source0-md5:	5d59470c6ad93ec9effba2c0ffd95f3c
Source1:	http://www.kde-look.org/content/files/33730-heregear.tar.gz
# Source1-md5:	47daa896b4778a05420dc2a069c300b5
Patch0:		%{name}-moodin.patch
URL:		http://www.kde-look.org/content/show.php?content=33730
Requires:	kdebase-desktop >= 9:3.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Splash screen based on here-gear wallpaper. Simple 3D art with KDE
gear.

%description -l pl.UTF-8
Ekran startowy oparty na tapecie here-gear. Prosta grafika 3D z
"zębatką KDE".

%package -n kde-splash-%{_splash}-moodin
Summary:	KDE splash screen
Summary(pl.UTF-8):	Ekran startowy KDE
Group:		X11/Amusements
Requires:	kdebase-desktop >= 9:3.4.0
Requires:	kde-splash-moodin

%description -n kde-splash-%{_splash}-moodin
Splash screen based on here-gear wallpaper. Simple 3D art with KDE
gear. Moodin version. Designed for 1024x768 resolution.

%description -n kde-splash-%{_splash}-moodin -l pl.UTF-8
Ekran startowy oparty na tapecie here-gear. Prosta grafika 3D z
"zębatką KDE". Wersja dla silnika Moodin. Przygotowana dla
rozdzielczości 1024x768.

%prep
%setup -q -n %{_splash} -a1
%patch -P0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/{%{_splash},%{_splash}-moodin}
install readme *.{txt,png,rc} $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install %{_splash}/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}-moodin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/heregear

%files -n kde-splash-%{_splash}-moodin
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/heregear-moodin
