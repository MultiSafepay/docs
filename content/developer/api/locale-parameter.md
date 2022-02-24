---
title: "Locale parameter"
weight: 4
meta_title: "Locale parameter - MultiSafepay Docs"
read_more: "."
url: '/developer/locale/'
aliases:
    - /developer/api/locale-parameter/
    - /faq/api/locale
    - /faq/api/using-locale-parameters
    - /developer/api/using-locale-parameters/
---
The `locale` parameter is used to:

- Localize MultiSafepay payment pages for the customer's language, region, and available payment methods.
- Set any special preferences for the user interface.
- Send [email templates](/features/email-templates/) in the customer's preferred language.  
    If an email template is set for a German customer, but the `locale` parameter is set to `en_US`, the English email template is sent instead of the German one.
- Show local variants of specific payment methods, e.g. For Visa:
    - Set to `fr_FR` to display [Cartes Bancaires](/payment-methods/cartes-bancaires).
    - Set to `da_DK` to display [Dankort](/payment-methods/dankort).
    - Set to `it_IT` to display [Postepay](/payment-methods/postepay). 


### Default

If `locale` is left empty or contains a unsupported value, the default is American English: `en_US`.

### Format

Use the format ab_CD where:

- ab = two letter [ISO 639 language code](https://www.iso.org/iso-639-language-codes.html)
- CD = two letter [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html)

## Common values

The table below sets out the codes for commonly used country/language combinations. 

| Country | Language | Locale value |
|---|---|---|
| Austria | German | de_AT |
| Belgium | Dutch, French | nl_BE, fr_BE |
| China | Chinese | zh_CN |
| Denmark | Danish | da_DK |
| Finland | Finnish | fi_FI |
| France | French | fr_FR |
| Germany | German | de_DE |
| Italy | Italian | it_IT |
| Netherlands | Dutch | nl_NL |
| Poland | Polish | pl_PL |
| Spain | Spanish | es_ES |
| Sweden | Swedish | sv_SE | 





 
