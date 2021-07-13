---
title : "Enabling and converting currencies"
meta_title: "MultiSafepay account - Enabling and converting currencies - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
weight: 70
aliases:
    - /faq/general/which-currencies-are-supported-by-multisafepay
    - /faq/general/currencies-supported
    - /faq/general/supported-currencies/
    - /tools/multisafepay-control/enabling-converting-currencies
---

{{< details title="Supported currencies per payment method" >}}

| Currency  | All payment methods  | Visa, Mastercard, Maestro  | Payouts  |
|---|---|---|---|
| AED (United Arab Emirates dirham)  |   |  Y |   |
| AUD (Australian dollar)  |  | Y  | Y  |
| BRL (Brazilian real)  |   |  Y |   |
| CAD (Canadian dollar)  |   | Y  | Y  |
| CHF (Swiss franc)  |   | Y  | Y  |
| CLP (Chilean peso)  |   |  Y |   |
| CNY (Chinese yuan)  |   |  Y |   |
| COP (Colombian peso)  |   |  Y |   |
| CZK (Czech koruna)  |   |  Y |   |
| DKK (Danish krone)  |   | Y  | Y  |
| EUR (Euro)  | Y  |  Y | Y  |
| GBP (Pound Sterling)   | Y  | Y  | Y  |
| HKD (Hong Kong dollar)  |   | Y  | Y  |
| HRK (Croatian kuna)  |   |  Y |   |
| HUF (Hungarian forint)  |   |  Y |   |
| ILS (Israeli new shekel)  |   |  Y |   |
| INR (Indian rupee)  |   |  Y |   |
| ISK (Icelandic króna)  |   |  Y |   |
| JPY (Japanese yen)  |   |  Y |   |
| KRW (South Korean won)  |   |  Y |   |
| MXN (Mexican peso)  |   |  Y |   |
| MYR (Malaysian ringgit)  |   |  Y |   |
| NOK (Norwegian krone) |   | Y  | Y  |
| NZD (New Zealand dollar)  |   |  Y |   |
| PEN (Peruvian Sol)  |   |  Y |   |
| PHP (Philippine peso)  |   |  Y |   |
| PLN (Polish złoty) |   | Y  | Y  |
| RON (Romanian leu)  |   |  Y |   |
| RUB (Russian ruble) |   |  Y |   |
| SEK (Swedish krona) |   | Y  | Y  |
| SGD (Singapore dollar)  |   |  Y |   |
| THB (Thai baht)  |   |  Y |   |
| TRY (Turkish lira)  |   |  Y |   |
| TWD (New Taiwan dollar)  |   |  Y |   |
| USD (United States dollar)  |   | Y  | Y  |
| VEF (Venezuelan bolívar)  |   | Y  |   |
| ZAR (South African rand)  |   |  Y |   |

{{< /details >}}

{{< details title="Currencies on request" >}}

For Visa, MasterCard, and Maestro, we can potentially support additional currencies on request. Email the Support Team at <support@multisafepay.com>  

{{< /details >}}

You can process payments in a large number of currencies, provided that they are:

- Supported by the specific payment method.
- Enabled in your [MultiSafepay account](https://merchant.multisafepay.com) and in the settings of any plugins.
- Correctly processed in the transaction [API request](/api/#orders).

## Enabling currencies in your MultiSafepay account

To view the currencies currently enabled in your MultiSafepay account, go to **Finance > Balance**.

To enable new currencies in your MultiSafepay account, email the Support Team at <support@multisafepay.com>

You must also add a business bank account that supports the currency to your MultiSafepay account. Follow these steps to ensure transactions can be processed in that currency and no conversion is required:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Finance > Balance > Add bank account**.
3. Process a bank transfer in the new currency to confirm the business bank account.

Once your new business bank account has been approved by the Risk Team, you can process payouts without currency conversion.

## Converting currency in your MultiSafepay account

To convert other currencies to Euros (EUR)in your [MultiSafepay account](https://merchant.multisafepay.com), go to **Finance > Currency conversion**. 

Take into account the exchange rate and/or any other costs.

For any questions, email the Support Team at <support@multisafepay.com>