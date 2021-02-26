---
title : "How do I interpret payments with an uncleared status?"
meta_title: "FAQ Finance - Uncleared Payments - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

## Credit card payments with an Uncleared status

The 'Uncleared' status can be assigned to any credit card payment. In this case, the payment is placed ‘on hold’ by the MultiSafepay fraud filter. Transactions with the status ‘uncleared’ must be evaluated and either accepted or refused by the merchant. We would like to emphasize that our automated fraud filter detects an increased risk of fraud, but it does not prevent all fraudulent payments. On the other hand, not every credit card payment detected by our fraud filter is necessarily a fraudulent payment.

## Pay after delivery payment methods with an Uncleared status

The 'Uncleared' status is also assigned to 'pay after delivery' payment methods. Klarna, Afterpay, in3, Santander and Pay After Delivery will all hold an 'Uncleared' status after shipment of an order. The order status will be _Shipped_, while the transaction status will be _Uncleared_. In this case, the transaction is confirmed and the payout is guaranteed. The _Uncleared_ status will only change to _Completed_ when the payout of a transaction has been received by MultiSafepay and the amount has been added to your MultiSafepay Control balance.

## Why should you check the transaction? 

When you accept payments by credit card, there are risks associated with it. The risk of financial damage, for example by fraud, is carried by the merchant; neither MultiSafepay nor the credit card holder are accountable in this case. When the credit card holder discovers a fraudulent payment, they can demand a refund of the payment, even if products ordered have already been delivered. This is called a ‘chargeback’. More information about chargebacks and the risks of credit card payments can be found on this [page](https://docs.multisafepay.com/faq/chargebacks). On this page, we explain what you need to consider and how to make an informed decision when accepting or refusing uncleared payments.

## Reviewing an uncleared payment

When you log in on MultiSafepay Control, you will see an alert indicating that uncleared payments are awaiting your approval. Click on the notification to go to the list of uncleared payments, then click on a transaction to open it. On this screen you will see the basic information of the transaction and a risk summary on the right. Here you will also find the buttons to accept or decline the transaction. For transactions with a high risk score (score from 8), please contact MultiSafepay in order to evaluate and approve or decline the transaction. To view a detailed risk report, click on the button ‘more information’ when reviewing a transaction in MultiSafepay Control.

## Evaluate the Transaction Amount

Ask yourself if the transaction amount (of a purchase) is higher (or lower) than average. Are you willing to risk that this payment will be revoked after you have delivered your product/service? Consider whether the amount is unusually high compared to the average order value in your online shop.

## Product or service

The risk of fraud also strongly depends on the products or services you offer. Consumer electronics, jewelry and articles by well-known fashion and designer brands are examples of products that are popular among fraudsters. These products are popular because they can be re-sold quite easily. Moreover, expensive products are also worth more to sell for fraudsters than cheap products, especially when ordered in large quantities. Ask yourself the following:

* Is the product easy to re-sell?
* Does the order make sense? 
* Does the product selection or the size of the order differ from usual
orders?

## The customer

View customer information in MultiSafepay Control as well as in your own system. Your own system may provide additional useful information unknown to MultiSafepay. Ask yourself the following questions:

* Do you already know the customer? Is it a good customer or did you experience
problems/challenges in the past?

* Does the customer fit the profile of your average customers, e.g. based on their location, average
order value, etc.?

* Check the email address provided by the customer: is it, for example, a free email service (i.e. Yahoo
or Hotmail?). Fraudsters generally use auto-generated email addresses and free email services.

* In case of doubt, contact your customer. Have you had any contact with the customer in the past?
What is the impression you get from the customer?

* Ask if the customer is willing to complete their order using a different payment method (one with a
payment guarantee, such as a bank transfer). You can also ask your customer for a copy of their ID
card and/or a credit card statement to verify that he/she is indeed the credit card holder.

## 3D secure

3D Secure is an additional security measure intended to reduce fraud. It is an extra step to verify the identity of the actual card holder. The 3D Secure check is performed during the payment process by, for example, filling in an additional password/code or by using a credit card reader. If a credit card has the 3D Secure option, you'll see the status 'Enrolled' in the risk summary when clicking on the transaction in MultiSafepay Control. Please find a list of all ‘Enrolled’ statuses below. In many cases, the transaction has been entered by the card holder. However, there are no guarantees that fraud can be completely prevented. Additionally the card holder may initiate a so-called ‘chargeback’ (or refund of a payment), e.g. when a product has not been received, etc. The 3D Secure verification is an important parameter to consider when reviewing a transaction. When a 3D verification is successfully completed, you are covered against fraud. Please note, however, that 3D verification only covers you for chargebacks performed due to suspected fraud. Chargebacks initiated for other reasons, such as when a customer does not receive his/her product, are not covered by the 3D verification. Additionally, please note that there are still many credit cards in circulation without 3D Secure.

## List of statuses

| 3D Secure result            | Description      |
|---------------------|-----------|
| Enrolled Liability  | 3D Secure available and successfully verified. Liability for fraud is shifted to the cardholder, fraud chargeback is not possible. |
| Not Enrolled, Liability  | 3D Secure available, but not used or successfully verified. Liability for fraud is shifted to the cardholder, fraud chargeback is not possible |
|  No Liability  | No 3D Secure verification available, liability not shifted, fraud chargeback is possible.|

## Risk report

Click on 'View risk report' in MultiSafepay Control for more information about the credit card used for the transaction. Here you will find, among other things, information about the number of credit cards used via a particular IP address, and the amount of credit cards used in combination with a particular email address. Here are some points of attention:

* A fraud score is assigned to uncleared payments. The score indicated the probability of fraud on a scale from 1-10 (10 being the highest score). This does not mean that transactions with score 10 are always fraudulent or that you are not at risk when a low score is assigned; it merely indicates the potential fraud risk (higher or lower).

* Transactions with a score of 6 and above will be assigned the status Uncleared due to increased fraud risk. That does not mean that there is no risk of fraud when transactions do not have an uncleared status. For transactions with a score of 6 to 8, you can choose to accept or cancel the payment yourself in MultiSafepay Control.

* Transactions with a fraud score of 8 or higher can only be approved by a MultiSafepay employee. In this case, please contact us so that we may help you assess the potential risks or fraud indicators. As part of our service, we are here to help and offer advice. Please note, however, that the final decision to either accept or reject a transaction lies with the merchant. MultiSafepay is not responsible nor liable for any risks pertaining the acceptance of payments.

* Does the country from the address match the location of the IP address and country in which the credit card was issued? Differences can often be easily explained, e.g. when an order is placed during a vacation or business trip. However it is wise to note where payment was made compared to where the credit card was initially issued. Locations that are far apart, particularly when including high-risk
areas, should always be taken into consideration when assessing a credit card payment.

* Under Fraud info, next to the score, you will find a number of indicators based on the e-mail address and the shipping details.

* Under 'History Data' you will find the number of credit cards used from the same IP address or with the same email address. If this number is high, this may indicate a fraudster. However, a high number can also be explained when the order is placed, for example, from a large business location.

## Conclusion

Accumulatively, these indicators paint an accurate picture of the uncleared transaction. However, these indicators offer no foolproof guarantee against fraudulent transactions. It is essential to consider all factors when evaluating a transaction; how likely is the possibility of fraud, what risks do you face based on your products, order value, etc.? If you trust the payment or consider it ‘low risk’, then you can accept the transaction. If you have any doubt, the transaction can be declined. We recommend that you notify your customer should you decide to reject their transaction.