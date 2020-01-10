Summary: Utility for visualizing block layer IO patterns and performance
Name: iowatcher
Version: 1.0
Release: 2%{?dist}
License: GPLv2
Group: Development/System
BuildRequires: librsvg2-devel
Requires: blktrace
Requires: sysstat
Requires: theora-tools
Source: http://www.kernel.org/pub/linux/kernel/people/mason/iowatcher/%{name}-%{version}.tar.bz2
URL: http://masoncoding.com/iowatcher/

%description
iowatcher generates graphs from blktrace runs to help visualize IO patterns and
performance as SVG images or movies. It can plot multiple blktrace runs
together, making it easy to compare the differences between different benchmark
runs.

You should install the iowatcher package if you need to visualize detailed
information about IO patterns.

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -Wno-unused-result"

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} install
install -Dpm 0644 iowatcher.1 %{buildroot}%{_mandir}/man1/iowatcher.1

%files
%doc README COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Andrew Price <anprice@redhat.com> - 1.0-1
- Package up the first official release
- Honor build flags with optflags
- Improve the files list

* Fri Jan 18 2013 Andrew Price <anprice@redhat.com> - 0.0-1.20130117git26d4e95
- Further improve the versioning
- Preserve timestamp on man page
- Remove BuildRoot, the clean and defattr sections and don't clean buildroot
- Install to DESTDIR
- Update Source and add a comment on how the tarball was generated
- Use _smp_mflags in build
- Thanks to Eduardo Echeverria for reviewing the package

* Thu Jan 17 2013 Andrew Price <anprice@redhat.com> - 0-0.1.git26d4e95
- Use a better versioning scheme

* Thu Jan 17 2013 Andrew Price <anprice@redhat.com> - 0.0.0.git26d4e95-1
- Added man page
- Added missing Requires
- Use _bindir

* Wed Dec 19 2012 Andrew Price <anprice@redhat.com> - 0.0.0.git619d3c2-1
- Initial packaging
