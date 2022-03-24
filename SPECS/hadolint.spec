%global debug_package %{nil}
%global git_owner hadolint
%global git_repo hadolint
%global git_archive_file v%{version}.tar.gz
%global git_archive_dir %{git_repo}-%{version}

Name:          %{git_repo}
Version:       2.9.3
Release:       1%{?dist}
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
%doc README.md docs/*.md
%{_bindir}/%{name}

%changelog
* Fri Mar 25 2022 Jamie Curnow <jc@jc21.com> 2.9.3-1
- https://github.com/hadolint/hadolint/releases/tag/v2.9.3

* Tue Mar 22 2022 Jamie Curnow <jc@jc21.com> 2.9.2-1
- https://github.com/hadolint/hadolint/releases/tag/v2.9.2

* Thu Mar 17 2022 Jamie Curnow <jc@jc21.com> 2.9.1-1
- https://github.com/hadolint/hadolint/releases/tag/v2.9.1

* Tue Nov 30 2021 Jamie Curnow <jc@jc21.com> 2.8.1-1
- https://github.com/hadolint/hadolint/releases/tag/v2.8.1

* Fri Aug 13 2021 Jamie Curnow <jc@jc21.com> 2.6.1-1
- https://github.com/hadolint/hadolint/releases/tag/v2.6.1

* Mon Jul 5 2021 Jamie Curnow <jc@jc21.com> 2.6.0-1
- https://github.com/hadolint/hadolint/releases/tag/v2.6.0

* Mon Jun 14 2021 Jamie Curnow <jc@jc21.com> 2.5.0-1
- https://github.com/hadolint/hadolint/releases/tag/v2.5.0

* Mon May 17 2021 Jamie Curnow <jc@jc21.com> 2.4.1-1
- https://github.com/hadolint/hadolint/releases/tag/v2.4.1

* Fri May 7 2021 Jamie Curnow <jc@jc21.com> 2.4.0-1
- https://github.com/hadolint/hadolint/releases/tag/v2.4.0

* Tue Apr 27 2021 Jamie Curnow <jc@jc21.com> 2.3.0-1
- https://github.com/hadolint/hadolint/releases/tag/v2.3.0

* Tue Apr 20 2021 Jamie Curnow <jc@jc21.com> 2.2.0-1
- https://github.com/hadolint/hadolint/releases/tag/v2.2.0

* Sat Apr 3 2021 Jamie Curnow <jc@jc21.com> 2.1.0-1
- https://github.com/hadolint/hadolint/releases/tag/v2.1.0

* Thu Mar 25 2021 Jamie Curnow <jc@jc21.com> 2.0.0-1
- https://github.com/hadolint/hadolint/releases/tag/v2.0.0

* Tue Mar 2 2021 Jamie Curnow <jc@jc21.com> 1.23.0-1
- https://github.com/hadolint/hadolint/releases/tag/v1.23.0

* Tue Feb 9 2021 Jamie Curnow <jc@jc21.com> 1.22.1-1
- https://github.com/hadolint/hadolint/releases/tag/v1.22.1

* Mon Feb 8 2021 Jamie Curnow <jc@jc21.com> 1.22.0-1
- https://github.com/hadolint/hadolint/releases/tag/v1.22.0

* Tue Feb 2 2021 Jamie Curnow <jc@jc21.com> 1.21.0-1
- https://github.com/hadolint/hadolint/releases/tag/v1.21.0

* Fri Jan 29 2021 Jamie Curnow <jc@jc21.com> 1.19.0-1
- https://github.com/hadolint/hadolint/releases/tag/v1.19.0

