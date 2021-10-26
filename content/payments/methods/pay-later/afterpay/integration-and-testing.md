---
title: 'Integration and testing AfterPay'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integration and testing AfterPay - MultiSafepay Docs"
short_description: "Integration and testing AfterPay in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/AfterPay.svg'
url: '/payment-methods/afterpay/integration-testing/'
aliases:
    - /payments/methods/billing-suite/afterpay/integration-and-testing/
---

To process AfterPay payments via our API, see API reference – [AfterPay](/api/#afterpay).

For the AfterPay logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View testing process" >}}

To enable AfterPay in your MultiSafepay test account, email the Integration Team at <integration@multisafepay.com>

To get a test AfterPay API key, you can either:

- Request one in your implementation ticket with AfterPay, or
- Email <sales@afterpay.nl> 

**Test an AfterPay transaction**

1. Send a [direct or redirect](/api/#afterpay) API request. For more information, see [difference between direct and redirect API requests](/developer/api/difference-between-direct-and-redirect).
2. If you send a redirect API request, select the checkbox at the bottom of the AfterPay page and click **Bevestig**.
3. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in **Order Summary** click **Decline**. The transaction and order status changes to **Void**.

**Test order rejection**  

To test AfterPay rejecting an order, use the following email address: <rejection@afterpay.nl> in your direct or redirect API request.
The transaction and order status changes to **Declined**.

**Change the order status**  

You can change the order status to: **Shipped** or **Cancelled**.
To change the order status, either:  
- Send an [Update an order](/api/#update-an-order) API request, or 
- In your MultiSafepay test account, go to **Order Summary**. Click **Order status**.

---

**Note:** You can't test: 
- Receiving a successful payment notification from AfterPay. 
- Changing the transaction status from **Uncleared** to **Completed**. 
- Processing a refund. 
{{< /details >}}