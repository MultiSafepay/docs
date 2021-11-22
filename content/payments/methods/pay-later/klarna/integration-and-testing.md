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

To process Klarna payments via our API, see API reference - [Klarna](/api/#klarna).

For the Klarna logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)
- [Klarna's test credentials](https://docs.klarna.com/resources/test-environment/)

**Test a Klarna order**  
1. Send a [direct](/api/#klarna) API request. 
2. On the Klarna page, click **Kopen**.
3. In the **Telefoonnummer** field, enter any mobile number, and then click **Ga verder**.
4. In the **Verificatiecode** field, enter any 6-digit number, and then click **Bevestigen**.  
The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The transaction and order statuses change to **Void**.

**Change the order status**  

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Send an [update an order](/api/#update-an-order) API request, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Order status**.

**Test refunding an order**

To refund an order:

1. Change the order status to **Shipped**.
2. Under **Order summary**, click **Refund order**, or send a [refund with shopping cart](/api/#refund-with-shopping-cart) API request.  
  The transaction status changes to **Completed**.

**Receive an invoice**  

You can only test invoicing in your MultiSafepay live account. To do this, change the order status to **Shipped**.

---

**Note:** You can't test:

- Receiving successful payment notifications from Klarna
- Changing the transaction status from **Uncleared** to **Completed**, except for refunds
- Sending redirect API requests

{{< /details >}}

