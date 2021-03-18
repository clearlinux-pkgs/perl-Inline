#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Inline
Version  : 0.86
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/Inline-0.86.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/Inline-0.86.tar.gz
Summary  : 'Write Perl Subroutines in Other Programming Languages'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Inline-license = %{version}-%{release}
Requires: perl-Inline-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Warn)

%description
NAME
Inline - Write Perl Subroutines in Other Programming Languages
VERSION
This document describes Inline version 0.86.

%package dev
Summary: dev components for the perl-Inline package.
Group: Development
Provides: perl-Inline-devel = %{version}-%{release}
Requires: perl-Inline = %{version}-%{release}

%description dev
dev components for the perl-Inline package.


%package license
Summary: license components for the perl-Inline package.
Group: Default

%description license
license components for the perl-Inline package.


%package perl
Summary: perl components for the perl-Inline package.
Group: Default
Requires: perl-Inline = %{version}-%{release}

%description perl
perl components for the perl-Inline package.


%prep
%setup -q -n Inline-0.86
cd %{_builddir}/Inline-0.86

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Inline
cp %{_builddir}/Inline-0.86/LICENSE %{buildroot}/usr/share/package-licenses/perl-Inline/19d40da3bc981cec880a2112a7e2646d480cb6f4
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Inline.3
/usr/share/man/man3/Inline::API.3
/usr/share/man/man3/Inline::FAQ.3
/usr/share/man/man3/Inline::Support.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Inline/19d40da3bc981cec880a2112a7e2646d480cb6f4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Inline.pm
/usr/lib/perl5/vendor_perl/5.32.1/Inline.pod
/usr/lib/perl5/vendor_perl/5.32.1/Inline/API.pod
/usr/lib/perl5/vendor_perl/5.32.1/Inline/FAQ.pod
/usr/lib/perl5/vendor_perl/5.32.1/Inline/Foo.pm
/usr/lib/perl5/vendor_perl/5.32.1/Inline/MakeMaker.pm
/usr/lib/perl5/vendor_perl/5.32.1/Inline/MakeMaker/Changes
/usr/lib/perl5/vendor_perl/5.32.1/Inline/Support.pod
/usr/lib/perl5/vendor_perl/5.32.1/Inline/denter.pm
