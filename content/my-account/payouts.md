---
title: "Payouts"
category: 62962dcdbccb9a001d4bbc81
order: 207
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'payouts'
---
A payout is when you transfer funds from your account balance to your business bank account.

You can make payouts any time for 0,50 EUR each.

# Business bank accounts
As part of your onboarding, you specify a business bank account to pay out to. 

<details id="how-to-add-additional-bank-accounts">
<summary>How to add additional bank accounts</summary>
<br>

To add additional bank accounts to your account (once fully onboarded), follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com). 
2. Go to **Finance** > **Bank accounts**.
3. Click **Add new bank account**.
4. Fill in the:
    - **Account holder name**
    - **IBAN**
5. From the **Currency** list, select the currency of the bank account.
6. Click **Save**.
7. To verify the account, on the **Business bank account** page either:
    - Make a payment of 1 EUR from the business bank account via iDEAL or Bank Transfer to your account balance, **or**
    - Upload a copy of a bank statement. Select the file, and then click **Upload**.
    **Note:** The company name on the bank statement must exactly match one of the trade names on your Chamber of Commerce extract.

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

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com). 
2. Go to **Finance** > **Payouts**.
3. Under **Automatic withdrawals**, click **+ Add**.
4. In the **Automatic withdrawals** window:
    - Under **Select days**, select a specific day of the week, or the end of the month. 
    - From the **Select currency** list, select the currency. 
    - If you want to schedule withdrawals only when your balance exceeds a specified amount, in the **Withdraw when balance exceeds** fields, enter the amount. 
    - If you want to specify a minimum amount to retain in your balance, in the **Reserve amount** fields, enter an amount.
    - From the **Select the account number** list, select the business bank account number you want to transfer the withdrawal to.
5. Click **Schedule payments**.

**Note:** To schedule payouts for different currencies, you must have a account balance and an active business bank account for each currency.

<img class="-radius max-width medium-img" src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Screenshot-Automatic-Withdrawals.png" alt="Screenshot of an automatic withdrawal in the MultiSafepay dashboard" >

</details>

<details id="how-to-make-a-payout-manually">
<summary>How to make a payout manually</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Finance** > **Payouts**.
3. Under **Withdraw funds**:  
    - Select the currency.
    - Enter an amount.
    - Click **Withdraw funds**.
4. Check the details of the payout, and then click **Submit**.
5. From the **Select bank account** list, select the business bank account number you want to transfer the withdrawal to. 
6. Click **Continue**.

</details>

# Currencies
The standard currency for automatic payouts is euros (EUR). For manual payouts, you can process other currencies if you specify a business bank account that can receive funds in that currency.

<details id="supported-currencies">
<summary>Supported currencies</summary>
<br>

You can make payouts in: 

- AUD (Australian dollar)
- CAD (Canadian dollar)
- CHF (Swiss franc)
- DKK (Danish krone)
- GBP (Pound Sterling)
- HKD (Hong Kong dollar)
- NOK (Norwegian krone)
- PLN (Polish złoty)
- SEK (Swedish krona)
- USD (United States dollar)

</details>

# Processing times 
The time taken to process payouts is determined by the Risk Team. The default payout delay is 1 day. 
Payouts may take up to three business days to arrive in your business bank account.

Payment batches are not processed on weekends. That is, payouts initiated on Fridays are processed on Monday morning.

Not all banks support instant payments and therefore may take extra time to process payments.

### Bank holidays

MultiSafepay pays out every business day of the year, but **not** on bank holidays. Delayed payouts are made the next business day. 

Check the dates of local bank holidays. They may change each year.

### Automatic payouts

Assuming default settings, if you schedule a payout on Monday, the payout batch includes all payments up to 23:59 hours on the Monday night. The payout batch is sent to MultiSafepay's bank on Tuesday morning. Our bank processes the batch and transfers the pay out to your business bank account. You should receive the payout on Tuesday afternoon.

### Manual payouts

The status of the pay out is **Reserved** for 24 hours before it is added to our bank’s payout batch in the morning. Then, the payout is transferred to your business bank account. Manual payouts usually take longer to process than automatic ones.

# Exclusions

You cannot make payouts if:

<details id="your-multisafepay-account-is-not-yet-fully-activated">
<summary>Your MultiSafepay account is not yet fully activated</summary>
<br>

You can process payments immediately after creating a MultiSafepay test account and adding your site. But MultiSafepay holds your funds in your account balance until your account is fully activated.

To check if your account is fully activated, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Finance** > **Payouts**.
3. If your account is not fully activated, a red bar appears at the top of the screen with a link to the page where you can upload the documents required to approve your account.

The Risk Team then checks and approves your account details and the information on your site. Once approved, we will send you an email that your account is fully activated. 

</details>

<details id="your-account-balance-is-negative">
<summary>Your account balance is negative</summary>
<br>

If your account balance is negative (e.g. due to refunds, chargebacks, or fees), payouts are paused until enough funds are available. 

Always set a "reserved balance" in your payout settings to prevent payout and/or refund delays.
</details>

<details id="your-payouts-are-deactivated">
<summary>Your payouts are deactivated</summary>
<br>

To check why we have deactivated payouts for your account, email <risk@multisafepay.com>
</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]
