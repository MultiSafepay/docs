---
title : "Currencies"
category: 62962dcdbccb9a001d4bbc81
order: 204
hidden: false
parentDoc: 62a206ee0298c80058af3aed
slug: 'currencies'
---
You can process payments in a large number of currencies, provided that they are:

- Supported by the specific payment method.
- Enabled in your dashboard and in the settings of any [ready-made integrations](/integrations/ready-made/).
- Correctly processed in the [create order](https://docs-api.multisafepay.com/reference/createorder) API request.

# Payment methods

All payment methods support: EUR (Euro)

Credit and debit cards support: 

|||
|---|---|
| AED (United Arab Emirates dirham) | KRW (South Korean won) |
| AUD (Australian dollar) | MXN (Mexican peso) |
| BRL (Brazilian real) | MYR (Malaysian ringgit) |
| CAD (Canadian dollar) | NOK (Norwegian krone) |
| CHF (Swiss franc) | NZD (New Zealand dollar) |
| CLP (Chilean peso) | PEN (Peruvian Sol) |
| CNY (Chinese yuan) | PHP (Philippine peso) |
| COP (Colombian peso) | PLN (Polish złoty) |
| CZK (Czech koruna) | RON (Romanian leu) |
| DKK (Danish krone) | RUB (Russian ruble) |
| GBP (Pound Sterling) | SEK (Swedish krona) |
| HKD (Hong Kong dollar) | SGD (Singapore dollar) |
| HRK (Croatian kuna) | THB (Thai baht) |
| HUF (Hungarian forint) | TRY (Turkish lira) |
| ILS (Israeli new shekel) | TWD (New Taiwan dollar) |
| INR (Indian rupee) | USD (United States dollar) |
| ISK (Icelandic króna) | VEF (Venezuelan bolívar) |
| JPY (Japanese yen) | ZAR (South African rand) |

> 📘 About JPY
> 
> JPY is a **zero-decimal currency**. For decimal currencies, you provide the amount in cents, e.g. value for 10 EUR = **1000**. For zero-decimal currencies, provide the whole value only, i.e. value for ¥10 = **10**.

For credit and debit cards, we can potentially support additional currencies on request. Email <support@multisafepay.com> 

# Payouts

You can make [payouts](/payouts/) in: 

| | |
|---|---|
| AUD (Australian dollar) | HKD (Hong Kong dollar) |
| CAD (Canadian dollar) | NOK (Norwegian krone) |
| CHF (Swiss franc) | PLN (Polish złoty) |
| DKK (Danish krone) | SEK (Swedish krona) |
| EUR (Euro) | USD (United States dollar) |
| GBP (Pound Sterling) | | 

# Activation

To view the currencies currently enabled for your account, in your dashboard go to **Finance > Balance**.

To enable new currencies, email <support@multisafepay.com>

You must also add a [business bank account](/invoices/) that supports the currency. Follow these steps to ensure transactions can be processed in that currency and no conversion is required:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Finance > Balance > Add bank account**.
3. Process a bank transfer in the new currency to confirm the business bank account.

Once your new business bank account has been approved by the Risk Team, you can process [payouts](/payouts/) without currency conversion.

# Conversion

To convert other currencies to Euros (EUR) in your [MultiSafepay dashboard](https://merchant.multisafepay.com), go to **Finance > Currency conversion**. 

Take into account the exchange rate and/or any other costs.
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>
