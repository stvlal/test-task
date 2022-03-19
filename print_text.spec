Name:           print_text
Version:        1.0
Release:        1
Summary:        Utility for printing text on the screen

License:        GPL3
URL:            https://github.com/stvlal/test-task
Source0:        %{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
Test task from RAIDIX company


%prep
%setup


%build
make


%install
make install


%files
%defattr(4755,root,root,0755)
/usr/local/bin/printText
