---
title: 'What is a chargeback?'
weight: 11
meta_title: "Credit cards, what is a chargeback? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---


Customers who disagree with or do not recognise a transaction that is charged to their credit card can ask the card issuing bank to raise a dispute. If a dispute is raised, the card scheme (e.g. Mastercard or Visa) will notify MultiSafepay and reclaim the transaction amount from the merchant.

### What is a retrieval?

If a customer does not recognise a transaction that is charged, the cardholder can ask for more information by filing a retrieval request. This process is a pre-chargeback process and can be used to prevent a chargeback process. There are no administrative fees at this point. It is still allowed to perform a refund in this stage.

### I received a chargeback notification, what do I do?

Providing evidence that the chargeback is wrongful is always the responsibility of the webshop.

MultiSafepay can challenge the chargeback on your behalf, but to do so, we need documented proof of the order. This includes:

* An invoice of the order
* Track & trace
* Signed proof of delivery
* Print- screens of (email) contacts you may have had with the cardholder.

The full documentation on how to upload the files via an API request can be accessed [here](/api/#chargeback)

The MultiSafepay chargeback team will decide on whether the chargeback can be challenged, based on the quality of the delivered proof.

The chargeback will be shown in a separate transaction connected to the original transaction in your [MultiSafepay Control](https://merchant.multisafepay.com) However, The required documentation to challenge the chargeback needs to be uploaded in the original transaction.

_Please note: the card scheme will make the final decision_.

### Chargeback rules, why aren't refunds allowed anymore?

As soon as the cardholder sends in the chargeback, he/she will typically be refunded by the issuing bank.
Visa and Mastercard directly reclaim the amount from MultiSafepay and on our turn we debit your MultiSafepay Control balance.

> When you refund a chargeback transaction, the chances are high that the customer will receive the amount twice. Therefore, we do not support a refund of a transaction tied to a chargeback.

### What are the reasons for a chargeback?

The most common chargeback reasons are fraud, non-delivery of goods or goods not as described.

### What can I do to minimize chargebacks?

There are several actions that can be taken to minimize the risk for chargebacks. This starts with good customer service.

Fraud-related chargebacks can be avoided altogether by using [3D Secure](/faq/general/what-is-3d-secure), whereby the cardholder needs to identify him or herself. Fraud-based chargebacks are no longer possible when using the 3D secure.

>It is still possible to receive a chargeback due to non-delivery and goods not as described.
These two reasons are well within your own control.

Non-delivery chargebacks can be minimized by:

* Informing your customer of delivery times, both expected and actual
* Having a well-documented delivery process e.g. by using track & trace with signature
* Refund or cancel the transaction if the goods will not be delivered within the terms of the delivery time or will not be delivered at all.

"Goods not as described" chargebacks can be minimized by:

* Having a clear description on your website and delivering quality goods.

### What happens if I provided proof, but the cardholder still does not agree?

If the customer does not agree with the outcome of the dispute, the process of the chargeback continues. It is possible to challenge the procedure, however the potential cost of doing so is significant.

You will need to present strong evidence of the transaction, that has not been presented before.

Please contact us at <retrieval@multisafepay.com> if you want to proceed and we will assist to the best of our abilities.

### Why can a cardholder initiate a chargeback?

A cardholder can claim a chargeback for a maximum of 180 days after the purchase based on their customer rights given by the card scheme (Visa, Mastercard and American Express).

Longer chargeback initiation periods can be arranged with the card schemes, should the business model of your webshop require (_e.g._ when a yearly subscription has been paid in advance).

By offering credit cards as a payment option in your webshop, you agree to the customer rights that come with credit card acceptance.

### Why do you charge a chargeback handling fee?

If a customer has initiated a chargeback, MultiSafepay will charge a fee to handle the dispute between you and the customer. Visa and Mastercard, as well as the processing bank can also charge fees if the dispute reaches the final stages of where an agreement cannot be reached between you and the customer.<br> 

For more information about these fees, please contact <support@multisafepay.com>
