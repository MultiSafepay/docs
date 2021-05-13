---
title : "Unmasking IBAN numbers"
meta_title: "FAQ API - Unmasking IBAN numbers - MultiSafepay Docs"
weight: 20
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

International Bank Account Numbers (IBAN) are sensitive data. 

By default, we mask IBAN in:

- [POST notifications](/faq/api/notification-url/#post-notification-example)
- [GET /orders/{order_id}](/api/#retrieve-an-order) responses

Masked IBAN only display the last 4 digits of the number, e.g. `*** 1234`.

### How to unmask

To unmask IBAN at a website level, reach out to your account manager to discuss why you need to unmask IBAN. You can perform regular business operations like performing refunds without the need of unmasking IBAN. 


Once your account manager has approved the unmasking of IBAN, follow these steps: 

1. In your MultiSafepay Control, go to **Settings** > **Website settings**.
2. Click the relevant website.
3. Under the **Website functionality** pane, click the **Unmask IBAN numbers in API requests and responses** toggle.

**Note:** The unmask toggle is always visible, however, without the approval of your account manager, it has no effect.

Unmasked IBAN display the full number, e.g. `NL87ABNA0000001234`.
