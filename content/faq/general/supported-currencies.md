---
title : "Supported currencies"
weight: 8
meta_title: "FAQ General - Supported currencies - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases: 
    - /faq/general/which-currencies-are-supported-by-multisafepay
    - /faq/general/currencies-supported
---

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

## Currencies on request

MultiSafepay can accept currencies for Visa, MasterCard, and Maestro not in the preceding list on request.

To request support of another currency, email the Support Team at <support@multisafepay.com>

## Requirements

* We can only process currencies supported by the specific [payment method](/payment-methods).
* The currency must be correctly processed within the transaction call received by MultiSafepay  using [JSON requests](/api/#orders).
* The currency must be enabled in your [MultiSafepay Control](https://merchant.multisafepay.com) and in the settings of any plugins.

**Note:** All currencies enabled in your MultiSafepay Control are listed under **Finance > Balance**.  

## Enabling currencies in your MultiSafepay Control

To enable new currencies in your MultiSafepay Control, email the Support Team at <support@multisafepay.com>

## Payout currency options

The standard currency for processing all incoming and outgoing transactions is Euros (EUR). To process payouts in other currencies, you must specify a business bank account that can receive funds in that currency.

Automatic withdrawals are also in Euros. You must schedule withdrawals in other currencies manually. 

For more information about automatic and manual withdrawal, see FAQ Finance – [Paying out funds from your MultiSafepay account](/faq/finance/paying-out-funds-from-your-multisafepay-control/). 

## Adding multi-currency business bank accounts to your MultiSafepay Control

When requesting to add an extra currency to your MultiSafepay Control, follow these steps to ensure transactions can be processed in that currency and no conversion is required:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. To add a business bank account that can receive the new currency, go to **Finance > Balance > Add bank account**.
3. Process a bank transfer in the new currency to confirm the business bank account.
4. The Risk Team finalizes your request.

## Adjusting payout settings in your MultiSafepay Control

* In your [MultiSafepay Control](https://merchant.multisafepay.com), you can convert other currencies to Euros (EUR). Take into account the exchange rate and/or any other costs. Go to **Finance > Currency Conversion**. 

* Once your new business bank account has been approved by the Risk Team, you can process payouts without currency conversion.

For example, the currency dollar (USD) is paid out in dollar (USD) and also received on your business bank account in dollars (USD).

For questions about currencies and options in your MultiSafepay Control, email the Support Team at <support@multisafepay.com>
