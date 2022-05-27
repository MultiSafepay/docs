---
title : "Unmasking IBANs"
meta_title: "Unmasking IBANs - MultiSafepay Docs"
weight: 8
read_more: "."
url: "/account/unmasking-ibans/"
aliases:
    - /developer/api/masking-iban-numbers/
    - /faq/api/masking-iban-numbers
    - /developer/unmasking-ibans/
---

International bank account numbers (IBANs) are sensitive data. For security reasons, we mask them so that only the last 4 digits are visible, e.g. `*** 1234`.

You can still perform most business operations with masked IBANs, e.g. processing refunds.

### Unmasking IBANs

To unmask IBANs for a specific website, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Click the relevant website.
4. Under **Website functionality**, click the **Unmask IBAN numbers in API requests and responses** toggle.

When unmasked, the full IBAN is displayed, e.g. `NL87ABNA0000001234`.
