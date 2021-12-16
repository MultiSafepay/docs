---
title: 'Integrating and testing in3'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing in3 - MultiSafepay Docs"
short_description: "Options for integrating in3 and testing payments"
layout: 'child'
logo: '/svgs/in3.svg'
url: '/payment-methods/in3/integration-testing/'
aliases:
    - /payments/methods/billing-suite/in3/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#in3---direct) and [redirect](/api/#in3---redirect) |
| **Ready-made integrations** | in3 (direct) is supported in the following ready-made integrations: {{< br >}} [Craft Commerce](/craft-commerce/) {{< br >}} [Magento 1](/magento-1/) {{< br >}} [OpenCart](/opencart/) {{< br >}} [PrestaShop 1.7](/prestashop-1-7/) {{< br >}} [VirtueMart](/virtuemart/) {{< br >}} [WooCommerce](/woo-commerce/)   |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can't adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test an in3 order


1. To test an in3 order, make a [direct](/api/#in3---direct) or [redirect](/api/#in3---redirect) API request with the following customer details.
| Date of birth    | Postal code | House number |
| ------------------- | ------------------- | ----------------- |
| 01-01-1999 | 1234AB | 1 |

    If you make a redirect API request:
- Enter in the:
    - **Birthdate** field `01-01-1999`.
    - **Phone number** field any phone number.  
- Select your title, and then click **Confirm**.
2. Select the checkbox to accept in3's payment terms and privacy statement, and then click **Afronden**.
3. On the Test platform page, from the **Test scenario** list, select **Completed**.
4. Click **Test**. 
5. On the in3 page, click **Terug naar webshop**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

### Test in3 declining an order   

To test in3 declining an order, make a [direct](/api/#in3---direct) or [redirect](/api/#in3---redirect) API request with the following customer details:

| Date of birth    | Postal code | House number |
| ------------------- | ------------------- | ----------------- |
| 01-01-2000 | 1111AB | 1 |

The order and transaction statuses change to **Declined**.

### Test shipping an order
To test shipping an order, either:

- Make an [update an order](/api/#update-an-order) API request with status `shipped`, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Order status**.

### Receive an invoice

You can only test invoicing in your MultiSafepay live account. To do this, change the order status to **Shipped**.

### Test refunding an order

To test refunding an order:

1. Create an order. 
2. Change the order status to `shipped`.
3. Click **Refund complete order**, and then click **Save item changes**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Completed**.

### Test an API refund

To test refunding an order via the API:

1. Create an order. 
2. Change the order status to `shipped`.
3. Make a [refund with shopping cart](/api/#refund-with-shopping-cart) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Completed**.

**Note:** You can't test cancelling orders.
