---
title: 'Apple Pay'
category: 6298bd782d1cf4006032e765
order: 502
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'apple-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Apple.svg" width="70" align="right" style="margin: 20px; max-height: 75px"/>

[Apple Pay](https://www.apple.com/apple-pay/) is a leading global payment method that lets customers tokenize their payment details in a digital wallet. It supports Maestro, Mastercard, and Visa, and Dutch bank accounts. Customers can make both online and near-field communication (NFC) payments. 

An additional layer of security is provided by 3D Secure, which requires customers to verify their identity.

Read how Apple Pay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/applepay)

| Overview | Details |
|---|---|
| **Chargebacks**   | [Yes](/chargebacks/) | 
| **Countries**  | [Worldwide](https://support.apple.com/en-us/HT207957)  | 
| **Currencies**  | [Multiple](https://support.apple.com/en-us/HT207957)  | 
| **Expiration** | Transactions expire after 1 hour. |
| **Payment pages** | [Yes](/payment-pages/) (current version only)  |
| **Refunds** | [Yes](/refunds/): Full and partial <br> Customers receive refunds in their Apple Pay account, and they appear on their credit card statement within the next business day.  |
| **Second Chance** | [Yes](/second-chance/) |
<br>

> ℹ️ More information 
> See Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).

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

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the card scheme is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/uncaptured/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. <br> See [Card errors](/card-errors/). | Declined | Declined   |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Reserved    | Reserved   |
| Refund complete.  | Completed  | Completed  |

</details>

# Activation 

First, apply to MultiSafepay and then activate Apple Pay in your dashboard.

<details id="how-to-activate-apple-pay"> 
<summary>How to activate Apple Pay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
    
    Include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 

2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
4. Go to **Settings**. 
5. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the relevant payment method, and then click **Save changes**.

> 💬  Support
> If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

</details>

# Integration

### Prerequisites

- Customers must use the Safari browser. 
- An SSL secured connection (HTTPS) is required.

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order |
| **Ready-made integrations** | Apple Pay redirect is supported in all [ready-made integrations](/integrations/ready-made/), **except** OsCommerce, VirtueMart, X-Cart, Zen Cart. |
| **Self-made integration** | - [Direct integration](/apple-pay-integration/#direct-integration) <br> - [Redirect integration](/apple-pay-integration/#redirect-integration) |
<br>

> **Note** 
> When integrating Apple Pay into your website, you must follow Apple's [branding guidelines](https://developer.apple.com/apple-pay/marketing).

> ℹ️ Testing
> To test Apple Pay payments, see [Testing](/testing/#wallets).
<br>

---

# User guide

## Gateways

American Express, Maestro, Mastercard, and Visa gateways are supported. 

## Known errors

For most of our ready-made integrations, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page. 

For our [OpenCart plugin](/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)