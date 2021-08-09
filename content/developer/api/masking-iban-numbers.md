---
title : "Unmasking IBAN numbers"
meta_title: "API Documentation - Unmasking IBAN numbers - MultiSafepay Docs"
weight: 20
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/api/masking-iban-numbers
---

International bank account numbers (IBANs) are sensitive data. 

For security reasons, we mask IBANs by default in:

- [`POST` notifications](/developer/api/notification-url/#post-notification-example)
- [`GET /orders/{order_id} responses`](/api/#retrieve-an-order)

When masked, only the last 4 digits of the IBAN are visible, e.g. `*** 1234`.

### Unmasking IBANs

You can still perform most business operations with masked IBANs, e.g. processing refunds.

To unmask IBANs for a specific website, follow these steps:

1. Sign in to your MultiSafepay account.
2. Go to **Settings** > **Website settings**.
3. Click the relevant website.
4. Under **Website functionality**, click the **Unmask IBAN numbers in API requests and responses** toggle.

When unmasked, the full IBAN is displayed, e.g. `NL87ABNA0000001234`.
