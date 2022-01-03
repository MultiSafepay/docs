---
title: 'Payment links'
weight: 50
meta_title: "Payment links - MultiSafepay Docs"
layout: 'single'
logo: '/svgs/External link.svg'
short_description: 'Generate payment links via our API or in your MultiSafepay account.'
url: '/payment-links/'
aliases:
    - /tools/payment-link/manually-generating-a-payment-link/
    - /tools/payment-link/payment-link-api/
    - /tools/multisafepay-control/manually-generated-payment-link
    - /tools/multisafepay-control/generating-and-disabling-payment-links
    - /account/multisafepay-account/generating-and-disabling-payment-links/
    - /payments/checkout/payment-link/
    - /payment-links/about/
    - /payment-links/cancellation/
    - /tools/multisafepay-control/generating-and-disabling-payment-links
    - /payment-links/disabling-payment-links-for-payment-methods/
    - /payment-links/disabling-links/
---
You can manually generate a link to a [MultiSafepay payment page](/payment-pages/) to send to a customer to complete payment. 

### Use cases 

- A customer wants to adjust an existing order and instead of starting over with a new order.
- You need to create a transaction for a manually generated order.
- MultiSafepay receives a payment from a customer for an amount that doesn't match any order. If you accept the payment, you need to manually generate a payment link and email it to MultiSafepay.
- A [Bank Transfer](/payment-methods/bank-transfer/) payment link has expired.

### Payment methods

All payment methods are supported except Paysafecard, in3, Betaal per Maand, Pay After Delivery, Klarna, and AfterPay. 

The payment page displays **all** payment methods activated for the relevant website. If&nbsp;you want to display specific payment methods, you need to create a new website profile with only the relevant methods activated. 

### Lifetimes

The lifetime of a payment link is how long it remains valid for the customer to access the payment page and complete payment. The default is 30 days. 

To set or adjust the lifetime, see API reference – [Adjust payment link lifetimes](/api/#adjust-payment-link-lifetimes).

**Note:** This is separate from the [transaction session expiry period](/developer/transaction-session-expiry/) set by each payment method. 

### Attempts 
The customer can open the link to the payment page up to 20 times, after which the link is disabled.

Each attempt creates a new transaction. If the customer completes payment in one of these transactions, all the others remain **Initialized** until they expire.

## Generating payment links

### In your MultiSafepay account

{{< details title="New transaction" >}}

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
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
    - **First name** and - **Last name**
    - **Email address**
    - **Country**
    - **Language**
11. To include additional information, in the top-right corner, click **Advanced mode** to display more fields. 
12. Click **Generate payment link**.
13. In the green bar that appears, copy the link from the green bar and pass it to the customer.

{{< /details >}}

{{< details title="Existing transaction" >}}

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Click on the relevant transaction.
4. In the **Transaction details** page, under **Order summary**, click **Payment link** > **Duplicate this order**.

**Note:** The order ID must be unique.

{{< /details >}}

{{< details title="From your MultiSafepay app" >}}

To generate a payment link from your MultiSafepay app, follow these steps:

1. Go to **Tools** > **Payment link generator**.
2. Fill in the required fields.
3. Click **Generate payment link**.
4. Save the QR code generated to your device and then send it to the customer.   
When the customer scans the QR code, they are directed to a pre-filled MultiSafepay payment page to complete payment.

{{< /details >}}

### From your backend

For some of our [ready-made integrations](/integrations/ready-made/), you can generate payment links in your [backend](/glossaries/multisafepay-glossary/#backend).

See API reference:

- [Create an order](https://docs.multisafepay.com/api/#create-an-order) – In the `type` parameter, enter `paymentlink`. 
- [Generating a payment link](/api/#generate-payment-links)

## Payment link statuses

For an overview of all payment links in your [MultiSafepay account](https://merchant.multisafepay.com), go to **Tools** > **Payment link generator**.

| Status | Description |
|---|---|
| Active | The link is generated, but the customer hasn't paid yet.  | 
| Completed | The customer has paid. | 
| Cancelled | You cancelled the link.| 
| Expired | The link has expired.  | 

## Cloning payment links

To generate a copy of an exisiting payment link: 

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Next to the relevant payment link, click the blue copy icon.  
A new link generator window opens with the same details prefilled.  
4. Click **Generate payment link**.

## Cancelling payment links

To cancel a payment link:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Next to the relevant payment link, click the red cross icon.  
The status changes to **Cancelled**. 

Or see API reference – [Cancel an order](/api/#cancel-an-order).

## Support

For support, email the Integration Team at <integration@multisafepay.com>
