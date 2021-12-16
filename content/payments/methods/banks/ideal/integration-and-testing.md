---
title: "Integrating and testing iDEAL"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing iDEAL - MultiSafepay Docs"
short_description: "Options for integrating iDEAL and testing payments"
layout: 'child'
logo: '/logo/Payment_methods/iDEAL.svg'
url: '/payment-methods/ideal/testing/'
aliases:
    - /payment-methods/ideal/ideal-testing
    - /payments/methods/banks/ideal/integration-and-testing/
    - /payments/methods/banks/idealqr/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [iDEAL direct](/api/#ideal---direct), [iDEAL redirect](/api/#ideal---redirect), [iDEAL QR](/api/#ideal-qr) (redirect only) |
| **Ready-made integrations** | iDEAL is supported in all our [ready-made integrations](/integrations/ready-made/), **except** ZenCart. {{< br >}} iDEAL QR (redirect) is supported in: {{< br >}} [Craft Commerce](/craft-commerce/) {{< br >}} [CS-Cart](/cs-cart/) {{< br >}} [Drupal 8](/drupal-8-9/) {{< br >}} [Magento 1](/magento-1/), [Magento 2](/magento-2/) {{< br >}} [Odoo](/odoo/) {{< br >}} [OpenCart](/opencart/) {{< br >}} [PrestaShop 1.7](/prestashop-1-7/) {{< br >}} [Shopware 5](/shopware-5/)  {{< br >}} [VirtueMart](/virtuemart/) {{< br >}} [WooCommerce](/woo-commerce/)  {{< br >}} [X-Cart](/x-cart/) |
| **Checkout options** | [Payment Components](/payment-components/) (embedded) {{< br >}} [Multisafepay payment pages](/payment-pages/) (hosted) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

You can't test iDEAL QR in your test MultiSafepay account. You can only make test payments in your live MultiSafepay account.

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test an iDEAL order

1. To test an iDEAL order, make a [direct](/api/#ideal---direct) or [redirect](/api/#ideal---redirect) API request.
2. If you make a redirect API request, select a bank.
3. On the Test platform page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

### Test cancelling an order

To test cancelling an order:

1. Make a [direct](/api/#ideal---direct) or [redirect](/api/#ideal---redirect) API request.
2. If you make a redirect API request, select a bank. 
3. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
4. Click **Test**.  
  The order status changes to **Void**.

Use the following test scenarios on the Test platform page to test different transaction statuses.

| Status                | Description              |
| --------------------- | ------------------------ |
| **Declined**              | Transaction was declined |
| **Open** **Completed** | Transaction is initialized. After 1 minute, this changes to **Completed**. |
| **Open** **Declined**  | Transaction is initialized. After 1 minute, this changes to **Declined**. |

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