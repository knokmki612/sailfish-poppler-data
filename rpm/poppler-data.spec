Name:       poppler-data
Version:    0.4.7
Release:    1
Summary:    Encoding data for the poppler PDF rendering library
License:    MIT
Source:     %{name}.tar.gz
URL:        https://poppler.freedesktop.org
BuildArch:  noarch

%description
This package provides the CMap tables required to display PDF documents containing CJK characters with libpoppler. They were previously provided by the packages cmap-adobe-{cns1,gb1,japan1,japan2,korea1} and gs-cjk-resource.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
make install prefix=/usr DESTDIR=%{buildroot}

%pre

%preun

%files
/usr/share/pkgconfig/poppler-data.pc
/usr/share/poppler/
