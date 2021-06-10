---
title : "Adding users"
weight: 1
meta_title: "MultiSafepay Control - Adding users - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/multisafepay-control/users
---

You can add an unlimited number of users to your MultiSafepay account. All users on one account share the same secure code. 

You can disable users, but not delete them.

To add users with different permission profiles, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).

2. Go to **Settings** > **User management**.

3. Click **Add new user** in the top right corner.

4. Enter the new user's:

    - User name
    - Full name
    - Password
    - Email address

5. From the **Status** dropdown menu, select **Active**.

6. Under **Rights** on the right side of the page, select the appropriate user rights check boxes. See [User rights overview](#user-rights-overview) below.

7. Click **Add user** in the top right corner.

### User rights overview
    
- Administrator has access to all functionalities in the account
- Reporting can:
  - See all transactions and the account's MultiSafepay balance 
  - Create and download reports
  - Generate payment links
- Technical can:
  - Add and edit websites and payment pages
  - Edit email templates
- Refund can:
  - Create refunds
  - See all transactions
  - Generate payment links
- Basic can:
  - See all transactions
  - Generate payment links
- DisableBalance cannot see the MultiSafepay balance
- Uncleared can accept or decline uncleared transactions
