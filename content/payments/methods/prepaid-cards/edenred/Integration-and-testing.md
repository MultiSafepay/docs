---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Edenred - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Edenred in your ecommerce platform"
layout: 'child'
url: '/payment-methods/edenred/integration-testing/'
aliases:
    - /payments/methods/prepaid-cards/edenred/integration-and-testing/
---

To process Edenred voucher payments via our API, see API reference – [Edenred](/api/#edenred).

By default, all activated Edenred vouchers display at checkout. You can specify which Edenred vouchers to display per transaction using our API, see API reference - [Specify vouchers](/api/#specify-vouchers).

For the Edenred voucher logos, see MultiSafepay GitHub - [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an Edenred order**

1. Send a [redirect](/api/#edenred) API request.
2. On the payment page, click **Add discount**.
3. From the **Test scenario** list, select the relevant discount, and then click **Test**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}