# SSH -- ALX

>Must Read: [SSH Essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys#ssh-overview)

## How I setup my server

The process is all in the [article](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys#ssh-overview), but just to save your time, so after [generating my key-pairs(public and private keys)](#generating-key-pairs):

- Manually copy public key

```bash
cat ~/.ssh/id_rsa.pub
```

- Paste key in intranet profile
- Request a server and run

```bash
$ ssh-copy-id <your server username>@<your server ip>
```

> Just do it, cause untill i did this, my issue wasn't resolved.

That should be all, you can check out your server with `ssh username@remote_host`

## Generating Key pairs
Run:

```bash
$ ssh-keygen
```

and follow the prompt.

> Help from [https://askubuntu.com/questions/4830/easiest-way-to-copy-ssh-keys-to-another-machine/4833#4833](https://askubuntu.com/questions/4830/easiest-way-to-copy-ssh-keys-to-another-machine/4833#4833)