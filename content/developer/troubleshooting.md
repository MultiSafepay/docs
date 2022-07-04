---
title: "Troubleshooting"
category: 62962df622e99600810c117d
order: 40
hidden: false
slug: 'troubleshooting'
---

This page lists errors you may encounter in transaction responses or statuses, or under **Offline actions** in your MultiSafepay dashboard, possible causes and how to resolve them.

---
### Error 1000: Unknown message type

The payment method is disabled or unavailable.

To check the payment method settings for your MultiSafepay account, email <support@multisafepay.com>

---
### Error 1001: Invalid amount

The [create order](/reference/createorder/) request contains an invalid amount.

All amounts must be given in cents, e.g. 10 EUR = 1000 **not** 10,00. 
The minimum transaction amount we can process is 1 euro cent (0.01 EUR).

---
### Error 1002: Invalid currency
  
The currency is not supported. The standard currency for all transactions is EUR.

For help identifying currencies, see [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).

---
### Error 1003: Invalid account ID

The [create order](/reference/createorder/) request contains an invalid account ID.

Check that your account ID was properly formatted, e.g. fix typing errors and remove blank spaces. 
Your account ID appears in the top-right corner of your dashboard.

---
### Error 1004: Invalid site ID

The [create order](/reference/createorder/) request contains an invalid site ID, or the site ID doesn’t match the account ID. 

To retrieve a site ID from your dashboard, go to **Settings** > **Website settings**, and then click the relevant site.

---
### Error 1005: Invalid security code

The [create order](/reference/createorder/) request contains an invalid security code, or the security code doesn't match the account ID or site ID. 

To retrieve a security code from your dashboard, go to **Settings** > **Website settings**, and then click the relevant site.

---
### Error 1006: Invalid transaction ID

The [create order](/reference/createorder/) request contains an invalid transaction ID (PSP ID). 

The transaction ID must be unique. The transaction ID you provided may have already been used for a completed transaction for that site ID. 
Consider creating a new site profile in your dashboard.

---
### Error 1007: Invalid IP address

The `ip_address` or `forwarded_ip` parameter in the [create order](/reference/createorder/) request contains an invalid customer IP address. 

For <<glossary:BNPL>> methods and credit cards, we check the customer's IP address as part of our [fraud check](/docs/uncaptured/).   

---
### Error 1008: Invalid description

The order description in the [create order](/reference/createorder/) request was missing or invalid.

Enter a free text description (max. 200 characters), which appears in the order details in your dashboard and on the customer’s bank statement (if supported by the customer’s bank).    

---
### Error 1010: Invalid variable

The `var1`, `var2`, or `var3` parameter in the [create order](/reference/createorder/) request contains an invalid value.

Check if:

- There are any special characters, which must be UTF-8 encoded.
- The value exceeds the 100 character limit.

---
### Error 1011: Invalid customer account ID

The customer account ID in the [create order](/reference/createorder/) request was invalid or missing.

Check: 

- The account ID exists
- The formatting, e.g. fix typing errors and remove any blank spaces

---
### Error 1012: Invalid customer security code

The customer security code in the [create order](/reference/createorder/) request was invalid or missing.

Check that the security code:

- Matches the account ID
- Is formatted correctly, e.g. fix typing errors and remove any blank spaces

---
### Error 1013: Invalid signature

The MD5 signature supplied with the message doesn’t match the message contents for the transaction.

- Check that the values used to calculate the MD5 signature are correct.
- Remove unnecessary blank spaces from the MD5 signature.
- Calculate the MD5 hash from the concatenation of the amount, currency, account ID, site ID, and transaction ID.

---
### Error 1014: Unspecified error

Check your logs and your MultiSafepay dashboard message screen for other error codes that may be causing this error.

For help diagnosing unspecified errors, email <integration@multisafepay.com>

---
### Error 1015: Account unknown

The account ID in the [create order](/reference/createorder/) request was invalid or missing.

Check that the account ID is formatted correctly, e.g. fix typing errors and remove blank spaces.

---
### Error 1016: Missing data

The [create order](/reference/createorder/) request is missing a required data type. This error most commonly occurs when the customer is directed to a payment page, or when you generate a [payment link](/docs/payment-links/).

Check that the site ID, security code, and transaction ID are included.

---
### Error 1017: Insufficient funds

The customer has insufficient funds in their MultiSafepay wallet to complete payment.

Advise the customer to top up their MultiSafepay wallet.

---
### Error 1018: Invalid country code

The country code in the [create order](/reference/createorder/) request was not recognized.

- Check that the country code is correct.
- Ensure you provide country codes in ISO3166-1 format.

---
### Error 1019: Site is inactive

The site is disabled in your account.

To reactivate the site in your MultiSafepay dashboard:

1. Go to **Settings** > **Website settings**, and select the relevant site.
2. From the **Status** list, select **Active**.
3. Click **Save**.

---
### Error 1020: Account is blocked

For security reasons, we have blocked your MultiSafepay account and it cannot process payments. 

