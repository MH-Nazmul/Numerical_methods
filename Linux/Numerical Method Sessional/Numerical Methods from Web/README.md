# E7-Textbook

**This is the production repo for the textbook.**

## Setup

To set up the book on the OCF account, use SFTP to transfer this repo's contents to the machine 
and symlink `_out` in this repo with the `~/public_html` folder on the machine.

## Make Changes

1. Make changes to your repo, PR into this repo
2. Pull changes to local copy of *this* repo
3. In local copy of this repo, run `make book`
4. Commit and push
5. SSH into OCF (`e7staff@ssh.ocf.berkeley.edu`)
6. `cd` in `~/E7-Textbook` (a copy of this repo)
7. Pull changes
8. Run `make prod`

Done!




<!-- 
To make changes to the book, edit the notebooks and run `make book` locally. Commit and push, then
follow the **Build** instructions below to push these changes to prod.

OCF username: `e7staff`

To make changes to the book in production, transfer the changes via SFTP to the machine, SSH into it
(`e7staff@ssh.ocf.berkeley.edu`), `cd` into this repo, and run `make prod`.
-->
