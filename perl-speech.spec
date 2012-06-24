#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Speech
%define	pnam	speech_pm
Summary:	Speech::Synthesiser - speech output for Perl
Summary(pl):	Speech::Synthesiser - wyj�cie mowy dla Perla
Name:		perl-speech
Version:	1.0
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}_%{version}.tgz
# Source0-md5:	49666e75d6014c9f521a582fb0f531ce
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	festival
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# note: there is only festival interface for now, so it isn't separated
# (and Requires: festival is in main package)

%description
This is a simple Perl extension module which provides a way for perl
programs to speak using a speech synthesiser. The interface is
intended to allow any synthesiser to be plugged in. An implementation
using the festival speech synthesiser is included.

%description -l pl
To jest prosty modu� Perla udost�pniaj�cy programom mo�liwo�� m�wienia
przy u�yciu syntezatora mowy. Interfejs jest zaprojektowany z my�l� o
mo�liwo�ci u�ycia dowolnego syntezatora. Do��czona jest implementacja
u�ywaj�ca syntezatora festival.

%prep
%setup -q -n %{pnam}_%{version}
# workaround and fixes for broken file locations
%{__perl} -pi -e 's/Speech::Synthesiser/Speech/' Makefile.PL
%{__perl} -pi -e 's/Speech::Speech::Festival/Speech::Festival/' Speech/Festival.pm
%{__perl} -pi -e 's/use Festival/use Speech::Festival/' test.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.txt
%{perl_vendorlib}/Audio/*.pm
%{perl_vendorlib}/Speech/*.pm
%{perl_vendorlib}/Speech/Festival
%{_mandir}/man3/*
