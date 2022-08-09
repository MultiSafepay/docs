---
title: "Currencies"
category: 62962dcdbccb9a001d4bbc81
order: 203
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'currencies'
---
# How it works

You can process payments in a large number of currencies, provided that they are:

- Supported by the specific payment method
- Enabled in your dashboard and in the settings of any [ready-made integrations](/docs/our-integrations/)
- Correctly processed in the [create order](/reference/createorder/) API request

# Activation

To view the currencies currently enabled for your account, in your dashboard go to **Finance > Balance**.

To enable new currencies, email <support@multisafepay.com>

You must also add a business bank account that supports the currency so that no conversion is required:

<details id="how-to-add-business-bank-account">
<summary>How to add a business bank account</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Finance > Balance > Add bank account**.
3. Process a bank transfer in the new currency to confirm the business bank account.

Once your new business bank account has been approved by the Risk Team, you can process <<glossary:payouts>> without currency conversion.
</details>
<br>

---

# User guide

## Conversion

To convert other currencies to Euros (EUR) in your [MultiSafepay dashboard](https://merchant.multisafepay.com), go to **Finance > Currency conversion**. 

Take into account the exchange rate and/or any other costs.

## Payment methods

All payment methods support: EUR (Euro)

Credit and debit cards support the following currencies (and potentially others on request):

| | | |
|---|---|---|
| AED United Arab Emirates dirham | HRK Croatian kuna | PHP Philippine peso |
| AUD Australian dollar | HUF Hungarian forint | PLN Polish złoty |
| BRL Brazilian real | ILS Israeli new shekel | RON Romanian leu |
| CAD Canadian dollar | INR Indian rupee | RUB Russian ruble |
| CHF Swiss franc | ISK Icelandic króna | SEK Swedish krona |
| CLP Chilean peso | JPY Japanese yen | SGD Singapore dollar |
| CNY Chinese yuan | KRW South Korean won | THB Thai baht |
| COP Colombian peso | MXN Mexican peso | TRY Turkish lira |
| CZK Czech koruna | MYR Malaysian ringgit | TWD New Taiwan dollar |
| DKK Danish krone | NOK Norwegian krone | USD United States dollar |
| GBP Pound Sterling | NZD New Zealand dollar | VEF Venezuelan bolívar |
| HKD Hong Kong dollar | PEN Peruvian Sol | ZAR South African rand |

> 📘 About JPY
> 
> JPY is a **zero-decimal currency**.
> For decimal currencies, you provide the amount in cents, e.g. value for 10 EUR = **1000**. 
> For zero-decimal currencies, provide the whole value only, i.e. value for ¥10 = **10**. 

## Payouts

You can make <<glossary:payouts>> in: 

| | | |
|---|---|---|
| AUD (Australian dollar) | EUR (Euro) | PLN (Polish złoty) |
| CAD (Canadian dollar) | GBP (Pound Sterling) | SEK (Swedish krona) |
| CHF (Swiss franc) | HKD (Hong Kong dollar) | USD (United States dollar) |
| DKK (Danish krone) | NOK (Norwegian krone) |  |
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)