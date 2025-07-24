---
title: "Payouts"
category: 627bbcf80c1c9c0050320b60
order: 11
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'payouts'
---
A payout is when you transfer funds from your account balance to your business bank account.

You can make payouts any time for 0,50 EUR each.

# Business bank accounts
As part of your onboarding, specify a business bank account to pay out to. 

<details id="how-to-add-additional-bank-accounts">
<summary>How to add additional bank accounts</summary>
<br>

To add additional bank accounts to your account (once fully onboarded), follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Finances** > **Bank accounts**.
3. Click **Add new**.
4. Fill in the:
    - **Account holder name**
    - **IBAN**
5. From the **Currency** list, select the currency of the bank account.
6. Click **Save**.
7. To verify the account, on the **Business bank account** page either:
    - Make a payment of 1 EUR from the business bank account via iDEAL or a bank transfer to your account balance, **or**
    - Upload a copy of a bank statement. Select the file, and then click **Upload**.
    **⚠️ Note:** The company name on the bank statement must exactly match one of the trade names on your Chamber of Commerce extract.

MultiSafepay verifies the bank account within 5 business days. We **only** accept business bank accounts (no private bank accounts) that are registered to your official company name. 

</details>

<details id="how-to-deactivate-a-bank-account">
<summary>How to deactivate a bank account</summary>
<br>

To deactivate a business bank account, email your request and account ID to <risk@multisafepay.com>

</details>

# Automated and manual payouts

You can schedule automated payouts on specific day, or make them manually. 

<details id="how-to-set-up-an-automated-payout">
<summary>How to set up an automated payout</summary> 
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Finances** > **Payouts**.
3. Under **Automate payout**, click **Add**:
    - Under **Select days**, select one or more days of the week, and/or the end of the month. 
    - From the **Select currency** list, select the currency. 
    - If you want to schedule payouts only when your balance exceeds a specified amount, in the **Pay out when balance exceeds** fields, enter the amount. 
    - If you want to specify a minimum amount to retain in your balance, in the **Set reserve balance** fields, enter an amount.
4. Click **Schedule payouts**.

&nbsp; **💡 Tip!** 
To schedule payouts for different currencies, you must have a account balance and an active business bank account for each currency.
For automated payouts, a report to view all transactions between two payouts will be available. For more information, see [payout report](/docs/reports#payout-report)

<img class="-radius max-width medium-img" src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Screenshot-Automatic-Withdrawals.png" alt="Screenshot of an automatic withdrawal in the MultiSafepay dashboard" >

</details>

<details id="how-to-make-a-payout-manually">
<summary>How to make a payout manually</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Finances** > **Payouts**.
3. Under **One-time payout**:  
    - Select the currency.
    - Enter the amount.
4. Click **Pay out**.

</details>

# Currencies
The standard currency for automatic payouts is euros (EUR). For manual payouts, you can process other currencies if you specify a business bank account that can receive funds in that currency.

<details id="supported-currencies">
<summary>Supported currencies</summary>
<br>

In addition to EUR, payouts can be made in:

- AUD (Australian dollar)
- CAD (Canadian dollar)
- CHF (Swiss franc)
- CZK (Czech koruna)
- DKK (Danish krone)
- GBP (Pound Sterling)
- JPY (Japanese yen)
- NOK (Norwegian krone)
- PLN (Polish złoty)
- SEK (Swedish krona)
- USD (United States dollar)

</details>

# Processing times 

The time it takes to process payouts is set by our Risk Team. The default delay before funds arrive in your business bank account for merchants in:

- Belgium and the Netherlands is 1 business day
- Other countries is 3-5 business days

Payout batches are not processed on weekends. That is, payouts initiated on Friday evenings are processed on Monday mornings.

Not all banks support instant payments and therefore may take extra time to process payouts. 

### Bank holidays

MultiSafepay pays out every business day of the year, but **not** on bank holidays. Delayed payouts are made the next business day. 

Check the dates of local bank holidays. They may change each year.

### Automatic payouts

Assuming default settings, if you schedule a payout on Monday, the payout batch includes all captured payments received up to 23:59 on Sunday night. MultiSafepay then processes this batch and initiates the transfer to your business bank account.

The timing for when you receive these funds will vary depending on the default payout delay set for your account. For more information on your payout schedule, please contact your account manager.

### Manual payouts

The status of the pay out is **Reserved** for 24 hours before it is added to our bank’s payout batch in the morning. Then, the payout is transferred to your business bank account. Manual payouts usually take longer to process than automatic ones.

# Exclusions

You cannot make payouts if:

- Your MultiSafepay account is not yet fully activated.

    <details id="how-to-resolve-account">
    <summary>How to resolve</summary>
    <br>

    You can process payments immediately after creating a MultiSafepay test account and adding your website. But MultiSafepay holds your funds in your account balance until your account is fully activated.

    To check if your account is fully activated, follow these steps:

    1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
       If your account is not fully activated, on the dashboard home page, under **Alerts**, a message appears that your account is incomplete. 
    2. Click **Go to activation**.

    We check and approve your account details and the information on your website. Once approved, we will send you an email that your account is fully activated. 

    </details>

- Your account balance is negative.
    
    <details id="how-to-resolve-balance">
    <summary>How to resolve</summary>
    <br>

    If your account balance is negative (e.g. due to refunds, chargebacks, or fees), payouts are paused until enough funds are available. 

    Always set a "reserved balance" in your payout settings to prevent payout and/or refund delays.
    </details>

- Your payouts are deactivated.
    
    <details id="how-to-resolve-payouts">
    <summary>How to resolve</summary>
    <br>

    To check why we have deactivated payouts for your account, email <support@multisafepay.com>
    </details>
    
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)