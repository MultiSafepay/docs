---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "WeChat Pay - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing WeChat Pay in your ecommerce platform"
layout: 'child'
url: '/payment-methods/wechat-pay/integration-testing/'
aliases:
    - /payments/methods/wallet/wechatpay/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#wechat-pay---direct) and [redirect](/api/#wechat-pay---redirect) |
| **Ready-made integrations** | WeChat Pay is supported in our [PrestaShop 1.7 plugin](/prestashop-1-7/). |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |


To display the QR code for WeChat Pay payments, you have two options:

- Use [redirect](/api/#wechat-pay---redirect) orders, to redirect the customer to a [MultiSafepay payment page](/payment-pages/) where the QR code is displayed under **Payment methods**.

- Use [direct](/api/#wechat-pay---direct) orders, retrieve the `qr_url` and render the QR code in your system to display it to the customer.

## Testing

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

### Test a WeChat Pay order

1. Make a [direct](/api/#wechat-pay---direct) or [redirect](/api/#wechat-pay---redirect) API request.
2. Scan the QR code with a general QR reader (**not** the WeChat app - an error occurs).
3. On the Test platform page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Completed**.

### Test refunding an order

To refund an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
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
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Notes**:  

- You can't test cancelling orders.
- In the live environment, you can't accept refund orders. These are done automatically.

