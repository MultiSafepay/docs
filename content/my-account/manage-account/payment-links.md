---
title: 'Payment links'
weight: 7
meta_title: "Payment links - MultiSafepay Docs"
layout: 'single'
logo: '/svgs/External link.svg'
short_description: 'Generate payment links via our API or in your MultiSafepay dashboard.'
url: '/account/payment-links/'
read_more: "."
aliases:
    - /tools/payment-link/payment-link-api/
    - /payments/checkout/payment-link/
    - /payment-links/cancellation/
    - /payment-links/disabling-payment-links-for-payment-methods/
    - /payment-links/disabling-links/
    - /payment-links/cancelling-cloning-payment-links/
    - /tools/payment-link/manually-generating-a-payment-link/
    - /tools/payment-link/payment-link-api/
    - /tools/multisafepay-control/manually-generated-payment-link
    - /tools/multisafepay-control/generating-and-disabling-payment-links
    - /account/multisafepay-account/generating-and-disabling-payment-links/
    - /payments/checkout/payment-link/
    - /payment-links/generating-links/
    - /payment-links/about/
---

You can manually generate a link to a [payment page](/payment-pages/) to pass to a customer to complete payment. Use cases include:

- A customer wants to adjust an existing order and instead of starting over with a new order.
- You need to create a transaction for a manually generated order.
- MultiSafepay collects a payment for an amount that doesn't match any order. If you accept the payment, you need to manually generate a payment link and email it to <support@multisafepay.com>
- A [Bank Transfer](/payment-methods/bank-transfer/) transaction has expired.

{{< details title="Payment methods" >}}

**All** payment methods are supported. 

The [payment page](/payment-pages/) displays **all** payment methods activated for the relevant website. If&nbsp;you want to display specific payment methods, you need to create a new website profile with only the relevant methods activated. 

{{< /details >}}

{{< details title="Link lifetime" >}}

The lifetime of a payment link is how long it remains active for the customer to access the payment page and complete payment. The default is 30 days. 

You can adjust the lifetime for some payment methods:

| Adjustable | Non-adjustable |
|---|---|
| Banking methods, except SEPA Direct Debit | SEPA Direct Debit |
| Gift cards | Edenred, Paysafecard |
| Wallets | PayPal – Links are valid for 14 days. The lifetime is set by PayPal. |
| Credit cards |  |

To set or adjust the lifetime, see API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder): `days_active` parameter.

**Note:** This is different to [transaction expiration times per payment method](https://docs-api.multisafepay.com/reference/transaction-expiration). 

{{< /details >}}

{{< details title="Number of customer attempts" >}} 
The customer can open the link to the payment page up to 20 times, after which the link is disabled.

Each attempt creates a new transaction. If the customer completes payment in one of these transactions, the [status](/about-payments/multisafepay-statuses/) of the other transactions remains **Initialized** until they expire.

{{< /details >}}

## Generating payment links

You can generate payment links via:

{{< details title="Dashboard: New transactions" >}}

To generate a payment link for a new transaction, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Click **New payment link**.
4. From the **Site** list, select the relevant website.
5. Under **Amount**, select the currency from the list, and then enter the whole value and cents.
6. In the **Order ID** field, enter the order ID from your webshop.  
**Note:** The order ID for every payment link must be unique.
7. In the **Description** field, enter a description of the order. 
8. In the **Link expiration (days)** field, enter the number of days for the link to remain active. Default: 30 days.
9. To send [Second Chance emails](/features/second-chance/), select the **Second chance email** check box. 
10. Optionally, enter the customer's:  
    - **First name** and **Last name**
    - **Email address**
    - **Country**
    - **Language**
11. To include additional information, in the top-right corner, click **Advanced mode** to display more fields. 
12. Click **Generate payment link**.
13. In the green bar that appears, copy the link from the green bar and pass it to the customer.

{{< /details >}}

{{< details title="Dashboard: Existing transactions" >}}

To generate a payment link for an existing transaction, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Click on the relevant transaction.
4. In the **Transaction details** page, under **Order summary**, click **Payment link** > **Duplicate this order**.

**Note:** The order ID must be unique.

{{< /details >}}

## Viewing payment links

For an overview of all payment links:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.

{{< details title="Payment link statuses" >}} 

| Status | Description |
|---|---|
| Active | The customer hasn't paid yet.  | 
| Completed | The customer has paid. | 
| Cancelled | You cancelled the link.| 
| Expired | The link lifetime has expired.  | 

{{< /details >}}

## Cloning payment links

If you need to generate multiple payment links, you can speed up the process by copying existing links.

{{< details title="Clone a payment link" >}}
To generate a copy of an existing payment link: 

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Next to the relevant payment link, click the blue copy icon.  
A new link generator window opens with the same details prefilled.  
4. Click **Generate payment link**.

{{< /details >}}

## Cancelling payment links

You can cancel a payment link in your dashboard, or see API reference – [Update or cancel an order](https://docs-api.multisafepay.com/reference/updateorder).

{{< details title="Cancel a payment link" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Next to the relevant payment link, click the red cross icon.  
The status changes to **Cancelled**. 

{{< /details >}}

## Support

Email <integration@multisafepay.com>
