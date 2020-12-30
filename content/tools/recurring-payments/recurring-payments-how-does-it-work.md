---
title : "Recurring payments, How it works"
weight: 52
meta_title: "Recurring Payments, How it works - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## Recurring payments process
The standard recurring payment process allows you to easily charge your customer on a recurring basis. This is a suitable solution for monthly or annual subscriptions.

The standard process is as follows:

1. The customer creates the original transaction by processing the first payment with a credit card as payment method (Visa, Mastercard or American Express). This is done on the website by selecting a product and/or service, and by finalizing the credit card payment

2. The result of a successful payment is the receipt of the recurring_id in the order details of a successful transaction. Retrieve the order details of a transaction through a _GET request_. For further information on how to retrieve an order available in our [API documentation](/api/#retrieve-an-order)

3. A recurring payment is created using the recurring_id provided in the original transaction. The charge is applied using the same payment details as the initial payment.

### SEPA Direct Debit
Through SEPA Direct Debit, payments from international bank account numbers (IBAN) can be processed, as a one-off or as a recurrent withdrawal. This only applies to private banking. SOFORT Banking and iDEAL are supported as SEPA Direct Debit payment methods.

Full API documentation on SEPA Direct Debit can be found on [SEPA Direct Debit explained](/payment-methods/banks/sepa-direct-debit)

{{< alert-notice >}}  The first payment for a SEPA Direct Debit collection is received and/or processed by the payment methods iDEAL, SOFORT Banking or SEPA Direct Debit. Upon successful completion of the payment, a recurring_id will be displayed in the response upon retrieving the order details only when recurring payment are enbled for that specific MultiSafepay Account.{{< /alert-notice >}} 

{{< alert-notice >}} It is important to note that recurring ID’s retrieved using a credit card cannot be processed when the gateway is set to DIRDEB (SEPA Direct Debit). In this case, the gateway must be set to the specific credit card e.g. ‘VISA’, ‘MASTERCARD’. Thus, only recurring ID’s retrieved by SEPA IBAN payments can be processed by DIREDEB. This allows recurring payments to be deducted with SEPA Direct Debit payment methods such as iDEAL or SOFORT. {{< /alert-notice >}} 

### Pre-notification
According to European law, merchants who use recurring payments should inform their customers about any charges being made. This can be done by email, but it is sufficient to include this in your General Terms & Conditions provided the customer has explicitly agreed to those Terms & Conditions.

### Credit Cards (Visa, Mastercard or American Express)
1. The customer selects a credit card as payment method on the website of the merchant
2. The customer submits a payment
3. If the payment was successful, you will receive a recurring payment ID in the transaction details which can be used for recurring payments.

_**MultiSafepay automatically uses the Site Description and Order ID to show on the customers bank statements. This way the customer can easily recognize the payments**_.

### Retry a failed recurring payment
When the transaction is declined, the reason will be supplied in the response of the transaction. The transaction may, for example, be refused due to insufficient funds. MultiSafepay does not provide automated retry functionality for recurring payments. It is the responsibility of the merchant to contact the customer or try and charge the customer again after a sufficient period of time.


## Create an initial transaction
View the [API documentation](/api) on how to create a standard transaction.

###  The Initial Payment - Status update request
When recurring is enabled in your MultiSafepay Control, you will receive a recurring ID when you do a [retrieve an order request](/api/#retrieve-an-order) 

A sample response is shown below.

```shell 
GET - /orders/{order_id}

  "success": true,
  "data": {
    "transaction_id": "",

```

> Response 

```shell 

"payment_details": {
  "recurring_id": "",

```

### Processing Subsequent Payments - JSON request
The recurring request is similar to the initial payment. However, in order to submit a recurring payment, you need to include the recurring ID in the gateway info section of the request. By including the recurring ID in this request, you do not have to include any bank account or credit card details in the request. An example of this is shown below. You should still offer the customer details, amount and especially an order description.

_**All actual recurring payment transactions use parameter type "direct" instead of "redirect".**_

```shell 

POST - /orders

  "type": "direct", 
  "order_id": "", 
  "recurring_id": "" 

```

Always use the correct payment gateway for each payment method used. Visa, Mastercard or American Express should be sent as gateway within the JSON request. More information about this can be found in the standard integration manual on our [API Documentation page](/api/#recurring-payment).

### Processing recurring payments from another Payment service provider

If you process recurring payments already with another payment service provider, you can not use recurring payments for these customers. However, you can make use of a 'Direct request' [Direct Debit](https://docs.multisafepay.com/api/#direct-sepa-direct-debit) instead with the retrieved IBAN and account holder name.



