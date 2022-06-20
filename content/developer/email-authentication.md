---
title: "Email authentication"
category: 62962df622e99600810c117d
order: 60
hidden: false
---
# Adding SPF records for MultiSafepay emails
Sender Policy Framework (SPF) records let you specify who is authorized to send emails on your domain's behalf. Receiving email servers can check the SPF record to verify the sender. Using an SPF record prevents emails sent by MultiSafepay on your behalf from being marked as spam.

1. Through your hosting provider, domain registrar, or DNS provider, create a DNS TXT record that is named after your domain, e.g. `example.com`.

2. Add either of the following entries to your TXT record containing `v=spf1` and including at least one of the following:
    - `ip4:213.189.0.0/23`
    - `ip4:185.99.128.0/22`
    - `include:spf.multisafepay.com`

    **Note:** The total number of includes permitted is 10, including mx records (if listed).

    You have successfully created an SPF record.

## Examples

### Original TXT record
```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 ~all"
```

### Modified TXT record example 1
```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 ip4:213.189.0.0/23 ip4:185.99.128.0/22 ~all"
```

### Modified TXT record example 2
```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 include:spf.multisafepay.com ~all"
```

## Setting up DKIM email authentication

MultiSafepay supports DomainKeys Identified Mail (DKIM) email authentication for all emails that we send. DKIM lets email servers verify that received emails actually came from the specified domain and haven't been altered or forged.

To set up DKIM you need to add a TXT record for MultiSafepay through your hosting provider, domain registrar, or DNS provider.

### MultiSafepay email servers
1. Add a TXT record named: `msp-2021._domainkey.{your domain}`, e.g. `msp-2021._domainkey.example.com`.

2. Add the following content to your TXT record:
    ```
    v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4pizvsOWTWxtcxthGR0k4rEcGsJH4hRy1fpoUAs3fUi0yMkygwsYUCtFLQY2TwrOtfPfaZ/2bPKXwyjC4kg93zFvSJTIQtQiFfKNT2aDtnDmZRwII4+s2k7+LHn4V/SjIxEBylN3Rt0g4iVlkZzgncEXeVksXj5eux8uDAUeZxj0Fp8PWSkxsBNVaJFb5sfR+c5piJ+8RmlqYUf7w/gXOW8mChC509//V9dfMaV39b7WoEf/JRw9KGM69C3hIdtb7cVKD/B6VxQIq3z1DCAcmSCXpcaXUaFbVaF4u/vEi+3v5DdPtDl/0rOy2NUFNL5XULW8OxdofzUbdL9SWN/IbwIDAQAB;
    ```
You have successfully added a TXT record for MultiSafepay's email servers.

### Mandrill

If you have [E-Invoicing](/payment-methods/e-invoicing/) or [Pay After Delivery](/payment-methods/pay-after-delivery/) activated, we also use Mandrill to send emails in addition to our own mail servers. In this case, you need to add another TXT record for Mandrill.

1. Add a TXT record named: `mandrill._domainkey.{your domain}`, e.g. `mandrill._domainkey.example.com`.

2. Add the following content to your TXT record:
    ```
    v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrLHiExVd55zd/IQ/J/mRwSRMAocV/hMB3jXwaHH36d9NaVynQFYV8NaWi69c1veUtRzGt7yAioXqLj7Z4TeEUoOLgrKsn8YnckGs9i3B3tVFB+Ch/4mPhXWiNfNdynHWBcPcbJ8kjEQ2U8y78dHZj1YeRXXVvWob2OaKynO8/lQIDAQAB;
    ```
You have successfully added a TXT record for Mandrill.
