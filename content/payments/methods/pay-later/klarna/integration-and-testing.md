---
title: 'Integrating and testing Klarna'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Klarna - MultiSafepay Docs"
short_description: "Options for integrating Klarna and testing payments"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
url: '/payment-methods/klarna/integration-testing/'
aliases:
    - /payments/methods/billing-suite/klarna/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#klarna---direct) and [redirect](/api/#klarna---redirect) |
| **Ready-made integrations** | Klarna (redirect) is supported in all our [ready-made integrations](/integrations/ready-made/).   |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can't adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

Klarna makes your ecommerce platform available in their merchant portal, where your credentials are generated. Use your credentials to configure the Klarna gateway in your MultiSafepay account. 


For questions about your Klarna integration and the connection with your MultiSafepay account, email the Integration Team at <integration@multisafepay.com>

## Testing 

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)
- [Klarna's test credentials](https://docs.klarna.com/resources/test-environment/)

### Test a Klarna order

1. Make a [direct or redirect](/api/#klarna) API request.
2. On the Klarna page, click **Kopen**.
3. In the **Telefoonnummer** field, enter any mobile number, and then click **Ga verder**.
4. In the **Verificatiecode** field, enter any 6-digit number, and then click **Bevestigen**.  
The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

### Test declining an order  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The transaction and order statuses change to **Void**.

### Change the order status  

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Make an [update an order](/api/#update-an-order) API request, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Order status**.

### Test refunding an order

To refund an order:

1. Change the order status to **Shipped**.
2. Under **Order summary**, click **Refund order**, or make a [refund with shopping cart](/api/#refund-with-shopping-cart) API request.  
  The transaction status changes to **Completed**.

### Receive an invoice  

You can only test invoicing in your MultiSafepay live account. To do this, change the order status to **Shipped**.

**Notes:** You can't test:

- Receiving successful payment notifications from Klarna.
- Changing the transaction status from **Uncleared** to **Completed**, except for refunds.


