---
title: 'Bancontact'
category: 6298bd782d1cf4006032e765
order: 101
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: bancontact
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Bancontact.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

[Bancontact](https://www.bancontact.com/en) is a leading Belgian payment method that supports online, mobile, QR, POS, and wallet payments. It is a household name and supported by over 80% of Belgian webshops. Once payment is completed, the customer cannot reverse it and Bancontact guarantees settlement. 

See how Bancontact can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/bancontact).

# Overview

|   |   |   
|---|---|
| **Countries**  | Belgium  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/) |
| **Supports**  | [Recurring payments](/recurring-payments/) (banking only) <br> [Second Chance](/second-chance/) <br> [3D Secure 2.0](/3ds2/) for all non-mobile payments |
| **Transactions expire after** | 1 hour (banking only)  |

# Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Bancontact (QR) at checkout
    Mu->>C: Redirects to payment page <br> to select their bank, <br> and then to their online banking
    C->>CB: Authenticates account/scans QR code and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds 

{{< /mermaid >}}

# Payment statuses  

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your account balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| The customer has initiated a transaction. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| Bancontact has declined the transaction. | Declined | Declined   |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |
| **Refunds** | ||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment components](/payment-components/) <br> [Payment pages](/payment-pages/) <br> - Banking: Current and deprecated versions <br> - QR: Current only |
| **Testing** | [Test payment details](/testing/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Bancontact redirect/QR |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |
<br>

---

# Bancontact WIP Service

Bancontact WIP is a wallet initiated payment service you can use for:

- Bancontact One-Click Pay: customer-initiated one-click payments to make checkout faster and increase conversion
- Bancontact Recurring: merchant-initiated subscription payments

## How it works

Bancontact Payconiq gives you access to a merchant wallet to securely store customers' payment details in. Customers give one-time consent and only need to pass [strong customer authentication](/pds2/) (SCA) for their first purchase. 

There is no shift in liability for [chargebacks](/chargebacks/) from issuer to acquirer since your fraud and disputes volumes are monitored quarterly. A maximum transaction amount applies. 

## Activation and criteria

- Bancontact WIP is only available to low-risk, high-volume merchants (25,000 transactions quarterly), within the SEPA area. 
- Applies to services only, not physical products. 
- You must have easy-to-use procedures in place for refunds, cancellations, and disputes.
- Customers must be able to add, update, and delete their stored payment details.  
- You must be able to continually demonstrate low rates of fraudulent transactions, or access to your merchant wallet may be revoked. 

Email a request to activate Bancontact WIP to <sales@multisafepay.com>

Requests are screened and approved by Bancontact Payconiq. 

## Integration

See [Recurring payments](/recurring-payments/).
<br>

> 💬  Support
> For support, email <support@multisafepay.com>