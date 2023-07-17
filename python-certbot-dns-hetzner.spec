%global srcname certbot-dns-hetzner

Name:           python-%{srcname}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Hetzner DNS authenticator certbot plugin

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-certbot >= 2.0
BuildRequires:  python3-devel
BuildRequires:  python3-dns-lexicon
BuildRequires:  python3-parsedatetime
BuildRequires:  python3-requests
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-tldextract

%global _description %{expand:
Hetzner DNS authenticator certbot plugin}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/certbot_dns_hetzner
%{python3_sitelib}/certbot_dns_hetzner-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog

/builddir/build/BUILDROOT/python-certbot-dns-hetzner-2.0.0-1.fc38.aarch64/usr/lib/python3.11/site-packages/certbot-dns-hetzner-2.0.0-py3.11.egg-info
