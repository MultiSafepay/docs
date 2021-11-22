---
title : "Unmatched Bank Transfer payments"
meta_title: "Unmatched Bank Transfer payments - MultiSafepay Docs"
read_more: "."
weight: 1
url: '/bank-transfer/unmatched-payments-test/'
tags: "hidden"
---
Read this page in [Dutch] or [German].

## Payment details
The customer receives the following payment details to include when transfering the funds to MultiSafepay: 

{{< screen src="/img/Bank-Transfer-Payment-Details.png" align="left" class="small-img desktop-radius" >}}

You can view these details in your MultiSafepay account, in the relevant **Transaction details** page under **Offline actions**.

## Customers transfering funds
When transfering the funds, the customer must correctly input:  

- The amount
- The payment reference number (16 digits, numbers only, no words)
- Their bank account number (optional, but recommended to help us match payments correctly)

## Matching payments

When MultiSafepay receives the payment (1–3 business days later), we automatically match it to the outstanding transaction in our system based on the details provided. 

If the payment details or amount are missing or incorrect, we try to match the payment manually.

If we cannot match the payment:  

- For smaller amounts, we refund the customer. 
- For larger amounts, we contact you for information to help identify the correct transaction. 

This costs all parties time and effort, and creates a negative customer experience.

## Potential errors

We may not be able to correctly match a payment if the customer has:  

- Transfered the wrong amount
- Made a typing error in the payment reference number
- Added words to the payment reference number, e.g. "Payment ID 5213 0452 1234 5670" 
- Provided the order number instead of the payment reference number
- Paid for multiple orders in one transfer
- Made a transfer but failed to:
    - Place their order with you
    - Click **Confirm** on the MultiSafepay payment page (redirect orders)  
    This means the transaction was not created successfully in our system.

Alternatively, the customer's bank may have added comments to the transfer.

## Potential solutions

### Clear instructions

If emailing the payment details to the customer yourself, make sure you provide clear instructions. 

### Transaction not successfully created

For redirect orders, if a [payment link](/payment-links/) was created: 

1. Click the link to open the payment page. 
2. If the customer didn't fill in the **Bank account number** field, enter their bank account number for them.
3. Click **Confirm** to create the transaction in our system.

If no payment link was created:

1. [Generate one manually](/payment-links/generating-links/). 
2. Include in the description the customer's name and the order number. 
3. Click **Bank Transfer**.
4. Click **Confirm** to create the transaction in our system.

## Support
Email the Support Team at <support@multisafepay.com>
