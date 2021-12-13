---
title: "Integrating and testing American Express"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing American Express - MultiSafepay Docs"
short_description: "Options for integrating American Express and testing payments"
layout: 'child'
aliases:
    - /payment-methods/credit-and-debit-cards/american-express/american-express-testing
    - /payment-methods/credit-and-debit-cards/credit-card-payment-page
---
## Integration

| | |
|---|---|
| **API** | See API reference – [American Express redirect](/api/#american-express). {{< br >}} **Bundled credit cards** {{< br >}} You can also bundle multiple credit cards together on your MultiSafepay credit card payment page. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits. {{< br >}} See API reference – [Credit cards](/api/#credit-cards). |
| **Ready-made integrations** | American Express (redirect) is supported in all our [ready-made integrations](/integrations/ready-made/).   |
| **Checkout options** | [Payment Components](/payment-components/) (embedded) {{< br >}} [Multisafepay payment pages](/payment-pages/) (hosted) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test an American Express order

1. Make a [redirect](/api/#american-express) API request.
2. On the payment page:
    - In the **Card number** field, enter `378282246310005`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different transaction statuses.

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 374200000000004| **Declined**  | Transaction was declined |
| 378734493671000| **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Void**. |

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

**Note:** In the live environment, you can't accept refund orders. These are done automatically.



