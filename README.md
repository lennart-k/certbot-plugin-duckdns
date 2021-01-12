# Certbot DuckDNS Plugin

This plugin is based on [certbot-dns-ispconfig](https://github.com/m42e/certbot-dns-ispconfig) and automates the DNS challenge for DuckDNS domains

## Installation

```
pip install git+https://github.com/lennart-k/certbot-plugin-duckdns
```

## Example

```
certbot certonly \
    --authenticator duckdns \
    --duckdns-token=TOKEN \
    --agree-tos \
    --preferred-challenges=dns
    -d "qed.duckdns.org" \
```
