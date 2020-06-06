# RHCE Ansible Practice 4
## Handlers

\* Username is `vagrant` with a password of `vagrant` if you need it.

Use the playbook.yml to do the following:
1. Create a play for the `webservers` group that uses these local variables:
  - `web_pkg: httpd`
  - `firewall_pkg: firewalld`
2. Create a task to install the two packages using those variables.
3. Make another task that will use the `app_svcs` variable from `vars.yml` to ensure the services are started and enabled.
4. Make a task that uses the copy module with the `web_svc_config_files` variable to move the custom configurations to the appserver. This task should trigger the `Restart httpd` handler.
5. Write a task that uses the `lineinfile` module to add the lines from the `ssh_config` variable to the `ssh_config_file`. This task should trigger the `Restart sshd` handler.
6. Write another task that takes the line `PermitRootLogin yes` line out of the `ssh_config_file`. This task should also trigger the `Restart sshd` handler.
7. Create a task that allows normal http traffic through the firewall.
8. Make a task that creates an `index.html` file. It should:
  - Use facts to create this dynamic message: "Welcome to (HOSTNAME) webserver! All (AMOUNT OF MEMORY) MBs of memory are working hard to serve this page up to you!"
  - Be placed in the `web_root` directory
9. Create another play that uses the localhost to test each webserver for accessability.