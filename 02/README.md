# RHCE Ansible Practice 2
## Using variables and facts

\* Username is `vagrant` with a password of `vagrant` if you need it.

1. Create an inventory file that groups the 2 nodes in the following way:
    - `node1` is in the `dev` group.
    - `node2` is in the `prod` group.

2. Create a file named `ansible.cfg` and do the following:
    - set the default inventory to your newly created file.
    - set the default user to `vagrant`
    - set it to ignore deprecation warnings
    - set up privilege escalation to become `root` using `sudo`.
    - set privilege escalation to default to not becoming root.
    - set privilege escalation to never ask for a password.

3. Create a vars file that contains the following values:
    ```
        web_pkgs = httpd, httpd-tools, mariadb-server, mariadb, firewalld
        test_pkgs = nginx, mariadb-server, mariadb, firewalld
        web_svcs = httpd, mariadb, firewalld
        test_svcs = nginx, mariadb firewalld
        dev_web_root = /usr/share/nginx/html
        prod_web_root = /var/www/html
        firewall_pkg = firewalld
        web_groups = devs, admins, editors, contribs
        web_users =  hannibal = uname: hannibal, comment: "John Hannibal Smith", uid: 4001, groups: "hannibal, wheel, admins"
                     face = uname: face, comment: "Templeton Faceman Peck", uid: 4002, groups: "face, admins"
                     ba = uname: ba, comment "BA Baracas", uid: 4003, groups: "ba, editors"
                     murdock = uname: murdock, comment: "Howling Mad Murdock", uid: 4004, groups: "murdock, contribs"
        firewall_rules = http, ssh
    ```
    I have included a `vars.yml` file in the `files` directory if you have trouble.

4. Create a `vault` directory and use `ansible-vault` to create a file called `secrets.yml` that includes:
    ```
    username: hannibal
    pwhash: $6$5ryGYaiSQ1dIEcNE$6EknsP3ILd8VDKs7py0MY78CtWHSzJ5Q3ErYyZRVeSAZiMHoRmNzcQMeucZJAGyBWxhmh/8xgrUl3hhQtfvbZ/
    ```
5. Create a playbook that will consist of 4 plays (`dev`, `prod`, `all`, `localhost`):
    - Create all of the `web_groups` and `web_users` on all servers using the variables from the `vars.yml` file.
    - Use the secrets.yml file to change the password for user `hannibal` to `A-Team` (the pwhash is already correct for this pw).
    - Install the `test_pkgs` and `firewall_pkg` on the `dev` group.
    - Enable and run the the `test_svcs` on the `dev` group.
    - Place an `index.html` file in the `dev_web_root` directory that contains the following text: "I love it when a plan comes together".
    - Create and apply permanent firewall rules using the `firewall_rules` variable for `dev`
    - Install the `web_packages` on the `prod` group.
    - Enable and run the the `web_svcs` on the `prod` group.
    - Place an `index.html` file in the `prod_web_root` directory that contains the following text: "I love it when a plan comes together".
    - Create and apply permanent firewall rules using the `firewall_rules` variable for `prod`
    - Create a play that will use localhost to test the accessability of each webserver.
