---
title: "IBANs"
category: 62962dcdbccb9a001d4bbc81
order: 205
hidden: false
parentDoc: 62a206ee0298c80058af3aed
slug: 'ibans'
---

International bank account numbers (IBANs) are sensitive data. For security reasons, we mask them so that only the last 4 digits are visible, e.g. `*** 1234`.

You can still perform most business operations with masked IBANs, e.g. processing refunds.

# How to unmask ibans

To unmask IBANs for a specific site, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Click the relevant site.
4. Under **Website functionality**, click the **Unmask IBAN numbers in API requests and responses** toggle.

When unmasked, the full IBAN is displayed, e.g. `NL87ABNA0000001234`.
<br>

> 💬  Support
> Email <support@multisafepay.com>