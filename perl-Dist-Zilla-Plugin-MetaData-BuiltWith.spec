%define upstream_name    Dist-Zilla-Plugin-MetaData-BuiltWith
%define upstream_version 1.000000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Go overkill and report everything in all name-spaces



License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Readonly)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Dist::Zilla::Role::ConfigDumper)
BuildRequires:	perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:	perl(Dist::Zilla::Util::EmulatePhase)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
Often, distribution authors get module dependencies wrong. So in such
cases, its handy to be able to see what version of various packages they
built with.

Some would prefer to demand everyone install the same version as they did,
but that's also not always necessary.

Hopefully, the existence of the metadata provided by this module will help
users on their end machines make intelligent choices about what modules to
install in the event of a problem.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*




