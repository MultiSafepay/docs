---
title : "American Express status 'declined'. What does this mean?"
weight: 24
meta_title: "American Express, what does 'declined' mean? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
aliases: [/credit-and-debit-cards/american-express/american-express-status-what-does-this-mean-/]
---

## Declined
If an American Express payment of a customer receives the status _declined_, it may be for several reasons. Only the customer can contact their credit card issuer to inquire as to why the credit card payment has been _declined_.

For questions about credit card payments and/or transaction statuses, email the Support Team at <support@multisafepay.com>

In most cases the declined reason is shown behind the declined status within the transaction in your MultiSafepay Control. 

| Transaction status | Reason | Description |
------- |----------|---------|
Declined | transaction not allowed | The fraud filter of MultiSafepay is declining the transaction. Email the Support Team at <support@multisafepay.com> 
Declined | Do not honour | This information is not shared with MultiSafepay, only the card holder can retrieve the information at the issuing bank.
Declined | 3D authorisation cancelled | When the [3D Secure](/faq/general/glossary/#3d-secure) verification is incomplete or can not be validated, the payment will be declined.
Declined | Expired card | The credit card is expired.
Declined | Not sufficient funds | The customer has insufficient credit on the credit card to complete the payment.
Declined | Merchant only accepts 3DS verified cards | "Declined, not verified". Email your request to our Risk Team at <risk@multisafepay.com> when wanting to accept unverified 3D cards. 
