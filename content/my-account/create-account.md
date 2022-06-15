---
title: 'Create an account'
category: 62962dcdbccb9a001d4bbc81
order: 100
hidden: false
excerpt: "Choose an account type or a free test account, and sign up."
slug: 'create-account'
---
This page describes MultiSafepay account types and how to create test and live accounts. 

## Account types

There are three types of account: merchant, partner, and primary accounts.

All account types represent a single legal entity, but can support multiple bank accounts and users with their own login credentials and permissions.

Check which type of account best fits your company:

{{< mermaid class="text-center" >}}

flowchart TD
    id1(Do you work with other companies that you charge fees to?)--> id2 & id3
    id2(No= Merchant account)
    id3(Yes. <br> Do you receive part of the MultiSafepay <br> transaction fee from your affiliated companies?)--> id4 & id5
    id4(No= Primary account, <br> e.g. marketplaces, franchises, crowdfunding)
    id5(Yes= Partner account, <br> e.g. digital agencies, SaaS companies)

{{< /mermaid >}}
&nbsp;  

## Test accounts

You may want to start with a test account. This is a free account where you can build and test your integration, explore payment features, and process test transactions. You can then create a live account and [onboard](/account/onboarding-golive/) to start processing real payments.

To create a free test account:

- Fill out the [signup form](https://testmerchant.multisafepay.com/signup).
- Sign in to your [test dashboard](https://testmerchant.multisafepay.com) using the security code we email you.

## Live accounts

To create and [onboard](/account/onboarding-golive/) a live account and start processing real payments, follow these steps: 

**1.** Fill out the relevant signup form: 

|   |  |  | 
|---|---|---|
| Merchant account | [Live signup form](https://merchant.multisafepay.com/signup) | [Test signup form](https://testmerchant.multisafepay.com/signup) |
| Partner/primary account | [Live signup form](https://merchant.multisafepay.com/signup?partner) | [Test signup form](https://testmerchant.multisafepay.com/signup?partner) |

You receive an email containing your **security code**. 

**2.** Use your security code to sign in to your account: 

- [Live account](https://merchant.multisafepay.com/) 
- [Test account](https://testmerchant.multisafepay.com/) 

**3.** Live accounts open by default to the onboarding steps page. You can navigate away from this page, and return to it via the button under **Alert**.

**4.** For partner/primary accounts, an account manager contacts you to confirm the appropriate account structure for your needs, and guide you through the [onboarding process](/getting-started/guide/#5-onboard-your-account).  

For any questions, email <support@multisafepay.com>

## Switching to MultiSafepay from another PSP

You can sign up for a MultiSafepay account while still using another PSP without incurring any costs. A test account lets you process test payments and gives access to all features. MultiSafepay only starts charging monthly fees when you onboard, go live, and begin processing real payments. 

### Transferring tokens
In collaboration with your current PSP, we can securely transfer tokenized credit card details. This is especially useful if you process [recurring payments](/features/recurring-payments/) or want to offer existing customers the option of reusing their credit card details.

For more information, email <sales@multisafepay.com>