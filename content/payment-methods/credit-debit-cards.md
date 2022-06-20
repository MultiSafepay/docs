---
title: 'Credit and debit cards'
category: 6298bd782d1cf4006032e765
order: 200
hidden: false
slug: cards
--- 
<details id="about-credit-and-debit-cards">
<summary>About credit and debit cards</summary>
<br>

Credit cards are issued by a bank, building society, or card scheme and let customers pay on credit. Debit cards are issued by a bank and let customers transfer funds directly from their bank account. Cardholders can pay for products or services at a point of sale, online, or on a mobile app. They can also withdraw cash, or link their card to digital wallets or other local payment methods.

Credit cards are a very common payment method in many countries. Their widespread acceptance, ease of use, and ability to process payments in multiple currencies make them the ideal choice for many customers.

Cards may feature:

- A card number to uniquely identify the card
- A 3-4 digit card verification code (CVC) for additional security
- An expiry date 
- The cardholder's name 

</details>

MultiSafepay supports the following credit and debit cards:

- [American Express](https://www.multisafepay.com/solutions/payment-methods/american-express) (Amex)
- [Mastercard](https://www.multisafepay.com/solutions/payment-methods/mastercard) (credit card) and [Maestro](https://www.multisafepay.com/solutions/payment-methods/maestro) (debit card)
- [Postepay](https://www.multisafepay.com/solutions/payment-methods/postepay)
- [Visa](https://www.multisafepay.com/solutions/payment-methods/visa/) and co-branded cards [Cartes Bancaires](https://www.cartes-bancaires.com/), [Dankort](https://www.multisafepay.com/solutions/payment-methods/dankort), [V&nbsp;Pay](https://www.multisafepay.com/solutions/payment-methods/vpay) (debit card) 

# Overview

|   |   | 
|---|---|
| **Countries**  | Amex, Maestro, Mastercard, Visa: Worldwide <br> Cartes Bancaires: France <br> Dankort: Denmark <br>Postepay: Italy <br> V Pay: Europe | 
| **Currencies**  | Multiple (Amex: EUR, GBP, USD only) – To support additional currencies, email <support@multisafepay.com> | 
| **Chargebacks**  | [Yes](/chargebacks/), **except** Postepay | 
| **Refunds** | [Full and partial](/refunds/) |
| **Transactions expire after** | 1 hour |
| **Supports** | [3D Secure 2.0](/3ds2/), [Handling cardholder data](/cardholder-data/), [Manual Capture](/manual-capture/), [MOTO](/moto/), [Recurring payments](/recurring-payments/), [Second Chance](/second-chance/), [Zero Authorization](/cards/zero-authorization/) **except** Amex |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CS as Card scheme
    participant Me as Merchant
    participant CB as Customer's bank

    C->>Mu: Selects the card at checkout
    Mu->>C: Redirects to payment page
    C->>CS: Enters payment details, authenticates, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes transaction
    alt MultiSafepay collects
        CB->>Mu: Transfers funds 
        Mu->>Me: Settles funds
    else With Amex merchant account number
        CB->>CS: Transfers funds
        CS->>Me: Settles funds
    end
    
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
| The customer has been redirected for 3D Secure authentication, or the card scheme is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/uncaptured/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| ([Amex account number flow](#amex-merchant-account-number)) American Express has collected payment. | Completed | Initialized |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. <br> See [Card errors](/card-errors/). | Declined | Declined   |
|**Refunds/chargebacks**|||
| Refund/chargeback initiated. | Reserved    | Reserved   |
| Refund/chargeback complete.  | Completed      | Completed   |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payment-methods/#apply-to-multisafepay) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Card order <br>  See Examples and select the relevant card scheme example. <br> **Co-branded cards** <br> Co-branded cards are processed through the `VISA` gateway. <br> Set the `locale` parameter: <br> - Cartes Bancaires: `fr_FR` (France) <br> - Dankort: `da_DK` (Denmark) <br> - Postepay: `it_IT` (Italy) <br> **Generic gateway** <br> The generic `CREDITCARD` gateway saves space in your checkout and the payment page detects the card scheme based on the first 4 digits of the card number. <br> See Examples > Credit card redirect. |
| **Checkout options** | [Payment components](/payment-components/) <br> [Payment pages](/payment-pages/) (current and deprecated versions)  |
| **Testing** | [Test payment details](/testing/#credit-and-debit-cards) |
| **Ready-made integrations** | All our [ready-made integrations](/integrations/ready-made/) support: <br> - Amex, Maestro, Mastercard (redirect) <br> - Visa (including Cartes Bancaires, Dankort, Postepay, V Pay) (redirect)   |
<br>

---

# User guide

## Amex merchant account number

If you use your Amex merchant account number:
    
- Amex settles the funds directly in your business bank account.
- You are automatically added to the Safekey directory. 
- All currencies are supported. 

## Refunds

- You **cannot** refund more than the original transaction. 
- MultiSafepay sends refunds to the issuer within 1 business day.
- Whether or not the refund is visible to the customer depends on the issuer's system.
- Depending on the issuer, the amount may not appear directly on the customer's card. We recommend that they contact the issuer. If they need an acquirer reference number (ARN), they can email <support@multisafepay.com> 
- You can process refunds via MultiSafepay for up to 180 days after payment was completed. 

## Reversals

If you process a partial refund on the same day, this is technically called a "reversal", but for simplicity is logged as a refund in your MultiSafepay dashboard. 

On the customer's credit card statement, the transaction may either be:

- Adjusted to the new amount= Partial reversal
- Not debited at all= Full reversal
<br>

> 💬  Support
> Email <support@multisafepay.com>