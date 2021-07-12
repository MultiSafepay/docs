---
title : "Adding SPF DNS records for MultiSafepay emails"
weight: 9
meta_title: "General developer information - Adding SPF DNS records - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/general/add-spf-dns-records
    - /faq/general/adding-spf-dns-records/
---

Sender Policy Framework (SPF) records let users specify which servers can send emails on behalf of their domain name system (DNS). Receiving servers can check the SPF record and decide to:

- Let the email through.
- Mark it as unsafe.
- Refuse it altogether.

MultiSafepay uses an SPF record to prevent our emails being marked as spam.

You can add the following _TXT record_ to the [DNS](https://nl.wikipedia.org/wiki/Domain_Name_System) of your customers:

- v = spf1 ip4: 213.189.0.0/23 mx

- v = spf1 ip4: 185.99.128.0/22 mx

**Note:** The filename should be the name of your website.
