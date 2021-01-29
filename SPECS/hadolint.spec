%global git_owner hadolint
%global git_repo hadolint
%global git_archive_file v%{version}.tar.gz
%global git_archive_dir %{git_repo}-%{version}

Name:          %{git_repo}
Version:       1.19.0
Release:       1%{?dist}.harbottle
Summary:       A smarter Dockerfile linter
License:       GPL 3.0
Url:           https://github.com/%{git_owner}/%{git_repo}
Source0:       %{url}/archive/%{git_archive_file}
BuildRequires: glibc-static

%description
A smarter Dockerfile linter that helps you build best practice Docker images.
The linter is parsing the Dockerfile into an AST and performs rules on top of
the AST. It is standing on the shoulders of ShellCheck to lint the Bash code
inside RUN instructions.

%prep
%setup -q -n %{git_archive_dir}

%build
stack build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
stack install --local-bin-path $RPM_BUILD_ROOT%{_bindir}

%files
%license LICENSE
%doc README.md docs/*
%{_bindir}/%{name}

%changelog
* Fri Jan 29 2021 Jamie Curnow <jc@jc21.com> 1.19.0-1
- https://github.com/hadolint/hadolint/releases/tag/v1.19.0
