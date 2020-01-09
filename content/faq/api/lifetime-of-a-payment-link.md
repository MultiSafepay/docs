---
title: "Lifetime of a payment link"
weight:
meta_title: "FAQ API - Lifetime of a payment link - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: "."
---

## The days_active and seconds_active parameters
The parameter <i>days_active</i> indicates the lifetime of a payment link. The unique payment link (session ID) is valid for **30 days** (by default): this means that the customer has 30 days to pay using the link. This period can also be adjusted (see rule exceptions below). 

The parameter <i>seconds_active</i> is equal to the <i>days_active</i>, except that, instead of minutes it is specified in seconds. Example: 86.400 seconds_active is 1 days_active.

It is possible that the customer attempts to pay several times. Each time this occurs, it will be registered as a transaction (PSP ID). When one transaction is successful, all remaining transactions will remain open until they expire. You as a merchant also have the control to cancel a payment link, thus making it void. An order will be completed (order ID) when the order has been successfully paid by the customer using the unique payment link and thus satisfying a single transaction (PSP ID). All remaining non-completed transactions will be updated with the status: **expired**.


## Rule exceptions

### Bank transfer
The payment link for bank transfers is valid for **60 days** (by default) rather than the standard 30 days. However, the payment link included in the bank transfer email sent to the customer can be adjusted by setting a days_active or seconds_active. This means that that the transaction with the bank transfer as a payment method is active for 60 days, while the payment link expires after 30 days by default. 

### PayPal    
A PayPal payment link is valid for **14 days**, as imposed by PayPal. Therefore, PayPal payment links will automatically expire after 14 days, which is less than the default MultiSafepay payment link lifetime. In light of this, the <i>days_active</i> and <i>seconds_active</i> parameters will only have an influence on the lifetime of a PayPal payment link only if they correspond to a period shorter than 14 days. 

### Second Chance email
The [Second Chance](/tools/second-chance/) email is a gentle payment reminder sent to the customer. The Second Chance email will include a payment link, through which customers can finalize the payment if they desire.

When enabled, the Second Chance email will be sent once after 1 hour and once after 24 hours. Currently, this cannot be adjusted. It is, however, possible to influence the lifetime of the payment link by means of the days_active or seconds_active. 

**Example 1:**      
When the days_active is set to 2, the payment link will automatically expire after the two days. The customer will not be able to complete the payment after the expired period. This ensures that the stock is reversed after the payment link expires.

**Example 2:**    
When the seconds_active is set within 84600 seconds (24 hours), the payment link supplied in the second Second Chance email will no longer be valid. The second Second Chance email is sent regardless, this cannot be changed. 

The Second Chance email is sent once after 1 hour and once after 24 hours. This is not adjustable and can only be _enabled_ or _disabled_. If the days_active or seconds_active are set under 24 hours, the payment link will display an error message when opened. 

> **Please note!** When a payment link is set to expire within 24 hours and Second Chance is enabled, the customer will receive an expired payment link in the Second Chance email. 

### Post-payment method 
Post-payment methods are excluded by default when setting a lifetime of a payment link. Post-payment methods have their own payment flow and can therefore not be altered via the <i>days_active</i> and <i>seconds_active</i> parameters.


## API 
Full [API documentation](/api/#days-active-seconds-active) on the lifetime of a payment link can be found on our API page.git a



