---
title: 'Google Pay'
weight: 240
meta_title: "Payment methods - Google Pay - MultiSafepay Docs"
layout: "single"
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/GooglePay.svg" 
short_description: "Digital wallet for online and in-app purchases."
url: "/payment-methods/google-pay/"
aliases:
    - /support-tab/magento2/payment-methods/googlepay
    - /payment-methods/wallet/googlepay
    - /payment-methods/google-pay/product-rules
    - /payment-methods/google-pay/overview/
    - /payment-methods/google-pay/payment-flow
    - /payment-methods/google-pay/integration-testing
    - /payment-methods/google-pay/activation
---

Google Pay™ is a digital wallet for in-app and online payments. Customers can tokenize their payment details in their Google Pay account.

[See how Google Pay can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/googlepay)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide. See Google Pay – [Countries or regions where you can use Google Pay](https://support.google.com/pay/answer/9023773?hl=en#zippy=%2Cpay-online-or-in-apps).  | 
| **Currencies**  | Multiple  | 
| **Chargebacks**  | [Yes](/payments/chargebacks/) | 
| **Refunds** | [Full and partial](/refunds/full-partial/) {{< br >}} Customers receive refunds in their Google Pay account, and they appear on their credit card statement within the next business day.  |
| **Supports**  | [Second Chance](/features/second-chance/) {{< br >}} [Recurring Payments](/payments/recurring-payments/)  |
| **Transactions expire after** | 1 hour |
| **Payment gateways** | Maestro, Mastercard, and Visa gateways are supported. <br> American Express is **not** supported. |
| **Terms and conditions** | By processing Google Pay payments, you agree to the [Google API Terms of Service](https://payments.developers.google.com/terms/sellertos). |

{{< details title="Supported browsers" >}} 

Google Pay is supported in the following browsers:

- Apple Safari
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Opera
- UCWeb UC Browser

{{< /details >}}

For more information, see Google Pay – [Overview](https://developers.google.com/pay/api/web/overview).

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant G as Google Pay
    participant CS as Card scheme
    participant Me as Merchant
    participant CB as Customer's bank
    
    C->>Mu: Selects Google Pay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> then to Google account
    else Direct flow
    Mu->>C: Redirects to Google account
    end
    C->>G: Completes payment 
    alt Redirect integration
    G->>Mu: Sends token
    else Direct integration
    G->>Me: Sends the customer's payment details as an encrypted token
    Me->>Mu: Sends token
    end
    Mu->>CS: Decrypts token and processes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes (or declines) transaction
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the card scheme is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. {{< br >}} Review it and then [manually capture or decline](/cards/uncaptured/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D&nbsp;Secure authentication. | Expired | Expired |
| The customer failed 3D&nbsp;Secure authentication or cancelled payment. {{< br >}} See [Card errors](/cards/errors/). | Declined | Declined   |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved   |
| Refund complete.  | Completed | Completed   |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only)  |
| **Testing** | [Test payment details](/testing/test-payment-details/) |
| **Google branding** | When integrating Google Pay into your ecommerce platform, you must follow [Google's brand guidelines](https://developers.google.com/pay/api/web/guides/brand-guidelines). |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) (redirect), **except** Magento 2 and WooCommerce. <br> For these, you can use a generic gateway. See their manuals for further details. |


{{< two-buttons href-2="/google-pay/direct/" text-2="Google Pay™ direct integration manual" description-2="Embed Google Pay in your checkout page for the best user experience." img-2="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/GooglePay.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="https://docs-api.multisafepay.com/reference/createorder" text-2="Google Pay™ redirect integration manual" description-2="Easily integrate Google Pay using MultiSafepay payment pages." img-2="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/GooglePay.svg" alt-2="Right arrow" >}}
