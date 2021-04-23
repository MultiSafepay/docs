---
title : Onboarding using our API
layout : single
tags : hidden
---

## Introduction

This page is for MultiSafepay partners wanting to onboard new affiliated merchants using our API. Onboarding involves setting up an account and having it screened and approved by MultiSafepay.

Using the API lets you create a customized onboarding flow for your new merchants. This is particularly useful if you need to onboard multiple merchants, e.g. for marketplaces, franchise models, and crowdfunding platforms. 

## Account types
MultiSafepay supports two different account types: merchant accounts and partner accounts. 

### Merchant accounts
Merchant accounts represent a single legal entity that processes payments. Accounts can:

- Manage multiple websites or ecommerce platforms, each with their own API key.  
- Include multiple business bank accounts.
- Support multiple users with their own login credentials and permissions.

### Partner account
Partner accounts act as a parent to one or multiple merchant accounts. Like merchant accounts, partner accounts can be used to process payments. However, in addition, they can  receive funds through commissions. There are three levels at which commissions can be managed:

- **Partner-level**: Use the partner-level settings to set fixed or percentage-based transaction fees that apply to all affiliated merchant accounts.
- **Affiliate-level**: Use the affiliate-level settings to set fixed or percentage-based transaction fees that apply to a specific affiliated merchant account. This overrides the Partner-level settings.
- **Transaction-level**: Use [Split Payments](/tools/split-payments/what-is-split-payments/) to split incoming funds from transactions over multiple accounts (merchant or partner). This feature can be used in combination with Partner- or Affiliate-level fees.

Like merchant accounts, partner accounts represent a single legal entity and allow you to connect multiple bank accounts and users.

For more information, [read about partner accounts](/tools/partner-account-control/).

## Requirements
To use our API for the onboarding of new merchant accounts, you need a partner account. If you currently have a merchant account, ask your account manager what option best suits your business requirements.  
 
If you don't have a MultiSafepay account yet, [sign up for a partner account](https://merchant.multisafepay.com/signup?partner). 


## Overview

Our API allows partner account holders to create affiliated merchant accounts. This is particularly useful when integrating MultiSafepay's onboarding process into your platform's onboarding flow or adding a large number of affiliated accounts.

At its highest level, the onboarding process entails the following steps:

1. [Create a merchant account](#create-a-merchant-account)
2. [Add a bank account](#add-a-bank-account)
3. [Add UBO details](#add-ubo-details)
4. [Add a website](#add-a-website)

First, create a merchant account, as the returned account identifier is required in the other steps. You can adjust the sequence of the following steps to match your desired onboarding flow.

### Create a merchant account
The first step in the onboarding process is the creation of a merchant account. First, collect general account information from the merchant account holder, including:

- Company address
- Chamber of commerce number
- VAT number
- Contact details

Use the `/signup-account` request to submit the account information. Upon successful submissions, a unique account identifier (`id`) is returned.

[Learn how to create a merchant account with our API](create-account)

### Add a bank account
With a merchant account `id`, one or multiple bank accounts can be added to the account. Adding a bank account requires the following information: 

- Currency
- Name of the account holder
- IBAN

After the bank account is added, it must be verified. This can be done through a payment link or by supplying a bank statement. Both options are accessible through our API.

The trade name associated with the bank account must be an exact match of one of the trade names listed in the chamber of commerce extract.

[Learn how to add bank accounts with our API](add-bank-accounts)

### Add UBO details
With a merchant account `id`, Ultimate Beneficial Owner (UBO) details can be added to the account. These details are required for a merchant account to process payments. UBO details include:

- Personal information
- Contact details
- Type of ownership

Upon successful submissions, a unique UBO identifier is returned. This identifier is used to add identity documents to the associated UBO.

[Learn how to add UBO details with our API](add-ubos)

### Add a website
With a merchant account `id`, one or multiple websites can be added. Collect and submit the following website information:

- Website URL
- Name of the website
- Notification URL
- Support details

Upon successful submissions, a website API key is returned. Once the merchant account, bank account, UBO details, and website have passed our _identification checks_, the website API key can be used to start processing payments.

{{< blue-notice >}}
For more information about the screening process, including the difference between _identification_ and _verification_ checks, read [our documentation on onboarding](https://docs.multisafepay.com/faq/getting-started/onboarding/).
{{< /blue-notice >}}

[Learn how to add a website with our API](add-websites)

---

## Next steps
Now that you know about the different account and have an overview over the onboarding process, it's time to start building your own onboarding flow.

{{< two-buttons href-2="create-account" header-2="Next" text-2="Create a merchant account" img-2="/svgs/arrow-thin-right.svg" alt-2="Arrow right" >}}

