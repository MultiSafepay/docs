---
title : "Unmasking IBAN numbers"
meta_title: "FAQ API - Unmasking IBAN numbers - MultiSafepay Docs"
weight: 20
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
---

International Bank Account Numbers (IBAN) are sensitive data. 

For security reasons, we mask IBAN by default in:

- [POST notifications](/faq/api/notification-url/#post-notification-example)
- [GET /orders/{order_id}](/api/#retrieve-an-order) responses

When masked, only the last 4 digits of the IBAN are visible, e.g. `*** 1234`.

### Unmasking IBAN

You can still perform most business operations with masked IBAN, e.g. processing refunds.

To unmask IBAN for a specific website, follow these steps:

1. In your MultiSafepay Control, go to **Settings** > **Website settings**.
2. Click the relevant website.
3. Under **Website functionality**, click the **Unmask IBAN numbers in API requests and responses** toggle.

When unmasked, the full IBAN is displayed, e.g. `NL87ABNA0000001234`.
