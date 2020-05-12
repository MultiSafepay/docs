---
title : "Accepting uncleared credit card payments, how and why?"
meta_title: "FAQ General - Accept an uncleared transaction - MultiSafepay Support"
meta_description: "You can make an informed decision based on the information provided in the Risk Report.
We have explained a number of important verification points to minimize the fraud risk when accepting a credit card payment marked with the status uncleared."
read_more: "."
---
## What is an uncleared transaction?
The status _uncleared_ means that we have received a credit card transaction, but the payment has not been automatically accepted, because our anti-fraud module has detected unusual data. You can find the details of why the transaction has not been accepted under the details or Risk Report. Occasionally, additional information will be added in the Transaction Notes.

It is up to you whether you want to accept or decline the transaction. You can make an informed decision based on the information provided in the Risk Report.


## How to understand an uncleared status?
Because of the fraud risk when receiving and processing credit card payments, we have added a small explanation.
The explanation entails and helps with accepting or rejecting a credit card transaction marked with the status _uncleared_. The responsibility for processing credit card payments lies entirely with the webshop. Therefore, it is up to you whether you want to accept or decline the transaction.

In the Risk Report, we have explained a number of important verification points to minimize the fraud risk when accepting a credit card payment marked with the status _uncleared_.


## Marked with the status uncleared
The so-called _uncleared_ status can be assigned to any credit card payment. In this case, the payment is placed 'on hold’ by the MultiSafepay fraud filter. Transactions marked with the status _uncleared_ must be evaluated and either be accepted or refused by the merchant. We would like to emphasize that our automated fraud filter detects an increased risk of fraud, but it does not prevent all fraudulent payments. On the other hand, not every credit card payment detected by our fraud filter is necessarily a fraudulent payment.


## Why should you check the transaction?
When you accept payments by credit card, there are risks associated with it. The risk of financial damage, for example by fraud, is carried by the merchant; neither MultiSafepay nor the credit card holder are accountable in this case. When the credit card holder discovers a fraudulent payment, they can demand a refund of the payment, even if products ordered have already been delivered. This is called a 'chargeback'.

[Chargeback, what it is](/faq/chargebacks/what-is-a-chargeback/)


## Reviewing an uncleared payment
When a credit card transaction marked with the status _uncleared_ is received, an _uncleared_ status notification is sent to the backend of the webshop. The notification is also visible in your MultiSafepay Control. You will be able to see an alert indicating that uncleared payments are awaiting your approval. Click on the notification to go to the list of uncleared payments, then click on a transaction to open it. In this screen you will see the basic information of the transaction and a risk summary on the right. Here you will also find the buttons to accept or decline the transaction. To view a detailed risk report, click on the _more information_ button when reviewing a transaction in MultiSafepay Control.

Under the contact details in your MultiSafepay Control, you can add an email address to enable receiving email notifications informing you about received uncleared transactions.

#### An uncleared transaction can only be accepted through your MultiSafepay Control. If no action is taken to accept the uncleared transaction, the authorization will automatically expire after 5 days.
***


## Evaluate the Transaction Amount
Ask yourself if the transaction amount (of a purchase) is higher (or lower) than average. Are you willing to risk that this payment will be revoked after you have delivered your product and /or service? Consider whether the amount is unusually high compared to the average order value in your webshop.

## Product or service
The risk of fraud also strongly depends on the products and/or services you offer. Customer electronics, jewelry and pages by well-known fashion and designer brands are examples of products that are popular among fraudsters. These products can be re-sold quite easily. Expensive products are also worth more to sell for fraudsters than cheap products, especially when ordered in large quantities. Ask yourself the following:

- Is the product easy to re-sell?
- Does the order make sense? Does the product selection or the size of the order differ from usual orders?

## The customer
View customer information available in your MultiSafepay Control as well as in your own system. Your own system may provide additional useful information, unknown to MultiSafepay. Ask yourself the following questions:

- Do you already know the customer? Is it a good customer or did you experience problems/challenges in the past?
- Does the customer fit the profile of your average customers, e.g. based on their location, average order value, etc.?
- Check the email address provided by the customer: is it, for example, a free email service. Fraudsters generally use auto-generated email addresses and free email services.
- In case of doubt, contact your customer. What is the impression you get from the customer?
- Ask if the customer is willing to pay with a different payment method. You can also ask for a copy of their ID card and/or a credit card statement. Do mind that the customer is not obliged to deliver.


## 3D secure
3D Secure is an additional security measure intended to reduce fraud. It is an extra step to verify the identity of the actual card holder.

[3D secure, What it is](/faq/general/what-is-3d-secure/)


## List of statuses
|3D Secure Result         | Meaning                                                                                                                                         |
|-------------------------| ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Enrolled Liability      | 3D Secure available and successfully verified. Liability for fraud is shifted to the cardholder, fraud chargeback is not possible.              |
| Not Enrolled, liability | 3D Secure available, but not used or successfully verified. Liability for fraud is shifted to the cardholder, fraud chargeback is not possible. |
| No Liability            | No 3D Secure verification available, liability not shifted, fraud chargeback is possible.                                                       |


## Risk report
Click on 'View risk report' in your [MultiSafepay Control](https://merchant.multisafepay.com/) for more information about the credit card used for the transaction. Here you will find information about the number of credit cards used via a particular IP address and the amount of credit cards used in combination with a particular email address. Here are some points to consider:

- A fraud score is assigned to uncleared payments. The score indicated the probability of fraud on a scale from 1-10 (10 being the highest score). This does not mean that transactions with score 10 are always fraudulent or that you are not at risk when a low score is assigned; it merely indicates the potential fraud risk (higher or lower).
- Transactions with a score of 6 and above will be assigned the status _uncleared_ due to increased fraud risk. That does not mean that there is no risk of fraud when transactions do not have an _uncleared_ status. For transactions with a score of 6 to 8, you can choose to accept or cancel the payment yourself in MultiSafepay Control. MultiSafepay is not responsible, nor liable for any risks pertaining the acceptance of payments.
- Does the country from the address match the location of the IP address and country in which the credit card was issued? Differences can often be easily explained, e.g. when an order is placed during a vacation or business trip. Locations that are far apart, particularly when including high-risk areas, should always be taken into consideration when assessing a credit card payment.
- Under Fraud info, next to the score, you will find a number of indicators based on the email address and the shipping details.
- Under 'History Data' you will find the number of credit cards used from the same IP address or with the same email address. If this number is high, this may indicate a fraudster. However, a high number can also be explained when the order is placed, for example, from a large business location.

## Conclusion
Together, these indicators paint an accurate picture of what uncleared transactions are and how they should be addressed. However, these indicators offer no foolproof guarantee against fraudulent transactions. It is essential to consider all factors when evaluating a transaction; how likely is the possibility of fraud, what risks do you face based on your products, order value, etc.? If you trust the payment or consider it ‘low risk’, then you can accept the transaction. If you have any doubt, the transaction can be declined. We recommend that you notify your customer should you decide to reject their transaction.


