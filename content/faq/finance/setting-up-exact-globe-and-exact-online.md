---
title : "Setting up Exact Globe and Exact Online"
meta_title: "FAQ Finance - Setting up Exact Globe and Exact Online - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
    - /faq/finance/set-up-exact-online-platform
    - /faq/general/set-up-exact-globe-platform
---

You can export MultiSafepay MT940 accountant reports from your MultiSafepay Control and import them into your Exact Globe or Exact Online account. 

You must first provide Exact with an additional international bank account number (IBAN). This can be a _dummy_, or placeholder, IBAN.  

## Generating dummy IBANs

1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
2. From the **Country** drop-down menu, select **The Netherlands**.
3. Under **Bank Code**, enter a bank, e.g. ING Group.
4. In the **Account number** field, enter any 7 digits.
5. Click **Calculate IBAN**.
6. A dummy IBAN and BIC code are generated.

## Providing dummy IBANs to Exact

| Step  | Exact Globe   | Exact Online   |
|---|---|---|
| 1. | Log in and go to **Bank accounts**. |  Log in and go to **Financial > Banking & Cash > Bank accounts > Overview**. |
| 2. | Click **New**. | Click **New**. |
| 3. | Under **Type**, select **Payment service provider**. | Enter your dummy IBAN. |
| 4. | Enter the dummy IBAN and select the same bank as before, e.g. ING Group.  | Click **Save**.  |
| 5.  | Click **Save**.  |   |

You can now register all transactions linked to this IBAN.

## Exporting from MultiSafepay Control

1. In your MultiSafepay Control, navigate to **Reports > Accountant Export**. 
2. In **Data Selection**, select a date range.
3. In the **Report Type** field, select **MT940**.
4. Click **Advanced options**.
5. In the **Bank Account / IBAN** field, enter the dummy IBAN.
6. In the **BIC** field, enter the dummy BIC code.

## Importing into Exact Online

1. Log in to your Exact Online account.
2. Go to **Financial > Banking & Cash > Statements > Import**.
3. Click **Choose File**, and then select the MT940 file you want to upload.
4. Click **Import**.

Exact Globe and Exact Online both import and match MultiSafepay MT940 reports provided that:

- Your accounting package can process MT940 files.
- The order numbers in the MT940 files also appear in the correct invoice fields in your accounting platform.
- The customer's name and order amounts that appear in the exported MT940 files match your accounting platform.

**Note:** Exact Basic / Standard package doesn't support the MT940 import function. You need at least Exact Advanced.

**Note:** Lightspeed users must request Lightspeed to make an adjustment to make sure order numbers appear in the correct fields in Exact Online to successfully match the MultiSafepay MT940.

