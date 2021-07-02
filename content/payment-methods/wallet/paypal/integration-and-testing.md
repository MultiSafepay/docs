---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "PayPal - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing PayPal in your ecommerce platform"
layout: 'child'
aliases:
    - /payment-methods/wallet/paypal/paypal-testing
---

To integrate PayPal using our API, see API Reference – [PayPal](/api/#paypal).

{{< details title="Credentials and testing process" >}}

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

To test PayPal transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in MultiSafepay Test Control as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. Since MultiSafepay does not collect payments on behalf of PayPal, the financial (transaction) status remains **Initialized** and cannot be changed to **Completed**.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined** | Transaction was declined |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted |
| **Initialized**/ **Declined** | Payment blocked by PayPal, then declined |
| **Cancelled** | Transaction was cancelled |

{{< /details >}}
