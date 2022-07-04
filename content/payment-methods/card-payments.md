---
title: 'Card payments'
category: 6298bd782d1cf4006032e765
order: 301
hidden: false
slug: 'card-payments'
parentDoc: 62a727569e389a012f577acd
--- 

<details id="about-credit-and-debit-cards">
<summary>About credit and debit cards</summary>
<br>

Credit cards are issued by a bank, building society, or <<glossary:card scheme>> and let customers pay on credit. Debit cards are issued by a bank and let customers transfer funds directly from their bank account. Cardholders can pay for products or services at a point of sale, online, or on a mobile app. They can also withdraw cash, or link their card to digital wallets or other local payment methods.

Credit cards are a very common payment method in many countries. Their widespread acceptance, ease of use, and ability to process payments in multiple currencies make them the ideal choice for many customers.

Cards may feature:

- A card number to uniquely identify the card
- A 3-4 digit card verification code (CVC) for additional security
- An expiry date 
- The cardholder's name 

</details>

MultiSafepay supports the following credit and debit cards:

- [American Express](https://www.multisafepay.com/solutions/payment-methods/american-express) (Amex)
- [Mastercard](https://www.multisafepay.com/solutions/payment-methods/mastercard/) (credit card) and [Maestro](https://www.multisafepay.com/solutions/payment-methods/maestro/) (debit card)
- [Postepay](https://www.multisafepay.com/solutions/payment-methods/postepay/)
- [Visa](https://www.multisafepay.com/solutions/payment-methods/visa/) and co-branded cards [Cartes Bancaires](https://www.cartes-bancaires.com/), [Dankort](https://www.multisafepay.com/solutions/payment-methods/dankort/), [V&nbsp;Pay](https://www.multisafepay.com/solutions/payment-methods/vpay) (debit card) 

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Amex, Maestro, Mastercard, Visa: Worldwide <br> Cartes Bancaires: France <br> Dankort: Denmark <br>Postepay: Italy <br> V Pay: Europe | 
| [Currencies](/docs/currencies/)  | Multiple (Amex: EUR, GBP, USD only) <br> To support additional currencies, email <support@multisafepay.com> | 
| [3D Secure 2.0](/docs/3ds2/) | Yes |
| [Chargebacks](/docs/chargebacks/)  | Yes, **except** Postepay | 
| [Payment components](/docs/payment-components/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions)  |
| [Recurring payments](/docs/recurring-payments/) | Yes |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/credit-debit-cards-payment-flow.svg" alt="Credit and debit cards payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the <<glossary:card scheme>> is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/docs/uncaptured/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| ([Amex account number flow](#amex-merchant-account-number)) American Express has collected payment. | Completed | Initialized |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. <br> See [Card errors](/docs/card-errors/). | Declined | Declined   |
| Refund/chargeback initiated. | Reserved    | Reserved   |
| Refund/chargeback complete.  | Completed      | Completed   |

# Activation 

First apply to MultiSafepay, and then activate in your dashboard.

<details id="how-to-activate-cards"> 
<summary>How to activate cards</summary>
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

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](/reference/createorder/) > Card order 
- See Examples and select the relevant <<glossary:card scheme>> example. 
- Transactions expire after 1 hour.

#### Co-branded cards
Co-branded cards are processed through the `VISA` <<glossary:gateway>>. 
Set the `locale` parameter: 
- Cartes Bancaires: `fr_FR` (France) 
- Dankort: `da_DK` (Denmark) 
- Postepay: `it_IT` (Italy) 

#### Generic gateway
- The generic `CREDITCARD` gateway saves space in your checkout and the payment page detects the card scheme based on the first 4 digits of the card number. 
- See Examples > Credit card redirect. 

### Ready-made integrations
All our [ready-made integrations](/docs/our-integrations/) support: 
- Amex, Maestro, Mastercard (redirect) 
- Visa (including Cartes Bancaires, Dankort, Postepay, V Pay) (redirect) 

### Testing
To test card payments, see [Testing](/docs/testing#credit-and-debit-cards).
<br>

---

# User guide

## Amex merchant account number

If you use your Amex merchant account number:
    
- Amex settles the funds directly in your business bank account.
- You are automatically added to the Safekey directory. 
- All currencies are supported. 

## Cardholder data

The redirect integration means MultiSafepay handles sensitive cardholder data. You can also integrate directly and handle data on your PCI DSS compliant server.

See [Cardholder data](/docs/cardholder-data/).

## Refunds

- You **cannot** refund more than the original transaction. 
- MultiSafepay sends refunds to the <<glossary:issuer>> within 1 business day.
- Whether or not the refund is visible to the customer depends on the issuer's system.
- Depending on the issuer, the amount may not appear directly on the customer's card. We recommend that they contact the issuer. If they need an acquirer reference number (ARN), they can email <support@multisafepay.com> 
- You can process refunds via MultiSafepay for up to 180 days after payment was completed. 

## Reversals

If you process a partial refund on the same day, this is technically a <<glossary:reversal>>, but for simplicity is logged as a refund in your MultiSafepay dashboard. 

On the customer's credit card statement, the transaction may either be:

- Adjusted to the new amount= Partial reversal
- Not debited at all= Full reversal
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)