Email <sales@multisafepay.com>

---
### Error 1021: Cannot create transaction

Direct requests don't involve a payment page, which means we can't filter out connection errors. This error can cause an increase in unpaid or expired transactions.

Check whether the customer’s bank is experiencing a temporary malfunction.

---
### Error 1022: Cannot initiate transaction

The transaction may already exist with a third party, e.g. if an iDEAL transaction already exists and another direct iDEAL transaction is initiated, you receive an `Error 1022: Kan geen transactie starten: ERR_EXISTS: transaction error.`

---
### Error 1023: No gateway available

The <<glossary:gateway>> for the payment method is unavailable. This error can occur with direct requests.

- Check whether the specified payment gateway supports direct requests.
- Ensure a gateway was specified in the [create order](/reference/createorder/) request.
- Check if the site is correctly configured for direct requests.

---
### Error 1024: Transaction refused

For Pay After Delivery and credit card transactions:

- The customer data may be incorrect.
- The credit card fraud indicator score indicated that this might be a fraudulent transaction. 
- The customer’s risk profile indicated a high risk of default on a Pay After Delivery transaction.

Check that the:

- Credit card information is correct
- Customer data is correct
- Customer data matches the credit card

---
### Error 1024: For Cloudflare – Incorrect customer IP address

Cloudflare overwrites the customer IP address field.

To provide the correct IP address, see Cloudflare – [Restoring original visitor IPs](https://support.cloudflare.com/hc/en-us/articles/200170786-Restoring-original-visitor-IPs).

---
### Error 1025: Only one currency allowed in shopping cart

The [create order](/reference/createorder/) request contains multiple currencies.

Ensure all items in the shopping cart use the same currency.

---
### Error 1026: Cart currency different to transaction currency

The currency of the transaction must match the currency of all items in the shopping cart.

---
### Error 1027: Cart amount must equal transaction amount

The total transaction amount differs from the sum of the individual items in the order.

Check that all amounts were entered correctly.

For Pay After Delivery payments, the system checks the amount for each item, the total amount, and the VAT. Ensure the VAT amount is provided. If no VAT was applied, enter 0%.

---
### Error 1028: Incorrect tax rate in rule

The [create order](/reference/createorder/) request contains an invalid custom tax rule.

- Check that the tax rate specified was formatted correctly as #.##, e.g. 0.19.
- Fix typing errors and remove blank spaces.

---
### Error 1029: Incorrect tax rate for an item

Some payment methods require in the [create order](/reference/createorder/) request:

- A tax table
- A list of order items
- The total amount 

This error occurs if the tax amount calculated based on the tax table provided doesn’t match the order items and order total. 

We recalculate the amount for each item (excluding tax) and the taxes (only 9% or 21%), and then the total amount. This should match the total order amount. 

Check that:

- The tax tables provided match the values used to calculate the tax owing in your site.
- You provided the amount for all items:  
    - Excluding total tax
    - Including total tax

---
### Error 1030: Incorrect currency for an item

The currency for one item is not supported in your MultiSafepay account.

For FastCheckout and Pay After Delivery transactions, check that the currency is valid.

---
### Error 1031: Incorrect price for an item

The price of an item in the shopping cart in the [create order](/reference/createorder/) request is incorrect. 

Make sure all prices are correct. 

---
### Error 1032: Invalid API key

The API key is not valid for the MultiSafepay account.

Check that:

- The API key was formatted correctly, e.g. fix typing errors and remove blank spaces.
- You used the correct API key for your MultiSafepay account.
- You used a live key in the live environment, and a test key in the test environment.

---
### Error 1033: Error fetching refund information

---
### Error 1034: Cannot refund transaction

The refund cannot be processed.

Check: 

- That the sum of any partial refunds doesn’t exceed the original transaction amount.
- That you can make payouts from your account balance.
- If the transaction was cancelled or has already been refunded
- If the same refund was paid within in a short period of time. If a second refund for the same amount is requested within 5 minutes, MultiSafepay rejects the second request to avoid double processing. Refunds sent in batches via the API cause this error because the process is so quick. To avoid this error, delay refund requests by at least 1 second.

---
### Error 1035: Invalid signature

The MD5 signature supplied with the message doesn’t match the message contents for the transaction.

---
### Error 1036: Invalid iDEAL issuer ID

The bank identifier for a direct iDEAL transaction was not recognized.

Check:

- The value is formatted correctly, e.g. fix typing errors and remove blank spaces.
- If a real bank identifier was used in the test environment, or if a test identifier was used in the live environment.

See [List iDEAL issuers](/reference/listidealissuers/).

---
### Error 5001: Cart data not validated

The cart was not validated when the transaction was created, and an incorrect amount displayed on the bank’s payment page. Email <integration@multisafepay.com>

---
### Error 9999: Unknown error

An unknown error occurred. Email <integration@multisafepay.com>
<br>

---

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a></p>
</blockquote>

[Top of page](#)