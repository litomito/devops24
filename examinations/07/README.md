# Examination 7 - MariaDB installation

To make a dynamic web site, many use an SQL server to store the data for the web site.

[MariaDB](https://mariadb.org/) is an open-source relational SQL database that is good
to use for our purposes.

We can use a similar strategy as with the _nginx_ web server to install this
software onto the correct host(s). Create the playbook `07-mariadb.yml` with this content:

    ---
    - hosts: db
      become: true
      tasks:
        - name: Ensure MariaDB-server is installed.
          ansible.builtin.package:
            name: mariadb-server
            state: present

# QUESTION A

Make similar changes to this playbook that we did for the _nginx_ server, so that
the `mariadb` service starts automatically at boot, and is started when the playbook
is run.

Using the `service` module to **enable at boot** and **start now**. Service name is `mariadb` on Alma/RHELL

    ---
    - name: Install and start MariaDB
      hosts: db
      become: true
      tasks:
        - name: Ensure MariaDB server is installed
          ansible.builtin.package:
            name: mariadb-server
            state: present

        - name: Ensure MariaDB is enabled and started
          ansible.builtin.service:
            name: mariadb
            enabled: true
            state: started

# QUESTION B

When you have run the playbook above successfully, how can you verify that the `mariadb`
service is started and is running?

You can verify that MaridaDB is running using **Ansible facts** like this:

    - name: Collect services facts
      ansible.builtin.service_facts:

    - name: Ensure mariadb-server is running
      ansible.builtin.debug:
        msg: "Mariadb is running"
      when: ansible_facts.services['mariadb.service'].state == 'running'

This checks the actual running state of the MaariaDB service directly from system facts, no manual commands needed.

# BONUS QUESTION

How many different ways can use come up with to verify that the `mariadb` service is running?

Different ways to verify **examples**:

1. `systemctl is-active mariadb`
2. `systemctl status mariadb`
3. `journalctl -u mariadb -n 50`
   and so on...
