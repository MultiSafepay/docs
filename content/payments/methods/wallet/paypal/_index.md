---
title: 'PayPal'
weight: 220
meta_title: "Payment methods - PayPal - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/PayPal.svg' 
short_description: 'Leading global payment method that supports credit cards and a digital wallet.'
url: '/payment-methods/paypal/'
aliases:
    - /support-tab/magento2/payment-methods/paypal
    - /payment-methods/paypal/
    - /payment-methods/wallet/paypal
    - /payments/methods/wallet/paypal/
    - /payments/methods/wallet/paypal/about/
    - /payments/methods/paypal/product-rules/
    - /payment-methods/paypal/product-rules/
    - /payment-methods/paypal/overview/
    - /payment-methods/wallet/paypal/how-does-paypal-work
    - /payments/methods/wallet/paypal/payment-flow/
    - /payment-methods/paypal/payment-flow/
    - /payment-methods/wallet/paypal/paypal-testing
    - /payments/methods/wallet/paypal/integration-and-testing/
    - /payment-methods/paypal/integration-testing/
    - /payment-methods/paypal/activate-paypal
    - /faq/errors-explained/paypal-error-10002
    - /faq/errors-explained/iframe-errors
    - /payments/methods/wallet/paypal/activation/
    - /payment-methods/paypal/activation/
---

[PayPal](https://www.paypal.com/nl/home) is a leading global payment method that lets customers pay by credit card or create a digital wallet linked to multiple payment methods.

[See how PayPal can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/paypal)

## Overview

|   |   |  
|---|---|
| **Countries**  | Worldwide  | 
| **Currencies**  | [Multiple](https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies/) | 
| **Chargebacks**  |  [Yes](/payments/chargebacks/)  |
| **Refunds** | [Full and partial](/refunds/full-partial/) (see guidance below) | 
| **Supports** | [Second Chance](/features/second-chance/) |
| **Transactions expire after**  | 14 days | |

### Refunds

Refunds are only processed if there are enough funds in your PayPal business account. Otherwise, PayPal issues an [eCheck](https://www.paypal.com/us/smarthelp/article/what-is-an-echeck-faq1082). 

To avoid PayPal cancelling the refund, in your PayPal account, authorize PayPal to withdraw funds from another bank account instead. 

For support, contact PayPal – [Help Center Home](https://www.paypal.com/us/smarthelp/home).

### PayPal Seller Protection

PayPal Seller Protection covers you in the event of claims, chargebacks, or reversals due to unauthorized purchases or items the customer didn't receive. You are covered for the full amount of all eligible transactions.

To be eligible, for specific countries, transaction requests must contain the correct `state` in the `customer_address`. 

For:

- A list of the countries, see PayPal API – [State codes](https://developer.paypal.com/api/rest/reference/state-codes/)
- More information, see PayPal – [What is Seller Pretection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156)

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant P as PayPal
    participant Me as Merchant

    C->>Mu: Selects PayPal at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> then to their PayPal account
    else Direct flow
    Mu->>C: Redirects to PayPal account
    end
    C->>P: Authenticates account, and completes payment 
    P->>Me: Settles funds in your <br> PayPal business account

{{< /mermaid >}}
&nbsp;  

**Note:** MultiSafepay does **not** collect funds for PayPal transactions.

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/account/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to PayPal. | Initialized | Initialized |
| - Awaiting the customer to pay in their PayPal account **or** <br> - PayPal is authorizing the transaction **or** <br> - You may need to enable the currency and then authorize the payment in your PayPal business account.  | Uncleared | Initialized |
| PayPal has collected payment. | Completed | Initialized |
| The customer cancelled the payment in PayPal. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 14 days. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Initialized |
| Refund complete.  | Completed | Initialized |
| Refund declined. | Declined | Declined |
| - PayPal is authorizing the refund. <br> **Or** <br> - There are not enough funds in your PayPal business account to process the refund. <br> For more information, see your PayPal business account. | Uncleared | Initialized   |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [PayPal activation](/payments/activating-payment-methods/#paypal) |
| **Checkout options** | [Payment components](/payment-components/) <br> [Payment pages](/payment-pages/) <br> ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/) versions) |
| **Testing** | [Test payment details](/testing/test-payment-details/#wallets) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order <br> Examples > PayPal direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) |

### Displaying your logo in the PayPal checkout

{{< details title="Displaying your logo in the PayPal checkout" >}}
To display your header or logo on the PayPal checkout page, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Files**, and upload the relevant images. 
3. Go to **Payment methods** at the bottom right, and then select the relevant images from the **Logo** and **Header** list. 
4. Click **Save**.

{{< /details >}}
