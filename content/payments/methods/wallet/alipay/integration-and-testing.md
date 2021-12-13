---
title: "Integrating and testing Alipay"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Alipay - MultiSafepay Docs"
short_description: "Options for integrating Alipay and testing payments"
layout: 'child'
url: '/payment-methods/alipay/integration-testing/'
aliases:
    - /payment-methods/wallet/paypal/paypal-testing
    - /payments/methods/wallet/alipay/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#alipay---direct) and [redirect](/api/#alipay---redirect)  |
| **Ready-made integrations** | Alipay (direct) is supported in all our [ready-made integrations](/integrations/ready-made/) **except** PrestaShop 1.6, OsCommerce, and Zen Cart.   |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

### Test an Alipay order

1. Make a [direct](/api/#alipay---direct) or [redirect](/api/#alipay---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

### Test cancelling an order

To test cancelling an order:

1. Make a [direct](/api/#alipay---direct) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Initialized**.
4. In your MultiSafepay test account, under **Order summary**, click **Cancel**.
5. In the **Add transaction comment** field, add a comment, and then click **Ok**.  
  The order status changes to **Void**.

### Test refunding an order

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
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

**Notes**:  

- You can't test:
    - Refunding via the API.
    - Alipay declining transactions.
- In the live environment, you can't accept refund orders. These are done automatically.

