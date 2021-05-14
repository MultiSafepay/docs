---
title : "Currencies supported"
weight: 8
meta_title: "FAQ General - Currencies supported - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases: 
    - /faq/general/which-currencies-are-supported-by-multisafepay
---

MultiSafepay processes the following currencies as standard for all payment methods: 

* EUR (Euro)
* GBP (Pound Sterling) 

Currencies available for Visa, MasterCard, and Maestro:

* EUR (Euro)
* USD (United States dollar)
* GBP (Pound Sterling)
* VEF (Venezuelan bolívar)
* AUD (Australian dollar)
* BRL (Brazilian real)
* CHF (Swiss franc)
* CLP (Chilean peso)
* COP (Colombian peso)
* CZK (Czech koruna)
* DKK (Danish krone)
* INR (Indian rupee)
* MXN (Mexican peso)
* PEN (Peruvian Sol)
* PLN (Polish złoty)
* RON (Romanian leu)
* SEK (Swedish krona)
* NOK (Norwegian krone)
* CAD (Canadian dollar)
* HRK (Croatian kuna)
* HKD (Hong Kong dollar)
* TWD (New Taiwan dollar)
* KRW (South Korean won)
* HUF (Hungarian forint)
* PHP (Philippine peso)
* ZAR (South African rand)
* CNY (Chinese yuan)
* JPY (Japanese yen)
* MYR (Malaysian ringgit)
* AED (United Arab Emirates dirham)
* ILS (Israeli new shekel)
* RUB (Russian ruble)
* SGD (Singapore dollar)
* NZD (New Zealand dollar)
* TRY (Turkish lira)
* ISK (Icelandic króna)
* THB (Thai baht)

## Currencies on request

MultiSafepay can accept currencies for Visa, MasterCard, and Maestro not in the preceding list on request.

## Requirements

* We can only process currencies that are supported by the specific [payment method](/payment-methods).
* The currency must be correctly processed within the transaction call received by MultiSafepay  using [JSON requests](/api/#orders).
* The currency must be enabled in your [MultiSafepay Control](https://merchant.multisafepay.com) and in the settings of any plugins.

**Note:** All currencies enabled in your MultiSafepay Control are listed under **Finance > Balance**.  

## Adding currencies to your MultiSafepay Balance

To enable new currencies in your MultiSafepay Control, email the Support Team at <support@multisafepay.com>

## Payout currency options

The standard currency for processing all incoming and outgoing transactions are Euros (EUR). To process payouts in other currencies, you must specify a business bank account that can receive funds in that currency.

Automatic withdrawals are also in Euros. You must withdraw payouts in other currencies manually. 
For more information about automatic and manual withdrawal, see FAQ Finance – [Paying out funds from your MultiSafepay account](/faq/finance/paying-out-funds-from-your-multisafepay-control/). 

### Adding multi-currency business bank accounts to your MultiSafepay Control

When requesting to add an extra currency to your MultiSafepay Control, follow these steps to ensure transactions can be processed in that currency and no conversion is required:

1. Add a business bank account in your MultiSafepay Control that can receive the new currency. Go to **Finance > Balance > Add bank account**.

2. Process a bank transfer in the new currency to confirm the business bank account.

3. The Risk Team finalizes your request.

### Adjusting payout settings in your MultiSafepay Control

* In your [MultiSafepay Control](https://merchant.multisafepay.com), you can convert other currencies to Euros (EUR). Take into account the exchange rate and/or any other costs. Go to **Finance > Currency Conversion**. 

* Once your new business bank account has been approved by the Risk Team, you can process payouts without currency conversion.

For example, the currency dollar (USD) is paid out in dollar (USD) and also received on your business bank account in dollars (USD).

For questions about currencies and options in your MultiSafepay Control, email the Support Team at <support@multisafepay.com>
