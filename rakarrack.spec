Summary:	Guitar effects for Linux
Summary(pl.UTF-8):	Efekty gitarowe dla Linuksa
Name:		rakarrack
Version:	0.6.1
Release:	3
License:	GPL
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/rakarrack/%{name}-%{version}.tar.bz2
# Source0-md5:	56b1e04779ae3d56cc8a3ad3c4e25152
Patch0:		%{name}-build.patch
URL:		http://rakarrack.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	alsa-utils
BuildRequires:	fltk-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	alsa-utils
Requires:	jack-audio-connection-kit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rakarrack is a richly featured multi-effects processor emulating a
guitar effects pedalboard. Effects include compressor, expander, noise
gate, graphic equalizer, parametric equalizer, exciter, shuffle,
convolotron, valve, flanger, dual flange, chorus, musicaldelay, arpie,
echo with reverse playback, musical delay, reverb, digital phaser,
analogic phaser, synthfilter, varyband, ring, wah-wah, alien-wah,
mutromojo, harmonizer, looper and four flexible distortion modules
including sub-octave modulation and dirty octave up. Most of the
effects engine is built from modules found in the excellent software
synthesizer ZynAddSubFX. Presets and user interface are optimized for
guitar, but Rakarrack processes signals in stereo while it does not
apply internal band-limiting filtering, and thus is well suited to all
musical instruments and vocals. Rakarrack is designed for Linux
distributions with Jack Audio Connection Kit.

%description -l pl.UTF-8

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	--enable-docdir=yes \
	--docdir=%{_docdir}/%{name}-%{version}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mkdir html
cp -a doc/help/* html/
%{__rm} html/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PACKAGERS.README README TODO html
%attr(755,root,root) %{_bindir}/rak*
%{_desktopdir}/rakarrack.desktop
%{_datadir}/rakarrack
%{_pixmapsdir}/*.png
%{_mandir}/man1/rakarrack.1*
