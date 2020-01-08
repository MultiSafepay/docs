---
title: "What does Locale do?"
weight:
meta_title: "FAQ API - Locale - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
A _locale_ is a set of parameters that defines the user's language, region and any special variant preferences that the user wants to see in their user interface. Usually a locale identifier consists of at least a language code and a country/region code (e.g. en_US). A _locale_ can be included to provide localized payment pages for the customer. Use the format ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html). This will show the desired language for that customer (if supported by MultiSafepay) on both the payment page and the emails MultiSafepay sends. When left empty or with a unsupported value, en_US, meaning American English, is used.

In some cases, the _locale_ is also used to show certain variants of payment methods, such as:

* [CartaSi](/payment-methods/branded-credit-cards/cartasi-what-is-it/) (it_IT needed)
* [Cartes Bancaires](/payment-methods/branded-credit-cards/carte-bleue-what-is-it/) (fr_FR needed) 
* [Dankort](/payment-methods/branded-credit-cards/dankort-what-is-it/) (da_DK needed)
* [Postepay](/payment-methods/branded-credit-cards/postepay/) (it_IT needed).


The _locale_ is also important for sending the correct email template to the customer. For example, if an email template is set for the German customer, but the locale is received as *en_US*, the email template will be sent in English and not in German. 