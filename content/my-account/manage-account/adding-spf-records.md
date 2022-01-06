---
title : "Adding SPF records for MultiSafepay emails"
weight: 13
meta_title: "Adding SPF records - MultiSafepay Docs"
read_more: "."
url: '/my-account/adding-spf-records/'
aliases:
    - /faq/general/add-spf-dns-records
    - /faq/general/adding-spf-dns-records/
    - /developer/general/adding-spf-dns-records/
---

Sender Policy Framework (SPF) records let you specify who is authorized to send emails on your domain's behalf. Receiving email servers can check the SPF record to verify the sender. Using an SPF record prevents emails sent by MultiSafepay on your behalf from being marked as spam.

## Adding an SPF record

1. Through your hosting provider, domain registrar, or DNS provider, create a DNS TXT record that is named after your domain. For example: `example.com`

2. Add either of the following entries to your TXT record containing `v=spf1` and including at least one of the following:
    - `ip4:213.189.0.0/23`
    - `ip4:185.99.128.0/22`
    - `include:spf.multisafepay.com`

    **Note:** The total number of includes permitted is 10, including mx records (if listed).

    You have successfully created an SPF record.

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

## See also
[Setting up DKIM email authentication](/my-account/setting-up-dkim/)