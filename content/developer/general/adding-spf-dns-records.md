---
title : "Adding SPF DNS records for MultiSafepay emails"
weight: 9
meta_title: "Adding SPF DNS records - MultiSafepay Docs"
read_more: "."
aliases:
    - /faq/general/add-spf-dns-records
    - /faq/general/adding-spf-dns-records/
---

Sender Policy Framework (SPF) records let users specify which servers can send emails on behalf of their domain name system (DNS). Receiving servers can check the SPF record and decide to:

- Accept the email.
- Mark it as unsafe.
- Refuse the email.

MultiSafepay uses an SPF record to prevent our emails being marked as spam.

## Accepting MultiSafepay emails

To tell your server to accept MultiSafepay emails, add either of the following entries to your TXT record containing `v=spf1` and include `spf.multisafepay.com`:

- ip4:213.189.0.0/23
- ip4:185.99.128.0/22

**Notes:** 

- The filename should be the name of your website. In the examples below, this is given as `example.com`.
- The total number of includes permitted is 10, including mx records (if listed).

## Examples

### Original TXT record
```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 ~all"
```

### Modified TXT record example 1
```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 ip4:213.189.0.0/23 ip4:185.99.128.0/22 ~all"
```

### Modified TXT record example 2
```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 include:spf.multisafepay.com ~all"
```