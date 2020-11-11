---
title: 'Email template, how does it work'
weight: 6
meta_title: "Email Template Basic Info - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## What is it? 
An email template is a preformatted and/or prewritten email that you can use to replace with your own content so that you can quickly and easily write and create emails.

MultiSafepay offers a number of options for sending a standard email, for example, a successful payment or a reminder email also known as a Second Chance email and many more. 

> MultiSafepay is unable to customize payment pages or email templates for you, although if you do encounter functionality issues, please contact us at <integration@multisafepay.com>

## Set a template
An email template can be set within your MultiSafepay Control under: _**Settings -> Email template -> Select a website -> Add new template.**_ 

The email template has a view options available. A list of the options available are shown and explained below:

1. **Bank transfer details email (to customer)**\
This is a standard email template to provide the customer with the bank details of MultiSafepay upon selecting the Bank transfer as payment method. 

    Because the payment is processed from within the customer's banking environment and not directly on the payment page, the necessary data is sent to the customer by email. With this payment data, the customer can transfer the payment from their own banking environment to MultiSafepay at a desired time.

    MultiSafepay will only sent the email to the customer when the Bank transfer request is recieved as a redirect request. Meaning, the customer is redirected to the payment page of MultiSafepay to confirm the placed order. 

    More information about the payment methods Bank transfer available in [Bank transfer, how does it work?](/payment-methods/bank-transfer/#how-it-works)

2. **Chargeback email (to merchant)**\
This email is intended to inform the merchant that a chargeback has taken place. When you, as a merchant, process credit card payments, it is recommended to activate the option to receive a chargeback notification by email.

     When the standard or personalized chargeback email template is set up, it is important to add an email to your account to which the embedded email template can be sent. Place the desired email address under your contact information -> chargeback email in your MultiSafepay Control. One or more email addresses can be added. 

     More information about Chargebacks available in [What is a chargeback?](/faq/chargebacks/what-is-a-chargeback)

3. **Manual capture reservation completed (to customer)**\
The reserved amount on the customer's credit card has been manually accepted by the merchant. The customer receives a payment confirmation of the accepted payment by mail. 


4. **Manual capture reservation completed (to merchant)**\
The reserved amount on the customer's credit card has been manually accepted by the merchant. The merchant receives a payment confirmation of the accepted payment by mail. 


5. **Partial and/or full capture completed (to customer)**\
The partial or full amount of the reserved amount on the customer's credit card, has been manually accepted by the merchant. The customer receives a payment confirmation of the partially or fully accepted payment by email.


6. **Partial and/or full capture completed (to merchant)**\
The partial or full amount of the reserved amount on the customer's credit card, has been manually accepted by the merchant. The merchant receives a payment confirmation of the partially or fully accepted payment by email.


7. **Refund complete email (to customer)**\
This email is intended to inform the customer that the requested refund has been processed by the merchant. 


8. **Second Chance email (to customer)**\
This email is intended as a friendly reminder to your customer in the event of a payment that has not been completed yet. 

    When the standard or personalized Second Chance email template is set up, it is important to enable the Second Chance in your MultiSafepay Control under **_Settings -> Website settings -> select a website -> enable the Second Chance email per website._**

    More information about the Second Chance email available in [Second Chance, How does it work?](/tools/second-chance/how-does-it-work)

9. **Transaction completed email (to customer)**\
This email is sent to the customer upon successful completion of a payment. 


10. **Transaction completed email (to merchant)**\
This email is intended to informs the merchant by email that the customer has successfully completed a payment.


## The importance of locale
A locale is a set of parameters that defines the user’s language, region and any special variant preferences that the user wants to see in their user interface. Usually a locale identifier consists of at least a language code and a country/region code (e.g. en_US). A locale can be included to provide localized payment pages for the customer. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. This will show the desired language for that customer (if supported by MultiSafepay) on both the payment page and the emails sent by MultiSafepay. When left empty or with a unsupported value, en_US, meaning American English, is used as default.

**For example, if an email template is set for a German customer, but the locale is received as en_US, the email template will be sent in English and not in German.**







