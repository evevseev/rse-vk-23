import psycopg2


conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="xxx.xxx.xxx.xxx", port=5432)


def create_ips(cursor, ips):
    argument_string = ",".join("('%s', '%s')" % (ip, case) for ip, case in ips)
    cursor.execute("INSERT INTO ips (ip, case_id) VALUES" + argument_string)


def create_cases(cursor, cases):
    argument_string = ",".join(
        "('%s', '%s', '%s', '%s')" % (ind, organization, number, date) for (ind, organization, number, date) in cases)
    cursor.execute("INSERT INTO cases (id, organization, number, date) VALUES" + argument_string)


def create_domains(cursor, domains):
    argument_string = ",".join("('%s', '%s')" % (domain, case) for domain, case in domains)
    cursor.execute("INSERT INTO domains (domain, case_id) VALUES" + argument_string)
