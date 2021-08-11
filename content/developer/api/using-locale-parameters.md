---
title: "Using locale parameters"
weight: 4
meta_title: "API Documentation - Using locale parameters - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/api/locale
    - /faq/api/using-locale-parameters
---
`locale` parameters specify the customer's language, region, and any special preferences they want to see in the user interface. You can use them to localize payment pages and send email templates in the customer's preferred language. 

**Note:** If an email template is set for a German customer, but the `locale` parameter is `en_US`, the English email template is sent instead of the German one.

You can also use `locale` to show variants of specific payment methods, e.g.:

* [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires) (fr_FR needed) 
* [Dankort](/payments/methods/credit-and-debit-cards/dankort) (da_DK needed)
* [Postepay](/payments/methods/credit-and-debit-cards/postepay) (it_IT needed)

## Format

Use the format ab_CD with:

- [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) 
- [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html) 

## Default

If `locale` parameters are left empty or contain a unsupported value, the default is American English `en_US`.




 