---
title : "Unmasking IBAN numbers"
meta_title: "FAQ API - Unmasking IBAN numbers - MultiSafepay Docs"
weight: 20
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

International Bank Account Numbers (IBAN) are sensitive data. 

For security reasons, we mask IBAN by default in:

- [POST notifications](/faq/api/notification-url/#post-notification-example)
- [GET /orders/{order_id}](/api/#retrieve-an-order) responses

When masked, only the last 4 digits of the IBAN are visible, e.g. `*** 1234`.

### Unmasking IBAN

You can still perform most business operations with masked IBANs, e.g. processing refunds.
To unmask IBANs for a specific website, email your reasons to your account manager at <sales@multisafepay.com>


Once your account manager has approved your request, follow these steps:

1. In your MultiSafepay Control, go to **Settings** > **Website settings**.
2. Click the relevant website.
3. In the **Website functionality** pane, click the **Unmask IBAN numbers in API requests and responses** toggle.

**Note:** The unmask toggle is always visible, but only active if approved by your account manager.

When unmasked, the full IBAN is displayed, e.g. `NL87ABNA0000001234`.
