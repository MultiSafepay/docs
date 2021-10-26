---
title: 'Integration and testing'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Klarna - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Klarna in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
url: '/payment-methods/klarna/integration-testing/'
aliases:
    - /payments/methods/billing-suite/klarna/integration-and-testing/
---

Klarna makes your ecommerce platform available in the MultiSafepay partner portal, where your credentials are generated. Use your credentials to configure the Klarna gateway in your MultiSafepay account. 

To process Klarna payments via our API, see API reference - [Klarna](/api/#klarna).

For questions about your Klarna integration and the connection with your MultiSafepay account, email the Integration Team at <integration@multisafepay.com>

For the Klarna logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials:

- [API key](/tools/multisafepay-control/get-your-api-key/)
- [Klarna's test credentials](https://docs.klarna.com/resources/test-environment/)

**Test a Klarna transaction**  
1. Send a [direct or redirect](/api/#klarna) API request. For more information, see [difference between direct and redirect API requests](/developer/api/difference-between-direct-and-redirect).
2. On the Klarna page, click **Kopen**.
3. Enter any mobile number in the **Telefoonnummer** field. Click **Ga verder**.
4. Enter any six digit number in the **Verificatiecode** field. Click **Bevestigen**.
5. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in **Order Summary** click **Decline**. The transaction and order status changes to **Void**.

**Change the order status**  

You can change the order status to: **Shipped** or **Cancelled**.
To change the order status, either:  
- Send an [Update an order](/api/#update-an-order) API request, or 
- In your MultiSafepay test account, go to **Order Summary**. Click **Order status**.

**Test refunding an order**

To refund an order:
  1. Change the order status to **Shipped**.
  2. In **Order Summary**, click **Refund order**. The transaction status changes to **Completed**.

**Receive an invoice**  

Testing the invoice process is possible only in your live MultiSafepay account. To do this, change the order status to **Shipped**.

---

**Note:** You can't test:
- Receiving a successful payment notification from Klarna. 
- Changing the transaction status from **Uncleared** to **Completed**, unless you are testing a refund.

{{< /details >}}

