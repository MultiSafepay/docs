---
title : "Mastercard status 'declined'. What does this mean?"
weight: 24
meta_title: "Mastercard, what does 'declined' mean? - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---
## Declined
If a Mastercard payment of a customer receives the status _declined_, it may be for several reasons. Only the customer can contact their credit card issuer to inquire as to why the credit card payment has been _declined_.

For questions about credit card payments and/or a payment status (of a credit card transaction), please contact us at <support@multisafepay.com>

In most cases the declined reason is shown behind the declined status within the transaction in your MultiSafepay Control. 

| Transaction status | Reason | Description |
------- |----------|---------|
Declined | transaction not allowed | The fraud filter of MultiSafepay is declining the transaction. Contact our support department at <support@multisafepay.com> for further information.
Declined | Do not honour | This information is not shared with MultiSafepay, only the card holder can retrieve the information at the issuing bank.
Declined | 3D authorisation cancelled | When the [3D Secure](/faq/general/glossary/#3d-secure) verification is incomplete or can not be validated, the payment will be declined.
Declined | Expired card | The credit card is expired.
Declined | Not sufficient funds | The customer has insufficient credit on the credit card to complete the payment.
Declined | Merchant only accepts 3DS verified cards | "Declined, not verified". Submit your request at our Risk Team at <risk@multisafepay.com> when wanting to accept unverified 3D cards. 
