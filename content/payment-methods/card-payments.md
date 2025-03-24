---
title: 'Card payments'
category: 6298bd782d1cf4006032e765
order: 3
hidden: false
slug: 'card-payments'
parentDoc: 62a727569e389a012f577acd
--- 

<details id="about-credit-and-debit-cards">
<summary>About credit and debit cards</summary>
<br>

Cards are issued by a bank, building society, or <<glossary:card scheme>> and let customers pay on credit. Debit cards are issued by a bank and let customers transfer funds directly from their bank account. Cardholders can pay for products or services at a point of sale, online, or on a mobile app. They can also withdraw cash, or link their card to digital wallets or other local payment methods.

Cards are a very common payment method in many countries. Their widespread acceptance, ease of use, and ability to process payments in multiple currencies make them the ideal choice for many customers.

Cards may feature:

- A card number to uniquely identify the card
- A 3-4 digit card verification code (CVC) for additional security
- An expiry date 
- The cardholder's name 

</details>

MultiSafepay supports the following credit and debit cards:

- <a href="https://www.multisafepay.com/solutions/payment-methods/american-express" target="_blank">American Express</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> (Amex)
- <a href="https://www.multisafepay.com/solutions/payment-methods/mastercard/" target="_blank">Mastercard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> (credit card) and <a href="https://www.multisafepay.com/solutions/payment-methods/maestro/" target="_blank">Maestro</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> (debit card)
- <a href="https://www.multisafepay.com/solutions/payment-methods/postepay/" target="_blank">Postepay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://www.multisafepay.com/solutions/payment-methods/visa/" target="_blank">Visa</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and co-branded cards <a href="https://www.multisafepay.com/solutions/payment-methods/carte-bleue" target="_blank">Cartes Bancaires</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, <a href="https://www.multisafepay.com/solutions/payment-methods/dankort/" target="_blank">Dankort</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, <a href="https://www.multisafepay.com/solutions/payment-methods/vpay" target="_blank">V&nbsp;Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> (debit card) 

**⚠️ Note:** [Co-branded cards](/docs/card-payments#co-branded-cards) are processed through the VISA <<glossary:gateway>>.

**⚠️ Note:** Payments made with AMEX in CHF are settled in EUR.

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Amex, Maestro, Mastercard, Visa: Worldwide <br> Cartes Bancaires: France <br> Dankort: Denmark <br>Postepay: Italy <br> V Pay: Europe | 
| [Currencies](/docs/currencies/)  | Amex: EUR, GBP, USD, CHF <br> Maestro, Mastercard, Visa: AED, AUD, BGN, BRL, CAD, CHF, CLP, CNY, COP, CZK, DKK, EUR, GBP, HKD, HRK, HUF, ILS, INR, ISK, JPY, KRW, MXN, MYR, NOK, NZD, PEN, PHP, PLN, RON, RUB, SEK, SGD, THB, TRY, TWD, UAH, USD, VEF, ZAR <br> To support additional currencies, email <support@multisafepay.com> | 
| [3D Secure 2.0](/docs/3ds2/) | Yes |
| [Chargebacks](/docs/chargebacks/)  | Yes, **except** Postepay | 
| [Payment components](/docs/payment-components/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions)  |
| [Recurring payments](/docs/recurring-payments/) | Yes |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/credit-debit-cards-payment-flow.svg" alt="Credit and debit cards payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the <<glossary:card scheme>> is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/docs/uncleared/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| ([Amex account number flow](#amex-merchant-account-number)) American Express has collected payment. | Completed | Initialized |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. <br> See [Card errors](/docs/card-errors/). | Declined | Declined   |
| Refund/chargeback initiated. | Reserved    | Reserved   |
| Refund/chargeback complete.  | Completed      | Completed   |

# Activation 

1. Email a request to activate cards to <sales@multisafepay.com> 
    
    Include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 

   We check your eligibilty and if approved, activate the payment method for your account. 
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
4. Select the checkbox for the payment method, and then click **Save changes**.

**⚠️ Note:** By default, recurring payments made with cards are limited to one transaction per IBAN every 24 hours. To request a change to this limit, email <sales@multisafepay.com>

💬  **Support:** If the payment method isn't visible in your dashboard, email <support@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Card order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Card direct/redirect**. Set `gateway` to `AMEX`, `MAESTRO`, `MASTERCARD`, `VISA`, or the generic `CREDITCARD`.

  **⚠️ Note:** Consider card-specific requirements for the [Create order request](/reference/createorder/), for example including correct details in the `email` or `phone` parameter for VISA payments. 

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- Transactions expire after 1 hour.

#### Co-branded cards
Co-branded cards are processed through the `VISA` <<glossary:gateway>>. 
In the `customer` object, set the `locale` parameter: 
- Cartes Bancaires: `fr_FR` (France) 
- Dankort: `da_DK` (Denmark) 
- Postepay: `it_IT` (Italy) 

#### Generic gateway
- The generic `CREDITCARD` gateway bundles all cards activated for your account into a single gateway to save space in your checkout. The [payment page](/docs/payment-pages/) automatically detects the specific card scheme based on the first 4 digits of the card number the customer enters. 
- See Examples > Card payment redirect. 

### Ready-made integrations
All our [ready-made integrations](/docs/our-integrations/) support: 
- Amex, Maestro, Mastercard (<<glossary:redirect>>) 
- Visa (including Cartes Bancaires, Dankort, Postepay, V Pay) (<<glossary:redirect>>) 

### Testing
To test card payments, see Testing payment methods - [Credit and debit cards](/docs/testing#credit-and-debit-cards).
<br>

---

# User guide

## Amount limits

For credit card payments, the maximum order amount will be limited to 5,000 EUR by default. To request a change to this limit, email <risk@multisafepay.com>

Occasional credit card payments that surpass the maximum limit must be justified. Email the invoice to <risk@multisafepay.com>

## Amex merchant account number

If you use your Amex merchant account number:
    
- Amex settles the funds directly in your business bank account.
- You are automatically added to the Safekey directory. 
- All currencies are supported. 

## Cardholder data

The <<glossary:redirect>> integration means MultiSafepay handles sensitive cardholder data. You can also integrate directly and handle data on your PCI DSS compliant server.

See [Cardholder data](/docs/cardholder-data/).

## Refunds and reversals

See [Card refunds](/docs/card-refunds/).

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)