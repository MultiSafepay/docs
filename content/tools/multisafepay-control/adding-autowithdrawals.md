---
title : "Adding auto-withdrawals"
weight: 6
meta_title: "MultiSafepay Control- Adding auto-withdrawals - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/multisafepay-control/autowithdrawl-updates
---

Auto-withdrawals let you schedule withdrawals on a specific day.

**Note:** To schedule auto-withdrawals for different currencies, you must have a MultiSafepay balance and an active bank account for each currency.

To add a new auto-withdrawal, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com). 
2. Go to **Finance** > **Payouts**.
3. Under **Automatic withdrawals**, click **+ Add**.
4. In the **Automatic withdrawals** window:
    - Under **Select days**, select a specific day of the week, or the end of the month. 
    - From the **Select currency** dropdown, select the currency. 
    - If you want to schedule withdrawals only when your balance exceeds a specified amount, in the **Withdraw when balance exceeds** fields, enter the amount. 
    - If you want to specify a minimum amount to retain in your balance, in the **Reserve amount** fields, enter an amount.
    - From the **Select the account number** dropdown, select the business bank account number you want to transfer the withdrawal to.
5. Click **Schedule payments**.

{{< screen src="/img/Screenshot-Automatic-Withdrawals.png" align="center" class="medium-img desktop-radius" >}}