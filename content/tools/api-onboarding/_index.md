---
title : Onboarding affiliated merchants via our API
layout : single
tags : hidden
---

This page is for MultiSafepay partners wanting to submit onboarding information about new affiliated merchants through our API. 

The API also lets you create a customized onboarding process for new merchants depending on your business model, e.g. marketplaces, franchises, and crowdfunding platforms. This is particularly useful if you are onboarding multiple merchants.  

### Partner and merchant accounts
Partner and merchant accounts each represent a single legal entity that processes payments. They can support multiple:

- Bank accounts
- Users with their own login credentials and permissions

Partner accounts act as a parent to affiliated merchant accounts and may receive commissions. For more information about commissions, see [Managing commissions](/tools/partner-account-control/managing-commissions).

If you currently have a merchant account, contact your account manager to discuss your options. 
If you don't have a MultiSafepay account, [sign up for a partner account](https://merchant.multisafepay.com/signup?partner).

## Submitting merchant information

### Step 1: Create a merchant account

See the [Create a merchant account](create-account) API reference for how to submit the merchant's company details, including:

- Company name and address
- Chamber of commerce number
- VAT number
- Contact details

The API returns an account ID.

### Step 2: Add a bank account
See the [Add bank accounts](add-bank-accounts) API reference for how to submit information about each bank account added to the merchant account, including: 

- Name of account holder
- IBAN
- Currency

MultiSafepay verifies all bank accounts added to merchant accounts. This can be done in two ways:

- MultiSafepay sends the merchant a payment link for a test transaction of 1 EUR. 
- You send us a bank statement for the merchant's bank account via the API.

The trade name associated with the bank account must exactly match one of the trade names listed in the chamber of commerce extract.

### Step 3: Add UBO details
See the [Add UBO details](add-ubos) API reference for how to submit details about the ultimate beneficial owner(s) (UBOs) of the merchant's company, including:

- Name and other identifying information
- Contact details
- Percentage and type of ownership

The API returns a unique UBO identifier, which you can use to submit the UBO's identification documents.

### Step 4: Add a website
See the [Add websites](add-websites) API reference for how to submit the following information about the merchant's website:

- Website name and URL
- [Notification URL](/faq/api/how-does-the-notification-url-work)
- Contact details for customer support
 
The API returns an API key. 

## Screening and approval 

After submitting this information, MultiSafepay screens the merchant account, bank account, UBO details, and website. Once approved, the merchant can use their API key to start processing payments.

For more information about the screening process, see Getting Started - [Onboarding](https://docs.multisafepay.com/faq/getting-started/onboarding/).

