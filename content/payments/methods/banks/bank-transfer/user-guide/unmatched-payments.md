---
title : "Resolving unmatched Bank Transfer payments"
meta_title: "Resolving unmatched Bank Transfer payments - MultiSafepay Docs"
read_more: "."
weight: 1
url: '/bank-transfer/unmatched-payments/'
---
Read this page in [Dutch](/bank-transfer/ongematchte-bankoverschrijvingen/) or [German](/bank-transfer/unzugeordneten-banküberweisungen/).

When MultiSafepay receives a Bank Transfer payment from a customer, we automatically match it to the corresponding transaction in our system based on the: 

- Amount and payment reference, **or**
- Amount and customer bank account number

If automatic matching fails, we try to match the payment manually.

There are two main reasons why automatic matching fails:

## Payment details incorrect, missing, or incorrectly formatted
We may not be able to match a payment if the customer:  

- Transfers the wrong amount
- Pays for multiple orders in one transfer
- Enters the payment reference number incorrectly, or includes words, e.g. "Payment ID 5213 0452 1234 5670" 
- Provides the order number instead of the payment reference number

Sometimes, the customer's bank has added comments to the transfer.

## Transaction not created

The customer made a transfer but did not:
    
- Place their order with you, **or**
- Click **Confirm** on the MultiSafepay payment page (redirect orders).  

This means the transaction was not created successfully in our system.

To create the transaction again, check if a [payment link](/payment-links/) was created: 

### Payment link created

1. Click the link to open the payment page. 
2. Click **Bank Transfer**.
3. If the customer didn't fill in the **Bank account number** field, enter their bank account number (if known) to help us match the payment.
4. Click **Confirm** to create the transaction in our system.

### Payment link not created

1. [Generate one manually](/payment-links/generating-links/). 
2. Include in the description the customer's name and the order number (for your records). 
3. Click **Bank Transfer**.
4. Add the customer's bank account number (if known) to help us match the payment.
5. Click **Confirm** to create the transaction in our system.

**Note:** The order ID must be unique for each payment link.

## Support

Email the Support Team at <support@multisafepay.com>