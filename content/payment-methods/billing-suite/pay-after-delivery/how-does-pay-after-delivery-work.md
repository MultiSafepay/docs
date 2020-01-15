---
title : "Pay After Delivery, How it works"
weight: 21
meta_title: "Pay After Delivery, How it works - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
## How it works
Pay After Delivery is a payment method developed and managed by our own MultiSafepay developers. Therefore, the payout of the transaction is guaranteed by MultiSafepay.

Pay After Delivery is an online payment method that allows customers to pay for online purchases after receiving them. A special feature of post-payment is that customers are only charged for the items they keep from an order.

When an uncleared Pay After Delivery is received, no action is required. Our support team will process the transaction within two business days.

The customer has 14 days to complete the payment after receiving the invoice from MultiFactor.

### Shipped status
When receiving a Pay After Delivery transaction, it is important to take the following steps:

Upon agreeing with an order _(by actually sending the goods)_, the order status should be changed from _completed_ to _shipped_.  You can adjust the order status in the original transaction in your [MultiSafepay Control](https://merchant.multisafepay.com) via change order status. Not changing the status to _shipped_ can result in the expiration of the order. If you do not change the order status to _shipped_, the order will eventually expire.

* Changing the status to _shipped_ allows Pay After Delivery to initiate the billing process towards the customer. MultiSafepay will guarantee the payout of the transaction.

The _shipped_ status is therefore important for invoicing the customer and the payout of the transaction on your MultiSafepay balance.


**Complete own funds**      
When the transaction is marked with the _shipped_ status, it is no longer possible to cancel the order. You can, however, close the transaction through the _complete own funds_.      

**Example:**      
In some cases, the customer pays the outstanding amount of the transaction directly to the webshop. This allows you to link the received payment to the outstanding transaction through _Complete own Funds_. Hereby you complete the outstanding transaction. The total amount of the transaction is deducted from your MultiSafepay balance and the transaction is finalized. 

When the customer has not supplied a payment, the transaction can be cancelled by _refund completed order_. This way you credit the invoice to a zero amount and the customer will no longer receive a reminder of the order. 

### Payment flow
As soon as your customer selects the payment method Pay After Delivery, he or she agrees with the terms and conditions. 

1. The shipped status is important for invoicing the customer. 24 Hours after the shipped status has been set, the first email towards the customer will be sent. The customer originally has 14 days to finalize the payment

2. When no payment has been received to complete the transaction, MultiFactor will send a reminder. The second payment request is valid for 6 days     <br>             
_The first and second payment request are sent without additional cost_ 

3. When no payment has been successfully linked to the outstanding transaction after the second payment request, a third reminder will be sent. However, additional cost of &euro; 7.50 will be added to the invoice. <br>
The third payment request will be valid for 6 days

4. The fourth payment request will be increased with &euro; 12.50 and is also valid for 6 days 

5. If, after repeated payment requests, the customer does not complete the outstanding transaction, the total amount of the order will ultimately be transferred to a collection agency.

_A payment link is supplied in every invoice email we send to the customer_


### Payout transaction
The payout of a Pay After Delivery transaction will be added onto your MultiSafepay Balance. A Pay After Delivery payout will be processed 30 days after changing the status to shipped.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Uncleared  | Uncleared  | When a Pay After Delivery transaction is marked with the status uncleared, Pay After Delivery will authorize or decline the transaction. No action is required.   |
| Completed  | Uncleared  | A successful Pay After Delivery transaction has been placed.   |
| Shipped    | Uncleared  | A capture has been sent to Pay After Delivery, the transaction has been confirmed. An invoice will be sent to the customer and your payout is guaranteed. |
| Shipped    | Completed  | Payout of a Pay After Delivery transaction has been received and added to your MultiSafepay Control balance.|
| Void       | Cancelled   | Transaction has been cancelled.  | 
| Expired    | Expired    | When no action is being taken within 90 days of receiving a transaction with the payment method Pay After Delivery, the transaction will automatically expire. | 

#### Refund flow 

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized    | Initialized   | A refund has been requested. | 
| Completed      | Completed     | Refund has been successfully processed. | 


The full API reference for Pay After Delivery can be found [here](/api/#pay-after-delivery).


### Product rules
Some rules may apply to certain payment methods. For Pay After Delivery, the following rules apply:

* Refunding more than the stated amount of the original transaction is not possible with Pay After Delivery. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page.

* Successful Pay After Delivery transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund.

* As a post-payment method, Pay After Delivery has a different payment flow and therefore the setting of days or seconds active will have no influence. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/) FAQ page

* When no action is being taken within 90 days of receiving a Pay After Delivery order, the transaction will expire

* When a Pay After Delivery transaction has the order status _shipped_, there will be no time limit on refunding the transaction

* Pay After Delivery transactions are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay/)

* Currently, Pay After Delivery is only offered in the Netherlands

* As a rule of thumb, post-payment methods do not allow the use of a [giftcard](/payment-methods/gift-cards/) by a customer when filling in the payment details (after the order has already been placed). This has to do with the accuracy of the order specifications, needed by the collecting party (i.e. Pay After Delivery). Our platform would otherwise interpret the giftcard as a discount (which is not present in the shopping cart specification) and would not reflect the right order information needed, for example, for taxation purposes. However, using giftcards for post-payment can be implemented as an option before placing the order (i.e. on your checkout page, before calling our API). It is the merchant's sole responsibility to enable this feature. Failing to comply with this product rule might result in unexpected errors and unwanted complications.

