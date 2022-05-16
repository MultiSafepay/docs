---
title: 'Cards overview'
weight: 10
meta_title: "Cards overview - MultiSafepay Docs"
layout: 'single' 
short_description: 'Global credit card scheme accepted in more than 160 countries.'
url: '/payment-methods/cards/'
aliases:
    - /payments/methods/american-express/
    - /support-tab/magento2/payment-methods/american-express
    - /payment-methods/creditcards/american-express/
    - /payment-methods/credit-and-debit-cards/american-express
    - /payments/methods/credit-and-debit-cards/american-express
    - /payment-methods/american-express/
    - /payments/methods/american-express/
    - /support-tab/magento2/payment-methods/american-express
    - /payment-methods/creditcards/american-express/
    - /payment-methods/credit-and-debit-cards/american-express
    - /payments/methods/credit-and-debit-cards/american-express
    - /payment-methods/american-express/
    - /payment-methods/amex/
    - /payment-methods/credit-and-debit-cards/american-express/american-express-additional-information
    - /payment-methods/american-express/about/
    - /payments/methods/amex/product-rules/
    - /payments/methods/amex/overview/
    - /payment-methods/amex/overview/
    - /payment-methods/american-express/activation/
    - /payment-methods/credit-and-debit-cards/american-express/activate-american-express/
    - /payment-methods/amex/activation/
    - /payment-methods/credit-and-debit-cards/american-express/how-does-american-express-work/
    - /payments/methods/credit-and-debit-cards/american-express/payment-flow/
    - /payment-methods/amex/payment-flow/
    - /payment-methods/credit-and-debit-cards/american-express/american-express-testing
    - /payment-methods/credit-and-debit-cards/credit-card-payment-page
    - /payments/methods/credit-and-debit-cards/american-express/integration-and-testing/
    - /payment-methods/amex/integration-testing/
---
MultiSafepay supports the following credit and debit cards:

- [American Express](https://www.multisafepay.com/solutions/payment-methods/american-express)
- [Mastercard](https://www.multisafepay.com/solutions/payment-methods/mastercard) and [Maestro](https://www.multisafepay.com/solutions/payment-methods/maestro) (debit card)
- [Postepay](https://www.multisafepay.com/solutions/payment-methods/postepay)
- [Visa](https://www.multisafepay.com/solutions/payment-methods/visa/)
    - [Cartes Bancaires](https://www.cartes-bancaires.com/)
    - [Dankort](https://www.multisafepay.com/solutions/payment-methods/dankort)
    - [V Pay](https://www.multisafepay.com/solutions/payment-methods/vpay) (debit card) 

## Overview

|   |   | 
|---|---|
| **Countries**  | AMEX, Maestro, Mastercard, Visa: Worldwide <br> Cartes Bancaires: France <br> Dankort: Denmark <br>Postepay: Italy <br> VPay: Europe | 
| **Currencies**  | Multiple (AMEX: EUR, GBP, USD only) <br> To support additional currencies, email <support@multisafepay.com> | 
| **Chargebacks**  | [Yes](/payments/chargebacks/), **except** Postepay | 
| **Refunds** | [Full and partial](/refunds/full-partial/) |
| **Transactions expire after** | 1 hour |
| **Payment features** | [3D Secure](/features/3d-secure/) <br> [Handling cardholder data](/features/handling-cardholder-data/) <br> [Manual Capture](/features/manual-capture/) <br> [MOTO](/features/moto/) <br> [Recurring Payments](/features/recurring-payments/) <br> [Second Chance](/features/second-chance/) <br> [Zero Authorization](/features/zero-authorization/), **except** AMEX |

{{< details title="American Express merchant account number" >}}

If you use your American Express merchant account number:
    
- American Express settles the funds directly in your business bank account.
- You are automatically added to the Safekey directory. 
- All currencies are supported.  
  
For more information, email <support@multisafepay.com>
{{< /details >}}

## Payment flow

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
    else With American Express MID
        CB->>CS: Transfers funds
        CS->>Me: Settles funds
    end
    
{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the card scheme is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/about-payments/uncleared-transactions/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| (Amex MID flow) American Express has collected payment. | Completed | Initialized |
| Payment wasn't captured manually or within 5&nbsp;days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. <br> See [Declined credit card payments](/about-payments/declined-status/). | Declined | Declined   |
|**Refunds/chargebacks**|||
| Refund/chargeback initiated. | Reserved    | Reserved   |
| Refund/chargeback complete.  | Completed      | Completed   |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Card order <br>  See Examples and select the relevant card scheme example. <br> **Co-branded cards** <br> Set the `locale` parameter: <br> - Cartes Bancaires: `fr_FR` (France) <br> - Dankort: `da_DK` (Denmark) <br> - Postepay: `it_IT` (Italy) <br> **Generic gateway** <br> The generic `CREDITCARD` gateway saves space in your checkout and the payment page detects the card scheme based on the first 4 digits of the card number. <br> See Examples > Credit card redirect. |
| **Ready-made integrations** | All our [ready-made integrations](/integrations/ready-made/) support: <br> - AMEX (redirect) <br> - Maestro (redirect) <br> - Mastercard (redirect) <br> - Visa (including Cartes Bancaires, Dankort, Postepay, VPay) (redirect)   |
| **Checkout options** | [Payment components](/payment-components/) <br> [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/))  |
| **Testing** | [Test payment details](/testing/test-payment-details/#credit-and-debit-cards) |
