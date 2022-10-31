---
title: "Onboarding affiliates via API"
category: 62962dcdbccb9a001d4bbc81
parentDoc: 62a2055be5b9db006a2545a7
order: 302
hidden: false
slug: 'affiliate-onboarding-api'
excerpt: ''
---

Partner/primary account holders can submit [onboarding information](/docs/onboarding/) for new affiliated merchants via our API.

Create a customized onboarding process for new merchants depending on your business model, e.g. marketplaces, franchises, and crowdfunding platforms. This is particularly useful if you are onboarding multiple merchants.

# Prerequisites 

Requests to onboard affiliated merchants via our API require a partner account API key. 
For more information, email your partner manager.

# 1. Create merchant accounts

See API reference – [Create affiliate](/reference/createaffiliate/) for how to submit the company details for each merchant, including:

- Company name and address
- Chamber of commerce number
- VAT number
- Contact details

The API returns a merchant account ID.

# 2. Add a bank account
See API reference – [Add bank account](/reference/addaffiliatebankaccount/) for how to submit information about each bank account added to the merchant account, including: 

- Name of account holder
- IBAN
- Currency

MultiSafepay verifies all bank accounts added to merchant accounts. This can be done in two ways:

- We send the merchant a payment link for a test transaction of 1 EUR. 
- You send us a bank statement for the merchant's bank account via our API.

✅ &nbsp; **Tip!** The trade name associated with the bank account must exactly match one of the trade names listed in the chamber of commerce extract.

# 3. Add UBO details
See API reference – [Add UBO](/reference/addaffiliateubo/) for how to submit details about the ultimate beneficial owner(s) (UBOs) of each merchant's company, including:

- Name and other identifying information
- Contact details
- Percentage and type of ownership

The API returns a unique UBO identifier, which you can use to submit the UBO identification documents.

# 4. Add sites
See API reference – [Add site](/reference/addaffiliatesite/) for how to submit the following information about merchants' site(s):

- Site name and URL
- Contact details for customer support
 
The API returns an API key for the site. 

# 5. Screening and approval 

After submitting this information, MultiSafepay screens the merchant accounts, bank accounts, UBO details, and sites. Once approved, the merchants can use their API key to start processing payments.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)