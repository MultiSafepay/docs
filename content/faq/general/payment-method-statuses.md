---
title: "What are the statuses per payment method?"
weight:
meta_title: "FAQ General - Payment method statsuses - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
layout: 'faqdetail'
---


Every payment method comprises of an Order Status as well as a Transaction Status relating to a single order transaction. This section outlines the transaction flow of an order and the different ways a transaction can be processed. This differs per payment method.

* Order Status: The order status indicates the status of the order, such as _Completed_, _Pending_ or _Rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction Status: The transaction status indicates the payment status of the transaction, such as _Completed_, _Pending_ or _Rejected_. Once the transaction status is completed, the amount of the transaction is added to your MultiSafepay balance.

An overview of the statuses per payment method can be viewed in the sub-sections below:


{{< collapse title="Banks" h2="." >}}

### Bank transfer

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized  | Initialized  | A payment link has been generated, but no payment has been received yet.    |
| Completed   | Completed   | A successful Bank transfer transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### Bancontact

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Bancontact transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Declined    | Declined    | Transaction has been rejected   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### Bancontact QR

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Bancontact transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Declined    | Declined    | Transaction has been rejected   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### Belfius

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized  | Initialized  | A payment link has been generated, but no payment has been received yet.   |
| Completed   | Completed   | A successful Belfius transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### CBC

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful CBC transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.                                                      |

### Dotpay
| Order Status | Transaction Status | Description                                                                                                          |
|--------------|------------------|----------------------------------------------------------------------------------------------------------------------|
| Initialized  | Initialized      | A payment link has been generated, but no payment has been received yet.                                             | 
| Completed    | Completed        | A successful Dotpay transaction has been received and the funds will be added to your MultiSafepay Control balance.  | 
| Declined     | Declined         | Transaction has been rejected.                                                                                       | 
| Expired      | Expired          | An unfinished transaction will automatically expire after a predefined period.                                       | 
| Void         | Cancelled         | Transaction has been cancelled.                                                                                     | 

### EPS

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful EPS transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### Giropay

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Giropay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Declined    | Declined    | Transaction has been rejected   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### iDEAL

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful iDEAL transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### iDEAL QR

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful iDEAL QR transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### ING Home'Pay

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful ING Home'Pay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### KBC

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful KBC transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### Request to Pay

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | Customer is redirected to the Deutsche Bank payment page  | 
| Uncleared   | Completed   | The payment has been authorised and successful. The customer is redirected back to MultiSafepay   | 
| Completed   | Completed   |  Transaction is on credit notification. For banks that support instant SEPA credit transfers, the credit notifications can be immediate, otherwise this will be done within the next 24 hours.  | 
| Expired   | Expired    | The customer does not complete the payment on the Deutsche Bank payment interface. | 
| Declined     | Declined     | Deutsche Bank or the customer bank rejects the payment.  | 
| Void        | Void    | The customer cancels the payment on the Deutsche Bank payment interface.   | 


### SEPA Direct Debit

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized   | Initialized    | Created but not yet processed by the bank.   |
| Uncleared     | Uncleared      | Processed by the bank waiting for clearing period (depending on amount and settings of the merchant).   |
| Completed     | Completed      | Payment has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Declined      | Declined       | Rejected during uncleared period.   |
| Cancelled      | Cancelled       | Transaction has been cancelled or incorrectly entered by webshop                             |

### TrustPay

| Order Status | Transaction Status | Description                                                                                                          |
|--------------|------------------|----------------------------------------------------------------------------------------------------------------------|
| Initialized  | Initialized      | A payment link has been generated, but no payment has been received yet.                                             | 
| Completed    | Completed        | A successful Trustpay transaction has been received and the funds will be added to your MultiSafepay Control balance.  | 
| Declined     | Declined         | Transaction has been rejected.                                                                                       | 
| Expired      | Expired          | An unfinished transaction will automatically expire after a predefined period.                                       | 
| Void         | Cancelled        | Transaction has been cancelled.                                                                                       | 

### Trustly

| Order Status | Transaction Status | Description                                                                                                                       |
|--------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Initialized  | Initialized      | A payment link has been generated, but no payment has been received yet.                                                          |
| Completed    | Completed        | A successful Trustly transaction has been received and the funds will be added to your MultiSafepay Control balance.              |
| Declined     | Declined         | Transaction has been rejected.                                                                                                    |
| Uncleared    | Uncleared        | Transaction is successful, but awaiting payment confirmation from Trustly. |
| Expired      | Expired          | An unfinished transaction will automatically expire after a predefined period.                                                    |
| Void         | Cancelled        | Transaction has been cancelled.                                                                                                   |


{{< /collapse >}}

{{< collapse title="Credit and Debit Cards" h2="." >}}

### American Express

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful American Express transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)  | 
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 


### Maestro

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet. | 
| Completed   | Completed   | A successful Maestro transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 
| 

### Mastercard

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Mastercard transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)  | 
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 
| 

### V Pay

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet. | 
| Completed   | Completed   | A successful V Pay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 
| 

### Visa

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Visa transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)  | 
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 
| 

{{< /collapse >}}

{{< collapse title="Billing Suite" h2="." >}}

