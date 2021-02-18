---
title : "E-Invoicing, How it works"
weight: 21
meta_title: "E-Invoicing, How it works - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
# How it works
Once E-Invoicing is activated in your MultiSafepay Control, you will need to set it up correctly. Firstly, an action needs to be created. An action will be set as email, text or letter. Multiple actions will become a collection flow. 

A collection flow needs to be linked to a website to be activated. When the collection flow is activated, E-Invoicing will be ready for use as payment method. 

The layout and creation of the email template is entirely your responsibility. You can design the collection flow based on your preferences and personalization requirements. In our email templates, you can use the tokens between @@. Further information is available on our [email template token](/tools/multisafepay-control/email-template-token) page.

## Create action
Each action needs to created following these steps: 

1. Login into your [MultiSafepay Control](https://merchant.multisafepay.com) and navigate to _E-Invoicing → Action_
2. Click on  _Add new template_
3. Select delivery option(s) _email address, SMS or Letter_
4. Provide a description. _Example: NL 1st invoice_
5. Select a language
6. The from address is by default _noreply@multisafepay.com_ When changing the from address, MultiSafepay strongly recommends you add a DNS records to your domain in order to avoid your messages being marked as spam. Further information available in your MultiSafepay Control
7. Enter a from name
8. Provide a subject. _Example: Invoice @sitename@_
9. The Body plain indicates plain (unformatted) text. The layout is entirely up to you
10. The body HTML is also up to you to create and design
11. Create an action for every step in the collection flow. 

Example plain body:      

```shell  
Date: @CURRENTDATE@ 
Order number: @DESCRIPTION@

Subject: your order with @SITENAME@

Dear @FIRSTNAME@ @LASTNAME@,

Thank you for your order at @SITENAME@.

Details of your order:
@CONTENT@

We kindly request you to pay the invoice for @ DUE_DATE @.

Complete your payment using the payment link below
@PAYLINK@ 

Use the following information for a bank transfer:
IBAN: @BANKTRANSFERIBAN@
BIC: ​@BANKTRANSFERBIC@
In the name of: @BANKTRANSFERHOLDER@
Payment reference:​ @BANKTRANSFERID@

Remember to mention the payment reference so that we can link your payment to the correct order. 

Kind regards, 
Your name 
Finance

__
For questions about your order, please contact our customer service via 0208500500 or example@email.nl
```
 
## Create collection flow
Now that the actions have been created, you can follow these steps to create a collection flow:

1. Navigate to _E-Invoicing → Workflows_
2. Select _Create new_
3. In the _Settings_ you can select a template when available 
4. Provide a name for the collection flow in the _Description_. Example: B2B Netherlands
5. Select an action from the _drag and drop_ to start creating a collection flow. Starting with the first invoice and building up the payment flow towards the customer
6. Enabling the _Debt collector_ allows you to hand over the invoice to the collection agency you are working with. Not all merchants decide to hand over the invoice to a collecting agency. This is optional
7. _Manual approval before execution_ is an option that allows you to accept or decline the transaction manually
8. The _Increase transaction fee_ will add an additional amount on top of the original amount. Amount should be formatted in cents ( &euro; 1.00 = 100)
9. Also available is adding a percentage instead of a fixed amount. This can be done through _Increase transaction fee %_
10. The _days active_ specifies how long the payment link is valid
11. There are 2 ways to set the _When_
 - The first is by _X days after previous step_. Select the number of days 
 - Also possible is to select _Day of month (1-28). This allows you to select a specific day of the month to sent the invoice to the customer. This is mostly used with repeated invoices
12. If desired you can select a _Day of the week_
13. Also available to provide a _Execution time_ 
14. _Save_ the communication settings and the first action of the flow is created
15. Repeat for every action you add to the collection flow
16. _Save flow_.


## Getting started
After creating the actions and setting the collection flow, you will be able to use E-Invoicing.

Good to know about the payment method E-Invoicing: 

* Every successful E-Invoicing transaction will be visible in your MultiSafepay Control under _E-Invoicing → Invoices_. A clear overview on the outstanding transactions 

* You can generate a personalized E-Invoice in your MultiSafepay Control. Produce an E-Invoice in your account for your customer under _E-Invoicing → E-Invoicing Generator_. The Invoice created will be sent to the email address supplied. 

* When E-Invoicing is being used for subscription payment, it is possible to generate a batch of transactions with the payment method E-Invoicing. Go to _E-Invoicing → Batches_. Upload a file in .xls, .xlsx or .csv format. Use the template available in your MultiSafepay Control as example.

## Delivery address

MultiSafepay can enable support for different delivery and invoice addresses upon request. Please contact your account manager for more information.

## Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Completed   | Initialized | A successful E-Invoicing transaction has been received.    | 
| Shipped     | Initialized   | A Capture has been sent to E-invoicing, the transaction has been confirmed. An invoice will be send to the customer. |
| Shipped     | Completed    | Payout of an E-Invoicing transaction has been received and added to your MultiSafepay Control balance.  |
| Declined    | Declined    | Transaction has been rejected.  | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 


### Refund flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized    | Initialized | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 

The full API reference for E-Invoicing can be found [here](/api/#e-invoicing)

## Product Rules
Some rules may apply to certain payment methods. For E-Invoicing, the following rules apply:

* Refunding more than the stated amount of the original transaction is NOT possible with E-Invoicing. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Successful E-Invoicing transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* Payments done through E-Invoicing are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay)


* As a post-payment method, E-Invoicing has a different payment flow and therefore the setting of days or seconds active will have no influence. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page

* As a rule of thumb, post-payment methods do not allow the use of a [gift card](/payment-methods/prepaid-cards/gift-cards) by a customer when filling in the payment details (after the order has already been placed). This has to do with the accuracy of the order specifications, needed by the collecting party (i.e. E-Invoicing). Our platform would otherwise interpret the gift card as a discount (which is not present in the shopping cart specification) and would not reflect the right order information needed, for example, for taxation purposes. However, using gift cards for post-payment can be implemented as an option before placing the order (i.e. on your checkout page, before calling our API). It is the merchant's sole responsibility to enable this feature. Failing to comply with this product rule might result in unexpected errors and unwanted complications.

