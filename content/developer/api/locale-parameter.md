---
title: "Locale parameter"
weight: 4
meta_title: "Locale parameter - MultiSafepay Docs"
read_more: "."
aliases:
    - /faq/api/locale
    - /faq/api/using-locale-parameters
    - /developer/api/using-locale-parameters/
---
The `locale` parameter is used to:

- Localize MultiSafepay payment pages for the customer's language, region, and available payment methods.
- Set any special preferences for the user interface.
- Send [email templates](/features/email-templates/) in the customer's preferred language.  
    If an email template is set for a German customer, but the `locale` parameter is set to `en-US`, the English email template is sent instead of the German one.
- Show local variants of specific payment methods, e.g. For Visa:
    - Set to `fr-FR` to display [Cartes Bancaires](/payment-methods/cartes-bancaires).
    - Set to `da-DK` to display [Dankort](/payment-methods/dankort).
    - Set to `it-IT` to display [Postepay](/payment-methods/postepay). 


### Default

If `locale` is left empty or contains a unsupported value, the default is American English: `en-US`.

### Format

Use the format ab-CD or ab_CD where:

- ab = two letter ISO language code
- CD = two letter ISO country code

## Common values

The table below sets out the codes for commonly used country/language combinations. 

For more countries and languages, see Fincher – [Country code language list](https://www.fincher.org/Utilities/CountryLanguageList.shtml).

| Country | Language | Locale value |
|---|---|---|
| Austria | German | de-AT |
| Belgium | Dutch, French | nl-BE, fr-BE |
| China | Chinese | zh-CN |
| Denmark | Danish | da-DK |
| Finland | Finnish | fi-FI |
| France | French | fr-FR |
| Germany | German | de-DE |
| Italy | Italian | it-IT |
| Netherlands | Dutch | nl-NL |
| Poland | Polish | pl-PL |
| Spain | Spanish | es-ES |
| Sweden | Swedish | sv-SE | 





 
