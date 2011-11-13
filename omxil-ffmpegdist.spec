Summary:	Distributable FFMpeg component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Rozprowadzalny komponent FFMpeg dla implementacji Bellagio OpenMAX IL
Name:		omxil-ffmpegdist
Version:	0.1
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxffmpegdist-%{version}.tar.gz
# Source0-md5:	6f2ff464bd62e725e42596fe705109fc
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.5
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
Distributable FFmpeg component is a component for Bellagio OpenMAX IL
that uses free parts of FFMpeg libraries to decode/encode audio and
video.

It can:
- decode MP3, Ogg Vorbis, AAC, g726 audio
- encode MP3, AAC, g726 audio
- decode MPEG4, AVC video
- encode MPEG4 video
- parse 3GP containers
- perform video colorspace conversions

%description -l pl.UTF-8
Rozprowadzalny komponent FFMpeg to komponent dla implementacji
Bellagio OpenMAX IL, wykorzystujący wolnodostępne elementy bibliotek
FFMpeg to dekodowania i kodowania dźwięku i obrazu.

Komponent ten potrafi:
- dekodować dźwięk MP3, Ogg Vorbis, AAC, g726
- kodować dźwięk MP3, AAC, g726
- dekodować obraz MPEG4, AVC
- kodować obraz MPEG4
- analizować kontenery 3GP
- wykonywać konwersję przestrzeni kolorów obrazu

%prep
%setup -q -n libomxffmpegdist-%{version}

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxffmpegdist.so*
