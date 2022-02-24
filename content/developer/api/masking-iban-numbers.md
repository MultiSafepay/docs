---
title : "Unmasking IBANs"
meta_title: "Unmasking IBANs - MultiSafepay Docs"
weight: 6
read_more: "."
url: '/developer/unmasking-ibans/'
aliases:
    - /faq/api/masking-iban-numbers
---

International bank account numbers (IBANs) are sensitive data. 

For security reasons, we mask IBANs by default in:

- [`POST` webhook notifications](/developer/webhooks/)
- [`GET /orders/{order_id} responses`](/api/#get-order-details)

When masked, only the last 4 digits of the IBAN are visible, e.g. `*** 1234`.

### Unmasking IBANs

You can still perform most business operations with masked IBANs, e.g. processing refunds.

To unmask IBANs for a specific website, follow these steps:

1. Sign in to your MultiSafepay dashboard.
2. Go to **Settings** > **Website settings**.
3. Click the relevant website.
4. Under **Website functionality**, click the **Unmask IBAN numbers in API requests and responses** toggle.

When unmasked, the full IBAN is displayed, e.g. `NL87ABNA0000001234`.
