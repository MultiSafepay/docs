---
title: 'Apple Pay'
weight: 230
meta_title: "Payment methods - Apple Pay - MultiSafepay Docs"
layout: "single"
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Apple.svg" 
short_description: "Digital wallet for online and in-app payments from Apple devices."
url: "/payment-methods/apple-pay/"
aliases:
    - //payment-methods/applepay/
    - /support-tab/magento2/payment-methods/applepay
    - /payment-methods/wallet/applepay
    - /payments/methods/wallet/applepay/
    - /payments/methods/wallet/applepay/about/
    - /payments/methods/apple-pay/product-rules/
    - /payment-methods/apple-pay/product-rules/
    - /payment-methods/apple-pay/overview/
    - /payment-methods/wallet/applepay/apple-pay-how-does-it-work
    - /payments/methods/wallet/applepay/payment-flow/
    - /payment-methods/apple-pay/payment-flow/
    - /payment-methods/wallet/applepay/apple-pay-compatibility-and-testing
    - /payment-methods/wallet/applepay/apple-pay-guidelines
    - /payments/methods/wallet/applepay/integration-and-testing/
    - /payment-methods/apple-pay/integration-testing/
    - /payment-methods/wallet/applepay/activate-apple-pay
    - /payments/methods/wallet/applepay/activation/
    - /payment-methods/apple-pay/activation/
---

[Apple Pay](https://www.apple.com/apple-pay/) is a leading global payment method that lets customers tokenize their payment details in a digital wallet. It supports Maestro, Mastercard, and Visa, and Dutch bank accounts. Customers can make both online and near-field communication (NFC) payments. 

An additional layer of security is provided by 3D Secure, which requires customers to verify their identity.

[See how Apple Pay can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/applepay)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | [Worldwide](https://support.apple.com/en-us/HT207957)  | 
| **Currencies**  | [Multiple](https://support.apple.com/en-us/HT207957)  | 
| **Chargebacks**   | [Yes](/payments/chargebacks/) | 
| **Refunds** | [Full and partial](/refunds/full-partial/) {{< br >}} Customers receive refunds in their Apple Pay account, and they appear on their credit card statement within the next business day.  |
| **Supports**  | [Second Chance](/features/second-chance/) |
| **Transactions expire after** | 1 hour |
| **Requirements** | Customers must use the Safari browser. <br> An SSL secured connection (HTTPS) is required. |
| **Payment gateways** | American Express, Maestro, Mastercard, and Visa gateways are supported. |

For more information, see Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as Apple Pay
    participant CS as Card scheme
    participant Me as Merchant
    
    C->>Mu: Selects Apple Pay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> and then to Apple
    else Direct flow
    Mu->>C: Redirects to Apple
    end
    C->>A: Authorizes payment on an iOS device with Touch ID or Face ID
    alt Redirect integration
    A->>Mu: Sends token
    else Direct integration
    A->>Me: Sends the customer's payment details as an encrypted token
    Me->>Mu: Sends token
    end
    Mu->>CS: Decrypts token and processes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes transaction
    CS->>Mu: Transfers funds 
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
| Refund initiated. | Reserved    | Reserved   |
| Refund complete.  | Completed  | Completed  |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only)  |
| **Testing** | [Test payment details](/testing/test-payment-details/) |
| **Apple branding** | When integrating Apple Pay into your website, you must follow Apple's [branding guidelines](https://developer.apple.com/apple-pay/marketing). |

{{< details title="Ready-made integrations" >}}
 
Supported in all [ready-made integrations](/integrations/ready-made/) (redirect), **except**:

- OsCommerce
- VirtueMart 
- X-Cart
- Zen Cart

{{< /details >}}

{{< details title="Known errors" >}}

For most of our ready-made integrations, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page. 

For our [OpenCart plugin](/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.

{{< /details >}}

{{< two-buttons href-2="/apple-pay/direct/" text-2="Apple Pay direct integration manual" description-2="Embed Apple Pay in your checkout page for the best user experience" img-2="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Apple.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/apple-pay/redirect/" text-2="Apple Pay redirect integration manual" description-2="Integrate Apple Pay using MultiSafepay payment pages" img-2="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Apple.svg" alt-2="Right arrow" >}}
