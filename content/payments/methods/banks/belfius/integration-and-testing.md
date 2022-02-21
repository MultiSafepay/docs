---
title: "Integrating and testing Belfius"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Belfius - MultiSafepay Docs"
short_description: "Options for integrating Belfius and testing payments"
layout: 'child'
logo: '/logo/Payment_methods/belfius.svg'
url: '/payment-methods/belfius/integration-testing/'
aliases:
    - /payment-methods/belfius/belfius-testing
    - /payments/methods/banks/belfius/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#belfius---direct) and [redirect](/api/#belfius---redirect) |
| **Ready-made integrations** | Supported in all our [ready-made integrations](/integrations/ready-made/), **except** OsCommerce and ZenCart. |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test a Belfius order

1. To test a Belfius order, make a [direct](/api/#belfius---direct) or [redirect](/api/#belfius---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

### Test cancelling an order

To test cancelling an order:

1. Make a [direct](/api/#belfius---direct) or [redirect](/api/#belfius---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.

### Test refunding an order

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test dashboard, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Notes:** 

- You can't test refunding via the API.
- In the live environment, you can't accept refund orders. These are done automatically.
