# Examination 1 - Understanding SSH and public key authentication

Connect to one of the virtual lab machines through SSH, i.e.

    $ ssh -i deploy_key -l deploy webserver

Study the `.ssh` folder in the home directory of the `deploy` user:

    $ ls -ld ~/.ssh

Look at the contents of the `~/.ssh` directory:

    $ ls -la ~/.ssh/

## QUESTION A

What are the permissions of the `~/.ssh` directory?

Answer:

    drwx------ 2 deploy deploy 29 Oct 16 08:57 .ssh

Why are the permissions set in such a way?

Answer:

Permissions drwx------ represents 700 and that means only the owner (deploy) has right to read, write or access this folder.
This prevents others from viewing private keys and keeps SSH secure.

## QUESTION B

What does the file `~/.ssh/authorized_keys` contain?

Answer:

It contains public keys of users allowed to log in without a password.
Each line is one key used for key-based authentication.

## QUESTION C

When logged into one of the VMs, how can you connect to the
other VM without a password?

Answer:

Generate and copy your key to the other VM:

    ssh-keygen -t ed25519
    ssh-copy-id deloy@other-vm

Now you can SSH without a password.

### Hints:

- man ssh-keygen(1)
- ssh-copy-id(1) or use a text editor

## BONUS QUESTION

Can you run a command on a remote host via SSH? How?

Yes. Example:

    ssh deploy@webserver "uptime"

Runs a remote command directly