### AfterPay

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Uncleared  | Uncleared  | When an AfterPay transaction is marked with the status uncleared, AfterPay will authorize or decline the transaction. No action is required.   |
| Completed  | Uncleared  | A successful AfterPay transaction has been received.   |
| Shipped    | Uncleared  | A capture has been send to AfterPay, the transaction has been confirmed. An invoice will be sent to the customer and your payout is guaranteed. |
| Shipped    | Completed  | Payout of an AfterPay transaction has been received and added to your MultiSafepay Control balance.|
| Declined   | Declined   | Transaction has been rejected by AfterPay. Behind the declined status in your [MultiSafepay Control](https://merchant.multisafepay.com), the reason of rejection is shown.     |
| Void       | Cancelled   | Transaction has been cancelled.  | 
| Expired    | Expired    | When no action is being taken within 90 days of receiving a transaction with the payment method AfterPay, the transaction will automatically expire. | 

### Betaal per Maand

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Uncleared   | Uncleared  | When a Betaal per Maand transaction is marked with the status uncleared, Betaal per Maand will authorize or decline the transaction. No action is required.   |
| Uncleared   | Initialized | A payment has been initiated, but no payment has been received yet.  | 
| Completed   | Uncleared  | A successful Betaal per Maand transaction has been received.   |
| Shipped     | Uncleared  | A Capture has been send to Betaal per Maand, the transaction has been confirmed. An invoice will be send to the customer and your payout is guaranteed. |
| Shipped     | Completed  | Payout of a Betaal per Maand transaction has been received and added to your MultiSafepay Control balance.|
| Declined    | Declined   | Transaction has been rejected by Betaal per Maand. Behind the declined status in your [MultiSafepay Control](https://merchant.multisafepay.com), the reason of rejection is shown.     |
| Void        | Cancelled   | Transaction has been cancelled.  | 
| Expired     | Expired    | When no action is being taken when receiving a transaction with the payment method Betaal per Maand, the transaction will automatically expire. | 

### E-Invoicing

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Completed   | Initialized | A successful E-Invoicing transaction has been received.    | 
| Shipped     | Initialized   | A Capture has been sent to E-invoicing, the transaction has been confirmed. An invoice will be send to the customer. |
| Shipped     | Completed    | Payout of an E-Invoicing transaction has been received and added to your MultiSafepay Control balance.  |
| Declined    | Declined    | Transaction has been rejected.  | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### in3

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized  | Initialized  | The customer is redirected to in3 and a credit check is conducted.   |
| Declined  | Declined  | The credit check has been declined.   |
| Completed    | Uncleared  | The payment has been successful. |
| Void    | Void  | The payment has been declined or abandoned.|
| Uncleared   | Initialized   | The payment is awaiting and the customer has 5 minutes to complete the payment, otherwise the transaction will be cancelled.  |
| Completed       | Completed   | The transaction has been settled and is complete.  | 

### Klarna

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized   | Initialized  | A Klarna transaction has been initiated by the customer.   |
| Completed  | Uncleared  | A successful Klarna transaction has been placed. The order is awaiting shipment. A payment has not yet been received by Klarna.   |
| Shipped    | Uncleared  | A capture has been sent to Klarna, the transaction has been confirmed. An invoice will be sent to the customer and your payout is guaranteed. |
| Shipped    | Completed  | Payout of a Klarna transaction has been received and added to your MultiSafepay Control balance.|
| Declined   | Declined   | Transaction has been rejected by Klarna. Behind the declined status in your [MultiSafepay Control](https://merchant.multisafepay.com), the reason of rejection is shown.     |
| Void       | Cancelled   | Transaction has been cancelled.  | 
| Expired    | Expired    | When no action is being taken when receiving a transaction with the payment method Klarna, the transaction will automatically expire. | 

### Pay After Delivery

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Uncleared  | Uncleared  | When a Pay After Delivery transaction is marked with the status uncleared, Pay After Delivery will authorize or decline the transaction. No action is required.   |
| Completed  | Uncleared  | A successful Pay After Delivery transaction has been placed.   |
| Shipped    | Uncleared  | A capture has been sent to Pay After Delivery, the transaction has been confirmed. An invoice will be sent to the customer and your payout is guaranteed. |
| Shipped    | Completed  | Payout of a Pay After Delivery transaction has been received and added to your MultiSafepay Control balance.|
| Void       | Cancelled   | Transaction has been cancelled.  | 
| Expired    | Expired    | When no action is being taken within 90 days of receiving a transaction with the payment method Pay After Delivery, the transaction will automatically expire. | 


{{< /collapse >}}

{{< collapse title="Wallet" h2="." >}}

### Apple Pay

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated to initialize an Apple Pay payment, but no payment has yet been received.  | 
| Completed   | Completed   | A successful Apple Pay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)  | 
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Void    | Transaction has been cancelled.   | 

### Alipay

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Alipay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Declined    | Declined    | Transaction has been rejected   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

### PayPal


| Order Status                   | Transaction Status         | Description |
|--------------------------------|--------------------------|-----------------------------------------------------------------------------------------|
| Initialized                    | Initialized              | A payment link has been generated, but no payment has been received yet.  | 
| Completed                      | Initialized              | A successful PayPal transaction has been received and the funds will be added to your PayPal balance.   | 
| Declined                       | Declined                 | Transaction has been rejected   | 
| Expired                        | Expired                  | An unfinished transaction will automatically expire after a predefined period.  | 
| Void                           | Cancelled                | Transaction has been cancelled.   | 
| Uncleared                      | Initialized                | An 'Uncleared' transaction without a reason is due to a configuration in your PayPal business account. The 'Uncleared' transactions are paid in a currency that is not enabled in your PayPal account. It is important to enable that specific currency in your PayPal account in order for the order status to change to 'Completed' in your MultiSafepay Control. |

{{< /collapse >}}

{{< collapse title="Prepaid cards" h2="." >}}

### Gift cards

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Gift card transaction has been received. A payout of a Gift card transaction will be processed by the issuer of the Gift card.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   |

### Paysafecard

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Paysafecard transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Declined    | Declined    | Transaction has been rejected   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

{{< /collapse >}}

If you have any questions about the statuses of a particular payment method, please contact our Integration Team at <integration@multisafepay.com>


