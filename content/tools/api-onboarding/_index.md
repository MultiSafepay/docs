---
title : Onboarding with our API
layout : single
tags : hidden
---

## Introduction

You can use our API to build your own onboarding flow. This can be useful if your business model involves multiple affiliate accounts that process payments. Examples of such business models include marketplaces, franchise models and crowdfunding platforms. 

{{< blue-notice >}}
This article explains MultiSafepay's account types and provides an overview of the onboarding process. If you are ready to build your own onboarding flow, [learn how to create a Merchant Account with our API](create-account).
{{< /blue-notice >}}

## Account types
Before we get started, it's helpful to understand our two account types.

### Merchant Account
Merchant Accounts are accounts used to process payments. Every Merchant Account represents a single legal entity. However, a Merchant Account can have multiple websites, and thus multiple API keys. This allows a  business to process payments for multiple websites or apps under one account. 

Furthermore, a Merchant Account can add multiple bank accounts, allowing businesses to split payouts over multiple bank accounts. Finally, Merchant Accounts can [add multiple users](/tools/multisafepay-control/users/), allowing multiple people to access the Merchant Account, each with their own login credentials and access rights.

**[Learn more about Merchant Accounts and User Rights](/tools/multisafepay-control/)**

### Partner Account
Partner Accounts act as a parent to one or multiple Merchant Accounts. Like Merchant Accounts, Partner Accounts can be used to process payments. However, in addition, they can  receive funds through commissions. There are three levels at which commissions can be managed:

- **Partner-level**: Use the partner-level settings to set fixed or percentage based transaction fees that apply to all affiliated Merchant Accounts.
- **Affiliate-level**: Use the affiliate-level settings to set fixed or percentage based transaction fees that apply to a specific affiliated Merchant Account. This overrides the Partner-level settings.
- **Transaction-level**: Use Split Payments to split incoming funds from transactions over multiple accounts (Merchant or Partner). This feature can be used in combination with Partner- or Affiliate-level fees.

Like Merchant Accounts, Partner Accounts represent a single legal entity and allow you to connect multiple bank accounts and users.

**[Learn more about Partner Accounts and managing commissions](/tools/partner-account-control/)**

## Requirements
To use our API for the onboarding of new Merchant Accounts, you need a Partner Account. [Create a Partner Account](https://merchant.multisafepay.com/signup?partner), or if you are currently have a Merchant Account, ask your Account Manager what option best suits your business requirements.

## Overview

Our API allows Partner Account holders to create affiliated Merchant Accounts. This is particularly useful when integrating MultiSafepay's onboarding process into your platform's onboarding flow.

At its highest level, the onboarding process involves four steps:

1. **[Create a Merchant Account](#create-a-merchant-account)**
2. **[Add a bank account](#add-a-bank-account)**
3. **[Add UBO details](#add-ubo-details)**
4. **[Add a website](#add-a-website)**

First, create a merchant account, as the returned account identifier is required in the other steps. You can adjust the sequence of the following steps to match your desired onboarding flow.

### Create a Merchant Account
The first step in the onboarding process is the creation of a Merchant Account. First, collect general account information from the Merchant Account holder, including:

- Company address
- Chamber of commerce number
- VAT number
- Contact details

Use the `/signup-account` request to submit the account information. Upon succesfull submissions, a unique account identifier (`id`) is returned.

**[Learn how to create a Merchant Account with our API](create-account)**

### Add a bank account
With a Merchant Account `id`, one or multiple bank accounts can be added to the account. Adding a bank account requires the following information: 

- Currency
- Name of the account holder
- IBAN

After the bank account is added, it must be verified. This can be done through a payment link or by supplying a bank statement. Both options are accessible through our API.

The trade name associated with the bank account must be an exact match of one of the trade names listed in the chamber of commerce extract. For more information, refer to our documentation on our [regular Merchant onboarding](/faq/getting-started/onboarding/#the-checks).

**[Learn how to add bank accounts with our API](add-bank-account)**

### Add UBO details
With a Merchant Account `id`, Ultimate Beneficial Owner (UBO) details can be added to the account. These details are required for a Merchant Account to process payments. UBO details include:

- Personal information
- Contact details
- Type of ownership

Upon succesfull submissions, a unique UBO identifier is returned. This identifier is used to add identity documents to the associated UBO.

**[Learn how to add UBO details with our API](add-ubo)**

### Add a website
With a Merchant Account `id`, one or multiple websites can be added. Collect and submit the following website information:

- Website URL
- Name of the website
- Notification URL
- Support details

Upon succesful submissions, a website API key is returned. Once the Merchant Accoutn, bank account, UBO details and website have passed our _identification checks_, the website API key can be used to start processing payments.

**[Learn how to add a website with our API](add-website)**

{{< blue-notice >}}
For more information about the screening process, read [our documentation on onboarding](https://docs.multisafepay.com/faq/getting-started/onboarding/).
{{< /blue-notice >}}

---

## Getting started
Now that you know about the different account and have an overview over the onboarding process, it's time to start building your own onboarding flow.

{{< two-buttons href-2="create-account" header-2="Next" text-2="Create a Merchant Account" img-2="/svgs/arrow-thin-right.svg" alt-2="Arrow right" >}}

