---
title: "Currencies"
category: 627bbcf80c1c9c0050320b60
order: 3
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'currencies'
---

You can process payments in a large number of currencies. When customers can pay in their preferred local currency, it increases their trust in your website and therefore your <Glossary>conversion rate</Glossary>.

For all supported currencies, see [Payment methods per currency](#payment-methods-per-currency) below.

# How it works

To accept payments in a currency other than the default (EUR), the currency must be:

* Supported by the payment method
* Enabled for your account
* Supported in your <Glossary>backend</Glossary>
* Correctly processed in the [create order](/reference/createorder/) request

**⚠️ Note:** If the currency the customer wants to use is **not** supported by a payment method, the payment method does not appear in your checkout.

## Payouts

You can [make payouts](/docs/payouts/) in:

|                       |                      |                          |
| --------------------- | -------------------- | ------------------------ |
| AUD Australian dollar | EUR Euro             | PLN Polish złoty         |
| CAD Canadian dollar   | GBP British pound    | SEK Swedish krona        |
| CHF Swiss franc       | HKD Hong Kong dollar | USD United States dollar |
| DKK Danish krone      | NOK Norwegian krone  |                          |

If you receive funds in any other currency, you need to convert them to a payout currency to pay them out.

**⚠️ Note:** MultiSafepay applies a 4% conversion fee.

## Business bank account

You must also add to your account a business bank account that supports the currency so that no conversion is required there:

<details id="how-to-add-business-bank-account">
  <summary>How to add a business bank account</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard <i className="fa fa-external-link" style={{fontSize: '12px', color: '#8b929e'}} /></a>.
  2. Go to **Finances** > **Bank accounts**.
  3. Click **Add new**.
  4. Process a bank transfer in the new currency to confirm the business bank account.
</details>

## Account balances

When a transaction is initiated for a currency enabled for your account, we automatically create a separate balance for it in your dashboard. This provides a clear overview of your currencies and makes them easier to manage.

<details id="example-balances">
  <summary>See example account balances</summary>

  <br />

  <div style={{textAlign: 'center'}}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/AccountBalances.png" alt="Example of account balances" />
  </div>
</details>

## Example

<details id="example-scenario">
  <summary>See an example scenario</summary>

  <br />

  1. You have EUR, GBP, and BRL enabled for your account and supported in your <Glossary>backend</Glossary>.
  2. A Brazilian customer wants to pay in BRL via Visa. Visa supports BRL.
  3. Based on the customer's country, you display prices in BRL and at checkout, the payment page displays BRL. The customer feels as if they are paying in their local currency.

  <div style={{textAlign: 'center'}}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/CurrencyPaymentPage.png" alt="Example of payment page in BRL" />
  </div>

  4. You receive the funds in the BRL balance in your dashboard.

  <div style={{textAlign: 'center'}}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/AccountBalancesBRL.png" alt="Example of BRL account balance" />
  </div>

  5. To pay out funds, MultiSafepay converts to EUR and charges a 4% fee.

  <div style={{textAlign: 'center'}}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/CurrenciesPayout.png" alt="Example of currency payout" />
  </div>
</details>

# Activation

To view the currencies currently enabled for your account, go to your dashboard homepage.

To enable new currencies, email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a>

# Integration

<details id="prerequisites">
  <summary>Prerequisites</summary>

  <br />

  You must have a business bank account under your account that supports the currency so that no conversion is required there.
</details>

Make sure you:

* Enable the currency in your integration.
* Add the currency correctly in [create order](/reference/createorder/) requests.
* Consider whether conversion is required for making payouts.

<br />

***

# User guide

## Conversion

To convert other currencies to Euros (EUR), follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard <i className="fa fa-external-link" style={{fontSize: '12px', color: '#8b929e'}} /></a>.
2. Go to **Finance** > **Payouts**.
3. Under **Currency Converter**:

* Select the currency.
* Enter the amount.

5. Click **Convert**.

**⚠️ Note:** Take into account the exchange rate and MultiSafepay's 4% conversion fee.

## Payment methods per currency

<details id="payment-methods-per-currency">
  <summary>See all payment methods per currency</summary>

  <br />

  In this table, "cards" means: Apple Pay, Google Pay, Maestro, Mastercard, and Visa.
  Cards support all currencies.

  | Currency                        | Payment methods                                                       |
  | ------------------------------- | --------------------------------------------------------------------- |
  | AED United Arab Emirates dirham | Cards                                                                 |
  | AUD Australian dollar           | Cards, PayPal                                                         |
  | BGN Bulgarian lev               | Cards                                                                 |
  | BRL Brazilian real              | Cards, PayPal                                                         |
  | CAD Canadian dollar             | Bank transfer, cards, PayPal                                          |
  | CHF Swiss franc                 | Bank transfer, cards, PayPal, Sofort                                  |
  | CLP Chilean peso                | Cards                                                                 |
  | CNY Chinese yuan                | Cards                                                                 |
  | COP Colombian peso              | Cards                                                                 |
  | CZK Czech koruna                | Bank transfer, cards, PayPal, TrustPay                                |
  | DKK Danish krone                | Bank transfer, cards, Klarna, PayPal                                  |
  | EUR Euro                        | All payment methods                                                   |
  | GBP Pound Sterling              | Bank transfer, cards, Klarna, PayPal, Paysafecard, Sofort, Trustly    |
  | HKD Hong Kong dollar            | Alipay+, bank transfer, cards, PayPal                                 |
  | HRK Croatian kuna               | Cards, PayPal                                                         |
  | HUF Hungarian forint            | Bank transfer, cards, Google Pay, Maestro, Mastercard, PayPal, Sofort |
  | ILS Israeli new shekel          | Cards                                                                 |
  | INR Indian rupee                | Cards                                                                 |
  | ISK Icelandic króna             | Cards                                                                 |
  | JPY Japanese yen                | Bank transfer, cards, PayPal                                          |
  | KRW South Korean won            | Alipay+, cards                                                        |
  | MXN Mexican peso                | Cards, PayPal                                                         |
  | MYR Malaysian ringgit           | Alipay+, cards, PayPal                                                |
  | NOK Norwegian krone             | Bank transfer, cards, Klarna, PayPal                                  |
  | NZD New Zealand dollar          | Cards, PayPal                                                         |
  | PEN Peruvian Sol                | Cards                                                                 |
  | PHP Philippine peso             | Alipay+, PayPal                                                       |
  | PLN Polish złoty                | Bank transfer, cards, Dotpay, PayPal, Sofort                          |
  | RON Romanian leu                | Cards                                                                 |
  | RUB Russian ruble               | Cards, PayPal                                                         |
  | SEK Swedish krona               | Bank transfer, cards, Klarna, PayPal, Trustly                         |
  | SGD Singapore dollar            | Cards, PayPal                                                         |
  | THB Thai baht                   | Alipay+, PayPal                                                       |
  | TRY Turkish lira                | Cards, PayPal                                                         |
  | TWD New Taiwan dollar           | Cards, PayPal                                                         |
  | USD United States dollar        | Alipay+, Alipay, bank transfer, cards, PayPal, Paysafecard            |
  | VEF Venezuelan bolívar          | Cards                                                                 |
  | ZAR South African rand          | Cards                                                                 |
</details>

## Zero-decimal currencies

JPY is a **zero-decimal currency**.\
For decimal currencies, you provide the amount in cents, e.g. value for 10 EUR = **1000**.
For zero-decimal currencies, you must provide the whole value only, i.e. value for ¥10 = **10**.

<br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)