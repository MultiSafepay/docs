---
title: "Setting up DKIM email authentication"
weight: 12
meta_title: "Setting up DKIM email authentication - MultiSafepay Docs"
read_more: "."
url: '/account/setting-up-dkim/'
---

MultiSafepay supports DomainKeys Identified Mail (DKIM) email authentication on all emails that we send. DKIM allows email servers to verify that emails they receive are actually from that domain and have not been altered or forged.

DKIM authenticates emails through a pair of cryptographic keys. We use the private key to encrypt the email content and generate a DKIM signature before sending. You set the public key in a TXT record through your hosting provider, domain registrar, or DNS provider. This allows receiving email servers to access the public key and use it to verify the integrity of the email and the authenticity of the sender.

## Adding TXT records

We use Mandrill in addition to our own mail servers to send emails. So two TXT records need to be added.

### MultiSafepay email servers
1. Add a TXT record named: `msp-2021._domainkey.{your domain}`, where `{your domain}` contains your domain.
{{< br >}}For example: `msp-2021._domainkey.myamazingwebshop.com`

2. Add the following content to your TXT record:
```
v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4pizvsOWTWxtcxthGR0k4rEcGsJH4hRy1fpoUAs3fUi0yMkygwsYUCtFLQY2TwrOtfPfaZ/2bPKXwyjC4kg93zFvSJTIQtQiFfKNT2aDtnDmZRwII4+s2k7+LHn4V/SjIxEBylN3Rt0g4iVlkZzgncEXeVksXj5eux8uDAUeZxj0Fp8PWSkxsBNVaJFb5sfR+c5piJ+8RmlqYUf7w/gXOW8mChC509//V9dfMaV39b7WoEf/JRw9KGM69C3hIdtb7cVKD/B6VxQIq3z1DCAcmSCXpcaXUaFbVaF4u/vEi+3v5DdPtDl/0rOy2NUFNL5XULW8OxdofzUbdL9SWN/IbwIDAQAB;
```
You have successfully added a TXT record for MultiSafepay's email servers.

### Mandrill
1. Add a TXT record named: `mandrill._domainkey.{your domain}`, where `{your domain}` contains your website domain.
{{< br >}}For example: `mandrill._domainkey.myamazingwebshop.com`

2. Add the following content to your TXT record:
```
v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrLHiExVd55zd/IQ/J/mRwSRMAocV/hMB3jXwaHH36d9NaVynQFYV8NaWi69c1veUtRzGt7yAioXqLj7Z4TeEUoOLgrKsn8YnckGs9i3B3tVFB+Ch/4mPhXWiNfNdynHWBcPcbJ8kjEQ2U8y78dHZj1YeRXXVvWob2OaKynO8/lQIDAQAB;
```
You have successfully added a TXT record for Mandrill.

## See also
[Adding SPF DNS records for MultiSafepay emails](/account/adding-spf-dns-records/)





