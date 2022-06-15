---
title: 'Apple Pay'
category: 6298bd782d1cf4006032e765
order: 502
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: apple-pay
---
[Apple Pay](https://www.apple.com/apple-pay/) is a leading global payment method that lets customers tokenize their payment details in a digital wallet. It supports Maestro, Mastercard, and Visa, and Dutch bank accounts. Customers can make both online and near-field communication (NFC) payments. 

An additional layer of security is provided by 3D Secure, which requires customers to verify their identity.

See how Apple Pay can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/applepay).

# Overview

|   |   |
|---|---|
| **Countries**  | [Worldwide](https://support.apple.com/en-us/HT207957)  | 
| **Currencies**  | [Multiple](https://support.apple.com/en-us/HT207957)  | 
| **Chargebacks**   | [Yes](/chargebacks/) | 
| **Refunds** | [Full and partial](/refunds/) <br> Customers receive refunds in their Apple Pay account, and they appear on their credit card statement within the next business day.  |
| **Supports**  | [Second Chance](/second-chance/) |
| **Transactions expire after** | 1 hour |
| **Requirements** | Customers must use the Safari browser. <br> An SSL secured connection (HTTPS) is required. |
| **Payment gateways** | American Express, Maestro, Mastercard, and Visa gateways are supported. |

For more information, see Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).

# Payment flow

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

# Payment statuses

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| The customer has been redirected for 3D Secure authentication, or the card scheme is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/uncaptured/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. See [Card errors](/card-errors/). | Declined | Declined   |
|**Refunds**|||
| Refund initiated. | Reserved    | Reserved   |
| Refund complete.  | Completed  | Completed  |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) (current version only)  |
| **Testing** | [Test payment details](/testing/) |
| **Apple branding** | When integrating Apple Pay into your website, you must follow Apple's [branding guidelines](https://developer.apple.com/apple-pay/marketing). |
| **Ready-made integrations** | Apple Pay redirect is supported in all [ready-made integrations](/integrations/ready-made/), **except** OsCommerce, VirtueMart, X-Cart, Zen Cart. |
<br>

To build your own Apple Pay integration, see:

- [Direct integration](/apple-pay-direct/)

- [Redirect integration](/apple-pay-redirect/)
<br>

---

# User guide

### Known errors

For most of our ready-made integrations, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page. 

For our [OpenCart plugin](/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>