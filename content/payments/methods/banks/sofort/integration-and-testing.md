---
title: "Integrating and testing Sofort"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Sofort - MultiSafepay Docs"
short_description: "Options for integrating Sofort and testing payments"
layout: 'child'
logo: '/logo/Payment_methods/SOFORT.svg'
url: '/payment-methods/sofort/integration-testing/'
aliases:
    - /payment-methods/bancontact/sofort-banking-testing
    - /payments/methods/banks/sofort-banking/integration-and-testing/
    - /payments/methods/banks/sofort/integration-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#sofort---direct) and [redirect](/api/#sofort---redirect) |
| **Ready-made integrations** | Supported in all our [ready-made integrations](/integrations/ready-made/). |
| **Checkout options** | [Payment Components](/payment-components/) (embedded) {{< br >}} [Multisafepay payment pages](/payment-pages/) (hosted) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test a Sofort order

1. To test a Sofort order, make a [direct](/api/#sofort---direct) or [redirect](/api/#sofort---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

### Test cancelling an order

To test cancelling an order:

1. Make a [direct](/api/#sofort---direct) or [redirect](/api/#sofort---redirect) API request.
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

### Test an API refund

To test refunding an order via the API:

1. Create an order. 
2. Make a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Note:** In the live environment, you can't accept refund orders. These are done automatically.

