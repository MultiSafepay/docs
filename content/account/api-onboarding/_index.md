---
title: "Affiliate onboarding via API"
layout: 'single'
logo: "/svgs/Community.svg"
weight: 50
short_description: "Create and onboard affiliated merchant accounts via our API."
url: '/account/affiliate-onboarding-api/'
aliases: 
    - /tools/api-onboarding
---

This page is for MultiSafepay partners wanting to submit onboarding information for new affiliated merchants via our API. 

The API also lets you create a customized onboarding process for new merchants depending on your business model, e.g. marketplaces, franchises, and crowdfunding platforms. This is particularly useful if you are onboarding multiple merchants.  

See also [About account types](/account/partner-account-control/about-account-types/).

## Submitting merchant information

### Step 1: Create a merchant account

See the [Create a merchant account](/account/api-onboarding/create-account) API reference for how to submit the merchant's company details, including:

- Company name and address
- Chamber of commerce number
- VAT number
- Contact details

The API returns an account ID.

### Step 2: Add a bank account
See the [Add bank accounts](/account/api-onboarding/add-bank-accounts) API reference for how to submit information about each bank account added to the merchant account, including: 

- Name of account holder
- IBAN
- Currency

MultiSafepay verifies all bank accounts added to merchant accounts. This can be done in two ways:

- MultiSafepay sends the merchant a payment link for a test transaction of 1 EUR. 
- You send us a bank statement for the merchant's bank account via the API.

The trade name associated with the bank account must exactly match one of the trade names listed in the chamber of commerce extract.

### Step 3: Add UBO details
See the [Add UBOs](/account/api-onboarding/add-ubos) API reference for how to submit details about the [ultimate beneficial owner(s)](/account/ubo/) (UBOs) of the merchant's company, including:

- Name and other identifying information
- Contact details
- Percentage and type of ownership

The API returns a unique UBO identifier, which you can use to submit the UBO's identification documents.

### Step 4: Add a website
See the [Add websites](/account/api-onboarding/add-websites) API reference for how to submit the following information about the merchant's website:

- Website name and URL
- [Notification URL](/developer/api/notification-url)
- Contact details for customer support
 
The API returns an API key. 

## Screening and approval 

After submitting this information, MultiSafepay screens the merchant account, bank account, UBO details, and website. Once approved, the merchant can use their API key to start processing payments.

For more information about the screening process, see Getting started – [Onboard and go live](/getting-started/go-live/).
