---
title: 'Integrating and testing AfterPay'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing AfterPay - MultiSafepay Docs"
short_description: "Options for integrating AfterPay and testing payments"
layout: 'child'
logo: '/logo/Payment_methods/AfterPay.svg'
url: '/payment-methods/afterpay/integration-testing/'
aliases:
    - /payments/methods/billing-suite/afterpay/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#afterpay---direct) and [redirect](/api/#afterpay---redirect) |
| **Ready-made integrations** | Supported in the following ready-made integrations: {{< br >}} [Craft Commerce](/craft-commerce/) {{< br >}} [CS-Cart](/cs-cart/) {{< br >}} [Drupal 8](/drupal-8-9/) {{< br >}} [Magento 1](/magento-1/), [Magento 2](/magento-2/) {{< br >}} [Odoo](/odoo/) {{< br >}} [OpenCart](/opencart/)  {{< br >}} [PrestaShop 1.6](/prestashop-1-6/), [PrestaShop 1.7](/prestashop-1-7/) {{< br >}} [Shopware 5](/shopware-5/), [Shopware 6](/shopware-6/) {{< br >}}  [WooCommerce](/woo-commerce/) {{< br >}}  [X-Cart](/x-cart/)    |
| **Checkout options** | [Payment links](/payment-links/about/) – You can't adjust the lifetime. {{< br >}} [Multisafepay payment pages](/payment-pages/) – Activate at website level in your MultiSafepay account. {{< br >}}   |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

**1.** Request a test API key from AfterPay via either:

- Your implementation ticket with AfterPay, **or**
- Email <sales@afterpay.nl> 

AfterPay shares the test key with MultiSafepay.

**2.** To enable AfterPay in your MultiSafepay test account, email the Integration Team at <integration@multisafepay.com>

### Test an AfterPay order

1. Make a [direct or redirect](/api/#afterpay) API request.
2. If you make a redirect API request, select the checkbox at the bottom of the AfterPay page, and then click **Confirm**.
3. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

2. If you make a redirect API request, select the checkbox at the bottom of the AfterPay page, and then click **Confirm**.
3. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

### Test declining an order  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The transaction and order statuses change to **Void**.

### Test AfterPay rejecting an order

To test AfterPay rejecting an order, in your direct or redirect API request, use the following email address: <rejection@afterpay.nl>  
The transaction and order statuses change to **Declined**.

### Change the order status

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Make an [update an order](/api/#update-an-order) API request, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Order status**.

**Note:** You can't test:  

- Receiving successful payment notifications from AfterPay
- Changing the transaction status from **Uncleared** to **Completed**
- Processing refunds
