# RHCE Ansible Practice 3
## Loops and Vars

\* Username is `vagrant` with a password of `vagrant` if you need it.

1. Edit your `inventory` file to create a group called `choctaw` that includes both the `webtest` and `webprod` groups.

2. Create a playbook named `playbook.yml`. In it, write a play that is aimed at the `choctaw` group

3. Write task that uses a loop to create the following groups:
    - `simpsons`
    - `flanders`
    - `wiggums`
    - `donut_lovers`

4. Add second task that will use a loop to create these users and put them into the correct groups using the `users` dict from the `vars.yml` file.
    - `homer, marge, bart, lisa` go in the `simpsons` group
    - `ned, rod`, and `todd` go in the `flanders` group
    - `chief` and `ralph` go in the `wiggums` group
    - `homer` and `chief` go in the `donut_lovers` group


5. Add a third task that uses a loop with the file command with the group_dirs variable to to create the following directories with the proper attributes.
    - `donut_shop_reviews (owner: homer, group: donut_lovers, permissions: 0644)`
    - `bible_verses (owner: ned, group: flanders, permissions: 777)`
    - `police_reports (owner: chief, group: wiggums, permissions: 0600)`

6.  Add a second play to the playbook that will install the required_packages (defined in the `vars.yml` file) on webtest machine only. The play should also create `firewalld` rules along with the `firewall_rules` variable to make sure that they are both running.

7. Add a third play to the playbook that only applies to the `webprod` machine. In it create the following tasks.
    - Uses a loop and `ansible_facts` to add the following line to files in the `banner_paths` variable: "This (DISTRIBUTION) (VERSION) server has been configured by Ansible.