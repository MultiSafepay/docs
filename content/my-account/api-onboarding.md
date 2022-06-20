---
title : "Onboarding affiliates via API"
category: 62962dcdbccb9a001d4bbc81
parentDoc: 62a2055be5b9db006a2545a7
order: 302
hidden: false
slug: 'affiliate-onboarding-api'
---

This page is for MultiSafepay partner or primary account holders wanting to submit onboarding information for new affiliated merchants via our API. 

The API also lets you create a customized onboarding process for new merchants depending on your business model, e.g. marketplaces, franchises, and crowdfunding platforms. This is particularly useful if you are onboarding multiple merchants.  


> 📘 Supported accounts
> 
> Requests to onboard affiliated merchants via our API require a partner account API key. For more information, email your partner manager.

## 1. Create merchant accounts

See API reference – [Create affiliate](https://docs-api.multisafepay.com/reference/createaffiliate) for how to submit the company details for each merchant, including:

- Company name and address
- Chamber of commerce number
- VAT number
- Contact details

The API returns a merchant account ID.

## 2. Add a bank account
See API reference – [Add bank account](https://docs-api.multisafepay.com/reference/addaffiliatebankaccount) for how to submit information about each bank account added to the merchant account, including: 

- Name of account holder
- IBAN
- Currency

MultiSafepay verifies all bank accounts added to merchant accounts. This can be done in two ways:

- We send the merchant a payment link for a test transaction of 1 EUR. 
- You send us a bank statement for the merchant's bank account via our API.

**Note:** The trade name associated with the bank account must exactly match one of the trade names listed in the chamber of commerce extract.

## 3. Add UBO details
See API reference – [Add UBO](https://docs-api.multisafepay.com/reference/addaffiliateubo) for how to submit details about the [ultimate beneficial owner(s)](/account/ubo/) (UBOs) of each merchant's company, including:

- Name and other identifying information
- Contact details
- Percentage and type of ownership

The API returns a unique UBO identifier, which you can use to submit the UBO identification documents.

## 4. Add websites
See API reference – [Add site](https://docs-api.multisafepay.com/reference/addaffiliatesite) for how to submit the following information about merchants' website(s):

- Website name and URL
- Contact details for customer support
 
The API returns an API key for the website. 

## Screening and approval 

After submitting this information, MultiSafepay screens the merchant accounts, bank accounts, UBO details, and websites. Once approved, the merchants can use their API key to start processing payments.

For more information, see [Onboarding process](/account/onboarding-process/).
