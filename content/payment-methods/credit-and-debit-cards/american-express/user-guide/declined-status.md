---
title : "Declined status"
meta_title: "American Express - Declined status - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 20
aliases:
    - /payment-mthods/credit-and-debit-cards/american-express/american-express-status-what-does-this-mean-
---

The table below shows possible reasons for the **Declined** reasons, which may appear in the relevant **Transaction details** page in your MultiSafepay account. 

Only the customer can contact their credit card issuer to find out the specific reason.

| Transaction status | Reason | Description |
|------- |----------|---------|
| Declined | Transaction declined by MultiSafepay | Our automated fraud filter declined the transaction. {{< br >}} Email the Support Team at <support@multisafepay.com> |
| Declined | Do not honor | The reason is not shared with MultiSafepay. {{< br >}} Only the cardholder can ask the issuer. |
| Declined | 3D authorisation cancelled | The [3D Secure](/faq/general/glossary/#3d-secure) verification was incomplete or couldn't be validated. |
| Declined | Expired card | The credit card has expired. |
| Declined | Insufficient funds | The customer has insufficient credit on their card to complete the payment. |
| Declined | Merchant only accepts 3D Secure-verified cards | Email requests to accept non-3D Secure verified cards to the Risk Team at <risk@multisafepay.com>  |

For any questions, email the Support Team at <support@multisafepay.com>