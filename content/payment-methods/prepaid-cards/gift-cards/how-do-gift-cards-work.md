---
title: "How it works"
weight: 21
meta_title: "How it works - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
# How it works
A gift card can be processed as a digital payment method. The credit on a gift card can be spent in a webshop that accepts the gift card.

With a gift card, the transaction can be paid both in full and partially by the customer.
The remaining amount of the transaction can be fulfilled by any other payment method the webshop is offering to the customer.

The actual payment using a gift card will not be processed by MultiSafepay, but instead by the issuer of the gift card. Therefore, when a gift card payment is successful, MultiSafepay will receive a _completed_ status. MultiSafepay will then process the transaction as paid.

The amount deducted from the gift card to complete a payment will be paid out by the issuer of the gift card.

## Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Gift card transaction has been received. A payout of a Gift card transaction will be processed by the issuer of the Gift card.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

* In case of full payments by means of gift cards, the transaction status will remain _initialized_ in spite of the transaction being **completed**.

### Request refund 
Transactions that are paid in full by means of gift card cannot be refunded via MultiSafepay Control, as there are no available payment details. Therefore, it is advised to process the refund through your own banking environment. 


## Product rules
Some rules may apply to certain payment methods. For gift cards, the following rules apply:

* Refunding more than the stated amount of the original transaction is NOT possible with gift cards. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page

* Payments done by means of gift cards are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay/)

* As a rule of thumb, giftcards cannot be used for (partly) paying for an order placed via a post-payment method. Post-payment methods do not allow the use of a giftcard by a customer when filling in the payment details (after the order has already been placed). This has to do with the accuracy of the order specifications, needed by the collecting party (e.g. Klarna, Afterpay, etc). Our platform would otherwise interpret the giftcard as a discount (which is not present in the shopping cart specification of post-payment methods) and would not reflect the right order information needed, for example, for taxation purposes. However, using giftcards for post-payment can be implemented as an option before placing the order (i.e. on your checkout page, before calling our API). It is the merchant's sole responsibility to enable this feature. Failing to comply with this product rule might result in unexpected errors and unwanted complications.
