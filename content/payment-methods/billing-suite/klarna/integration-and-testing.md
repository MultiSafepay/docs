---
title: 'Integration and testing'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Klarna - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing Klarna in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
---

Klarna makes your ecommerce platform available in the MultiSafepay partner portal, where your credentials are generated. Use your credentials to configure the Klarna gateway in your MultiSafepay Control. 

To integrate Klarna using our API, see API Reference - [Klarna](/api/#klarna).

For questions about your Klarna integration and the connection with MultiSafepay Control, email the Integration Team at <integration@multisafepay.com>

{{< details title="View credentials and testing process" >}}

Test credentials:

- [API key](/tools/multisafepay-control/get-your-api-key/)
- [Klarna's test credentials](https://developers.klarna.com/en/gb/kco-v3/test-credentials)

To test Klarna transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay Test Control.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test control so you can't change the transaction (financial) status to **Completed**. Alternatively, in your live MultiSafepay Control, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in Klarna.

For more information about integrating Klarna with MultiSafepay, see Payment methods – [Klarna](/payment-methods/billing-suite/klarna).

{{< /details >}}

