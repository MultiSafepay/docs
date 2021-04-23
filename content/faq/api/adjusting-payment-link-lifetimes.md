---
title: "Adjusting payment link lifetimes"
weight:
meta_title: "FAQ API - Adjusting payment link lifetimes - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
    - /faq/api/lifetime-of-a-payment-link
---
The lifetime of a payment link is how long the link remains valid for the customer to complete the transaction. 

The lifetime is specified in the `days_active` parameter. The `sessionID` for each unique payment link is valid for **30 days** by default. The customer has 30 days to use the link to complete the transaction. Lifetimes can be adjusted, see Adjusting lifetimes below. 

The `seconds_active` parameter is the same as `days_active` but is measured in seconds instead of minutes, e.g. 86.400 `seconds_active` is 1 `days_active`.

If the customer attempts to complete the payment several times, each attempt is registered as a separate transaction (`PSP ID`). If one of the transactions succeeds, all the others remain open until they expire.

You can also cancel payment links.


# Adjusting lifetimes

### Bank transfers
Payment links for bank transfers are valid for **60 days** by default, rather than the standard 30 days. You can adjust the liftetime in the bank transfer email sent to the customer by setting a `days_active` or `seconds_active` parameter. The transaction then remains active for 60 days, and the payment link expires after the default 30 days. 

### PayPal    
PayPal sets a payment link lifetime limit of **14 days**. This is less than MultiSafepay's default lifetime. You can only use the `days_active` and `seconds_active` parameters to adjust the lifetime of a PayPal payment link within 14 days. 

### Post-payment methods 
By default, you cannot adjust payment link lifetimes for post-payment methods, which have their own payment flow.

For more information about payment link lifetimes, see API - [Days Active, Seconds Active](/api/#days-active-seconds-active).

### Second Chance emails
[Second Chance](/tools/second-chance) emails include a payment link as a gentle reminder to the customer, and they can complete the payment if they choose. 

We send two Second Chance emails: one after 1 hour and the other after 24 hours. This cannot be adjusted. You can only enable or disable Second Chance. 

You cannot edit the payment link in Second Chance emails, because the `session_id` of the initial transaction has already been used. You can only edit the link in the initial request. 

But you can adjust the payment link lifetime using the `days_active` or `seconds_active` parameters. If `days_active` or `seconds_active` is set for under 24 hours, the payment link displays an error message when opened. 

**Example 1:**      
When `days_active` is set to 2, the payment link automatically expires after 2 days, after which the customer can no longer complete the payment. This ensures that the stock is reversed after the payment link expires.

**Example 2:**    
If `seconds_active` is set under 86400 seconds (24 hours), the second email is still sent, even though the payment link it contains is no longer valid. This can't be changed. 




