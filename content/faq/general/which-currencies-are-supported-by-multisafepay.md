---
title : "Currencies supported by MultiSafepay"
weight:
meta_title: "FAQ General - Currencies - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

MultiSafepay processes the following currencies as standard and available with all payment methods: 

* EUR (Euro)
* GBP (Pound Sterling) 

Those are all the currencies available for Visa, MasterCard and Maestro:

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

## On request currencies

MultiSafepay can accept on request new currencies for Visa, MasterCard and Maestro not listed in the previous list.

## Requirements

* The currency is only processed when it is supported by the selected [payment method](/payment-methods)
* The desired currency is correctly processed within the transaction call, received by MultiSafepay when using [JSON](/api/#orders) requests
* The plugin settings allow the currency selected
* The currency is enabled/allowed within your [MultiSafepay Control](https://merchant.multisafepay.com)

_When multiple currencies are enabled within your MultiSafepay Control, all currencies will be shown under Finance > Balance_.  

## Add currency to your MultiSafepay Balance

In order to enable more currencies in your MultiSafepay Control, please submit your request with our Support department via <support@multisafepay.com>

## Payout currency options

All incoming and outgoing transactions are processed in Euros (EUR) as standard currency. It is possible to manually withdraw a payout in other processing currencies too but automatic withdrawal is available only for EUR (more information on automatic & manual withdrawal methods [here](https://docs.multisafepay.com/faq/finance/how-can-i-pay-out-the-funds-on-my-multisafepay-account-)). To process a payout in another currency, you must provide us with a business bank account that is able to receive funds in the requested currency.

### Add multi-currency business bank account to your MultiSafepay Control

When you request an extra currency to be added to your MultiSafepay Control, you need to follow a few steps in order to ensure transactions can be processed in that particular currency and that no currency conversion is needed:

1. Add a business bank account in your MultiSafepay Control that is able to receive the currency. This can be done through Finance > Balance > Add bank account

2. Process a bank transfer in the requested currency to confirm the business bank account

3. The Risk Team will finalize your request.

### Adjust payout settings in MultiSafepay Control

* Within your [MultiSafepay Control](https://merchant.multisafepay.com), you will have the possibility to convert the currency to Euros (EUR). This can be done through Finance > Currency Conversion. Take into account the exchange rate and/or costs involved

* If a business bank account that can receive the currency as is has been added to your MultiSafepay Control (and approved by our Risk Team), a payout can be processed without currency conversion.

For example, the currency dollar (USD) is paid out in dollar (USD) and received on your business bank account in the dollars (USD) as well.

For any inquiries on currencies and the full functionality of your MultiSafepay Control, our Support team is happy to assist you via <support@multisafepay.com>
