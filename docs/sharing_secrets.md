---
title: Sharing secrets
description: How to share secrets with Dexter during the pilot phase.
---

During the pilot phase, you may not always be able to enter secrets like API keys directly into Dexter. You can securely share secrets with Dexter using your password manager or public-key cryptography.

If you'd prefer to share secrets using a different method, please let us know. We're happy to accommodate your needs.

## Using a password manager

During the pilot phase, you can share secrets with Dexter using the sharing functionality of your password manager:

- [1Password](https://support.1password.com/share-items/)
- [LastPass](https://support.lastpass.com/s/document-item?language=en_US&bundleId=lastpass&topicId=LastPass/share-passwords.html&_LANG=enus)

## Using public-key cryptography

You can share secrets with Dexter using public-key cryptography. Here's how it works:

1. Write the secret in a text file (e.g. `secret.txt`)
1. Download Dexter's public key
1. Encrypt the secret using `openssl` and Dexter's public key

    ```
    openssl pkeyutl -encrypt -pubin -inkey dexter.pub -in secret.txt -out secret.enc
    ```

1. Send the encrypted secret file to Dexter via email to [vincent@getdexter.co]

We will decrypt the secret using our private key and use it to configure Dexter for you.

### Dexter's public key

```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAlLkP0+HlHlyY/ht4Ea29
Fpm/msKZJdyfOa6pTrQHrQ+eXbewglOPtT6907dGNKPwJvAp70NCoER7CQSelryN
SmLtk5rFDOThn9zqprPOy/m8Lhu/CvPS1Sq8dGDfzrh+/41E0duY47e4dRFWfBdL
vddpYoUEhOUlv4hRUTxSrEF1r2IeOAUqHHfAz1yhbRpzcRu7vybno7oLvVt+2a9G
pkxYaOmLKwh8JkgstHy05MGBYE3WoG/qIHJm9ZlQN3dfhywEOw+/YzBVM6hjNjXG
WNVbtIvMTBrbn2qarAxfW8pMQjgt2vzAJRdVfwufSV4z/4bGudbE87CyT7mnahjo
dtQu3fvEILjJPA89uAGsyuqVIpnyp9MsNOFIFNQ7rh2rRx51YfMSfe/prhOGf0j6
4/hVwjq68q1a37LjVC8BEVQc7Se3xQ5OdQeOT2c8HiVcXeToILHWQQTDlFBMrG7X
F5OLGGh3z2Pxuke97JHwXTZWq8NJmZE4mD2CndckDb5xqSn946/MPwegCuQtQZqj
sXtFq+ln00jeMgDuvKPGgV0pviBqXtmgeO3ltJD3zo4drNk/8RdOS4hAYyYwspd7
lLPWPSiAZWaUL7lRlLo5Gou6dD3MyY8ryibk461JVATufUaYsWQY0w5SOwWiOs/8
C4UkIs3dISi2/Ej9sf4mSSECAwEAAQ==
-----END PUBLIC KEY-----
```

[vincent@getdexter.co]: mailto:vincent@getdexter.co
