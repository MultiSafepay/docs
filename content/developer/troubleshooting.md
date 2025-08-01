---
title: "Troubleshooting"
category: 62962df622e99600810c117d
order: 4
hidden: false
slug: 'troubleshooting'
---
This page lists error codes you may encounter in transaction responses or statuses, or under **Notification history** in your MultiSafepay dashboard, possible causes and how to resolve them.

***

### 1000: Unknown error

An unknown error occurred. Email [integration@multisafepay.com](mailto:integration@multisafepay.com)

***

### 1001: Invalid amount

The `amount` in the create order request was invalid.

All amounts must be given in cents, e.g. 10 EUR = 1000 **not** 10,00.\
The minimum transaction amount is 1 euro cent (0.01 EUR).

***

### 1002: Invalid currency

The `currency` is not supported. The standard currency for all transactions is EUR.

For help identifying currencies, see <a href="https://www.iso.org/iso-4217-currency-codes.html" target="_blank">ISO-4217</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

***

### 1003: Invalid account ID

The `account_id` was invalid.

Check that your account ID is properly formatted.\
Your account ID appears in the top-right corner of your dashboard.

***

### 1004: Invalid website ID

Deprecated: The [`website_id`](/docs/sites#site-id-api-key-and-security-code) was invalid, or doesn’t match the account ID.

***

### 1005: Invalid security code

Deprecated: The [security code](/docs/sites#site-id-api-key-and-security-code) was invalid, or doesn't match the account ID or website ID.

***

### 1006: Invalid transaction ID

The `transaction_id` was invalid.

The transaction ID must be unique. The transaction ID you provided may have already been used for a completed transaction for that website ID.\
Consider creating a new website profile in your dashboard.

***

### 1007: Invalid IP address

The `ip_address` or `forwarded_ip` was invalid.

For <Glossary>BNPL</Glossary> and card orders, we check the customer's IP address as part of our [fraud check](/docs/uncleared/).

***

### 1008: Invalid description

The `description` was missing or invalid.

Enter a free text order description (max. 200 characters), which displays in your dashboard and on the customer’s bank statement (if supported by their bank).

***

### 1010: Invalid variable

The `var1`, `var2`, or `var3` parameter was invalid.

* Any special characters must be UTF-8 encoded.
* The character limit is 100 characters.

***

### 1011: Invalid customer account ID

Deprecated: The customer account ID was missing or invalid.

***

### 1012: Invalid customer security code

Deprecated: The customer security code was missing or invalid.

***

### 1013: Invalid signature

The MD5 signature supplied with the message doesn’t match the message contents for the transaction.

* Check that the values used to calculate the MD5 signature are correct.
* Remove unnecessary blank spaces from the MD5 signature.
* Calculate the MD5 hash from the concatenation of the amount, currency, account ID, website ID, and transaction ID.

***

### 1014: Unspecified error

Check your logs and your MultiSafepay dashboard message screen for other error codes.

For help diagnosing unspecified errors, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

***

### 1015: Unknown account ID

The `account_id` was missing or invalid.

***

### 1016: Missing data

The request is missing required information.

This error most commonly occurs when the customer is directed to a payment page, or when you generate a [payment link](/docs/payment-links/).

Check that you included the [`website_id`, security code](/docs/sites#site-id-api-key-and-security-code), and transaction ID.

***

### 1017: Insufficient funds

The customer has insufficient funds in their MultiSafepay wallet to complete payment.

Advise the customer to top up their MultiSafepay wallet.

***

### 1018: Invalid country code

The `country` was not recognized.

Check that the country code is in correct ISO3166-1 format.

***

### 1019: Website is inactive

The website is blocked in your account.

[Unblock the website](/docs/sites#blockunblock-a-site) in your MultiSafepay dashboard:

***

### 1020: Account is blocked

For security reasons, we have blocked your MultiSafepay account and it cannot process payments.

Email [sales@multisafepay.com](mailto:sales@multisafepay.com)

***

### 1021: Cannot create transaction

Direct requests don't involve a payment page, which means we can't filter out connection errors. This error can cause an increase in unpaid or expired transactions.

Check whether the customer’s bank is experiencing a temporary malfunction.

***

### 1022: Cannot initiate transaction

The transaction may already exist with a third party.

For example, if an iDEAL transaction already exists and another <Glossary>direct</Glossary> iDEAL transaction is initiated, you receive an `Error 1022: Kan geen transactie starten: ERR_EXISTS: transaction error.`

***

### 1023: Gateway unavailable

The `gateway` is unavailable. This error can occur with <Glossary>direct</Glossary> requests.

* Check whether the payment method supports <Glossary>direct</Glossary> requests.
* Ensure you specified a gateway in the create order request.
* Check if the website is correctly configured for <Glossary>direct</Glossary> requests.
* For payment components, check if the correct API token is used. Do not use an API key.

***

### 1024: Transaction declined

For Pay After Delivery and card orders:

* The `customer` data may be incorrect.
* The transaction was flagged in our [fraud check](/docs/uncleared/).
* We considered the customer’s risk profile unacceptable.

Check that the:

* Card details are correct
* Customer details are correct
* Customer details match the credit details

If your are using Cloudflare, the customer's `ip_address` might be overwritten.\
To provide the correct IP address, see Cloudflare – <a href="https://support.cloudflare.com/hc/en-us/articles/200170786-Restoring-original-visitor-IPs" target="_blank">Restoring original visitor IPs</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

**💡 Tip!** For card payments, use the <a href="https://docs.multisafepay.com/reference/getorder" target="_blank">Get order</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> request and check the response details to learn more about the decline reason.

***

### 1025: Multiple currencies in cart

The `shopping_cart` contains multiple currencies.

Ensure all items in the cart use the same currency.

***

### 1026: Cart currency different to order currency

The order `currency` must match the currency of all items in the shopping cart.

***

### 1027: Cart amount must equal order amount

The total order `amount` must be equal to the sum of the items in the shopping cart.

Check that all amounts are correct.

For Pay After Delivery orders, we check the amount for each item, the total amount, and the VAT. Ensure you provide the VAT amount. If no VAT was applied, enter 0%.

***

### 1028: Incorrect custom tax rate

A `tax_tables.rate` is invalid.

Check that the tax rate specified was formatted correctly as #.##, e.g. 0.19.

***

### 1029: Incorrect item tax rate

Some payment methods require in the create order request:

* `tax_table`
* An array of items
* The total amount

This error occurs if the tax rate calculated based on the tax table provided doesn’t match the order items and order total.

We recalculate the amount for each item (excluding tax) and the taxes (only 9% or 21%), and then the total amount. This should match the total order amount.

Check that:

* The tax tables provided match the values used to calculate the tax owing in your <Glossary>backend</Glossary>.
* You provided the amount for all items:
  * Excluding total tax
  * Including total tax

***

### 1030: Incorrect item currency

The `currency` for an item in the shopping cart is not supported in your MultiSafepay account.

For FastCheckout and Pay After Delivery orders, check that the currency is valid.

***

### 1031: Incorrect item price

The `unit_price` of an item in the shopping cart is incorrect.

***

### 1032: Invalid API key

The API key is not valid.

Check that:

* You used the correct [website API key](/docs/sites#site-id-api-key-and-security-code).
* The API key was formatted correctly.
* You used a live key in the live environment, and a test key in the test environment.

***

### 1033: Error fetching refund information

***

### 1034: Cannot refund transaction

The refund cannot be processed.

Check:

* That the sum of any partial refunds doesn’t exceed the original order amount
* That you can make <Glossary>payouts</Glossary> from your account balance
* If the order was cancelled or has already been refunded
* If the same refund was paid within in a short period of time. If a second refund for the same amount is requested within 5 minutes, MultiSafepay rejects the second request to avoid double processing. Refunds sent in batches via the API cause this error because the process is so quick. To avoid this error, delay refund requests by at least 1 second.

***

### 1035: Invalid signature

The MD5 signature supplied with the message doesn’t match the message contents for the transaction.

***

### 1036: Invalid iDEAL issuer ID

The bank identifier for a <Glossary>direct</Glossary> iDEAL transaction was not recognized.

Check:

* The identifier is formatted correctly.
* If you used a real bank identifier in the test environment, or a test identifier in the live environment.

See [List iDEAL issuers](/reference/listidealissuers/).

***

### 5001: Cart data not validated

The `shopping_cart` was not validated when the order was created, and an incorrect amount displayed on the payment page. Email [integration@multisafepay.com](mailto:integration@multisafepay.com)

***

### 9999: Unknown error

An unknown error occurred. Email [integration@multisafepay.com](mailto:integration@multisafepay.com)\ <br />

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:integration@multisafepay.com">[integration@multisafepay.com](mailto:integration@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)