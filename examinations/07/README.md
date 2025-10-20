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

# QUESTION B

When you have run the playbook above successfully, how can you verify that the `mariadb`
service is started and is running?

Svar: Jag hittade ett sätt att kontrollera om mariaDB är running via min playbook. Jag börjar med att köra modulen ansible.builtin.service_facts: som samlar information. Sedan kör jag en annan modul som heter ansible.builtin.debug: med ett meddelande som säger "mariaDB is running" men detta körs endast när mariadb.service == running. ifall den är stoppad så skippas denna task.

# BONUS QUESTION

How many different ways can use come up with to verify that the `mariadb` service is running?

Svar: Jag kan gå in på db servern och köra sudo systemctl status mariadb för att se om det står active. Jag kan även köra min playbook med de tasksen som jag förklarade i förra frågan för att verifiera att den är running.

Precis som ansible.builtin.service_facts sättet att verifiera så hittade jag ett liknande sätt att verifiera om mariaDB körs och det är genom att använda ansible.builtin.command och skriva ett kommando för att sedan lagra utmatningen i en variabel. Jag kan sedan skriva ut ett meddelande beroende på vad stdout är när jag kör det kommandot. Detta är samma sak som att skriva ett kommando direkt i DB servern men detta sätt automatiserar det istället.

    - name: Check MariaDB status with command
      ansible.builtin.command: systemctl is-active mariadb
      register: result
      changed_when: false

    - name: Verify status
      ansible.builtin.debug:
        msg: "MariaDB is active"
      when: result.stdout == "active"