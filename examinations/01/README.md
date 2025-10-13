# Examination 1 - Understanding SSH and public key authentication

Connect to one of the virtual lab machines through SSH, i.e.

    $ ssh -i deploy_key -l deploy webserver

Study the `.ssh` folder in the home directory of the `deploy` user:

    $ ls -ld ~/.ssh

Look at the contents of the `~/.ssh` directory:

    $ ls -la ~/.ssh/

## QUESTION A

What are the permissions of the `~/.ssh` directory?

Svar: drwx------. 2 deploy deploy 29 Oct 13 11:39 .

Why are the permissions set in such a way?

Svar: Mappen innehåller känsliga filer. Om andra kan lista innehållet eller läsa filer i .ssh kan de komma åt dina nycklar eller konfiguration.

## QUESTION B

What does the file `~/.ssh/authorized_keys` contain?

Svar: Denna fil innehåller de publika nycklarna som matchas med de privata nycklarna för att kunna logga in via ssh

## QUESTION C

When logged into one of the VMs, how can you connect to the
other VM without a password?

Svar: Man skapar först en nyckel på VM1 sen kopierar man den publika nyckeln till authorized_keys i VM2. Sedan kan man SSHa utan lösenord.

### Hints:

* man ssh-keygen(1)
* ssh-copy-id(1) or use a text editor

## BONUS QUESTION

Can you run a command on a remote host via SSH? How?

Svar: Ja det funkar. T.ex. ssh webserver 'echo hej'. Kommandot inom enkla citattecken (' ') är det som körs på den fjärranslutna servern. När kommandot är klart stängs SSH-anslutningen automatiskt och resultatet visas i den lokala terminalen.

